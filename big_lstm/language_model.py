import tensorflow as tf

from model_utils import sharded_variable, variable_summaries
from common import assign_to_gpu, average_grads, find_trainable_variables
from hparams import HParams
from model_utils import LSTMCell


class LM(object):
    def __init__(self, hps, mode="train", ps_device="/gpu:0"):
        self.hps = hps
        data_size = hps.batch_size * hps.num_gpus
        self.x = tf.placeholder(tf.int32, [data_size, hps.num_steps])
        self.y = tf.placeholder(tf.int32, [data_size, hps.num_steps])

        losses = []
        tower_grads = []
        xs = tf.split(self.x, hps.num_gpus, 0)
        ys = tf.split(self.y, hps.num_gpus, 0)
        for i in range(hps.num_gpus):
            with tf.device(assign_to_gpu(i, ps_device)), tf.variable_scope(tf.get_variable_scope(),
                                                                           reuse=True if i > 0 else None):
                loss = self._forward(i, xs[i], ys[i])
                losses += [loss]
                if mode == "train":
                    cur_grads = self._backward(loss,  summaries=((i == hps.num_gpus - 1) and hps.do_summaries))
                    tower_grads += [cur_grads]

        self.loss = tf.add_n(losses) / len(losses)
        tf.summary.scalar("model/loss", self.loss)

        self.global_step = tf.get_variable("global_step", [], tf.int32, trainable=False)

        if mode == "train":
            grads = average_grads(tower_grads)
            if hps.optimizer == 1:
                optimizer = tf.train.MomentumOptimizer(hps.learning_rate, 0.9)
            elif hps.optimizer == 2:
                optimizer = tf.train.AdamOptimizer(hps.learning_rate)
            elif hps.optimizer == 3:
                optimizer = tf.train.RMSPropOptimizer(learning_rate=hps.learning_rate)
	    elif hps.optimizer == 4:
		optimizer = tf.train.GradientDescentOptimizer(hps.learning_rate)
            else:
                optimizer = tf.train.AdagradOptimizer(hps.learning_rate, initial_accumulator_value=1.0)
            self.train_op = optimizer.apply_gradients(grads, global_step=self.global_step)
            self.summary_op = tf.summary.merge_all()
        else:
            self.train_op = tf.no_op()

        if mode in ["train", "eval"] and hps.average_params:
            with tf.name_scope(None):  # This is needed due to EMA implementation silliness.
                # Keep track of moving average of LSTM variables.
                ema = tf.train.ExponentialMovingAverage(decay=0.999)
                variables_to_average = find_trainable_variables("LSTM")
                self.train_op = tf.group(*[self.train_op, ema.apply(variables_to_average)])
                self.avg_dict = ema.variables_to_restore(variables_to_average)

    def _forward(self, gpu, x, y):
        hps = self.hps
        self.initial_states = []
        for i in range(hps.num_layers):
            with tf.device("/gpu:%d" % gpu):
                state = tf.Variable(tf.zeros([hps.batch_size, hps.state_size + hps.projected_size],
                                             dtype=tf.float32),
                                    trainable=False, collections=[tf.GraphKeys.LOCAL_VARIABLES],
                                    name="state_%d_%d" % (gpu, i), dtype=tf.float32)
                self.initial_states += [state]

        emb_vars = sharded_variable("emb", [hps.vocab_size, hps.emb_size],
                                    hps.num_shards, dtype=tf.float32)

        x = tf.nn.embedding_lookup(emb_vars, x)  # [bs, steps, emb_size]
        if hps.keep_prob < 1.0:
            x = tf.nn.dropout(x, hps.keep_prob)

        inputs =  [tf.squeeze(tf.cast(v, tf.float32), [1]) for v in tf.split(x, hps.num_steps, 1)]

        for i in range(hps.num_layers):
            with tf.variable_scope("lstm_%d" % i):
                cell = LSTMCell(hps.state_size, hps.emb_size, num_proj=hps.projected_size, dtype=tf.float32)

            state = self.initial_states[i]
            for t in range(hps.num_steps):
                inputs[t], state = cell(inputs[t], state)
                if hps.keep_prob < 1.0:
                    inputs[t] = tf.nn.dropout(inputs[t], hps.keep_prob)

            with tf.control_dependencies([self.initial_states[i].assign(state)]):
                inputs[t] = tf.identity(inputs[t])

        inputs = tf.reshape(tf.concat(inputs, 1), [-1, hps.projected_size])

        # Initialization ignores the fact that softmax_w is transposed. Twhat worked slightly better.
        softmax_w = sharded_variable("softmax_w", [hps.vocab_size, hps.projected_size], hps.num_shards)
        softmax_b = tf.get_variable("softmax_b", [hps.vocab_size])

        if hps.num_sampled == 0:
            full_softmax_w = tf.reshape(tf.concat(softmax_w, 1), [-1, hps.projected_size])
            full_softmax_w = full_softmax_w[:hps.vocab_size, :]

            logits = tf.matmul(tf.to_float(inputs), full_softmax_w, transpose_b=True) + softmax_b
            targets = tf.reshape(y, [-1])
            loss = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=targets)
        else:
            targets = tf.reshape(y, [-1, 1])
            loss = tf.nn.sampled_softmax_loss(softmax_w, softmax_b, targets, tf.to_float(inputs),
                                               hps.num_sampled, hps.vocab_size)
        loss = tf.reduce_mean(loss)
        return loss

    def _backward(self, loss, summaries=False):
        hps = self.hps

        loss = loss * hps.num_steps

        emb_vars = find_trainable_variables("emb")
        lstm_vars = find_trainable_variables("LSTM")
        softmax_vars = find_trainable_variables("softmax")

        all_vars = emb_vars + lstm_vars + softmax_vars
        grads = tf.gradients(loss, all_vars, aggregation_method=tf.AggregationMethod.EXPERIMENTAL_ACCUMULATE_N)
        orig_grads = grads[:]
        emb_grads = grads[:len(emb_vars)]
        grads = grads[len(emb_vars):]
        for i in range(len(emb_grads)):
            assert isinstance(emb_grads[i], tf.IndexedSlices)
            emb_grads[i] = tf.IndexedSlices(emb_grads[i].values * hps.batch_size, emb_grads[i].indices,
                                            emb_grads[i].dense_shape)

        lstm_grads = grads[:len(lstm_vars)]
        softmax_grads = grads[len(lstm_vars):]

        lstm_grads, lstm_norm = tf.clip_by_global_norm(lstm_grads, hps.max_grad_norm)
        clipped_grads = emb_grads + lstm_grads + softmax_grads
        assert len(clipped_grads) == len(orig_grads)

        if summaries:
            with tf.device("/cpu:0"):
                tf.summary.scalar("model/lstm_grad_norm", lstm_norm)
                tf.summary.scalar("model/lstm_grad_scale", tf.minimum(hps.max_grad_norm / lstm_norm, 1.0))
                tf.summary.scalar("model/lstm_weight_norm", tf.global_norm(lstm_vars))
                #embeding vars and grads
                for v, g in zip(emb_vars, emb_grads):
                    name = v.name[6:]
                    gname = 'dLoss_by_' + name
                    variable_summaries(v, "Embedding_weights", name)
                    variable_summaries(g, "Embedding_gradients", gname)
                #LSTM vars and gradients
                for v, g in zip(lstm_vars, lstm_grads):
                    name = v.name[6:]
                    gname = 'dLoss_by_' + name
                    variable_summaries(v, "LSTM_weights", name)
                    variable_summaries(g, "LSTM_gradients", gname)
                #softmax vars and gradients
                for v, g in zip(softmax_vars, softmax_grads):
                    name = v.name[6:]
                    gname = 'dLoss_by_' + name
                    variable_summaries(v, "Softmax_weights", name)
                    variable_summaries(g, "Softmax_gradients", gname)

        return list(zip(clipped_grads, all_vars))

    @staticmethod
    def get_default_hparams():
        return HParams(
            batch_size=128,
            num_steps=20,
            num_shards=8,
            num_layers=1,
            learning_rate=0.2,
            max_grad_norm=10.0,
            num_delayed_steps=150,
            keep_prob=0.9,
            optimizer = 0,
            vocab_size=793470,
            emb_size=512,
            state_size=2048,
            projected_size=512,
            num_sampled=8192,
            num_gpus=8,
            average_params=True,
            run_profiler=False,
            do_summaries=False,
            max_time=180,
)
