# aws-tf-examples
### Prepare tfrecords ImageNet dataset
In order to download imagenet dataset, you should create an ImageNet account via [http://image-net.org](http://image-net.org). Then you will have your account and access key.

1. Download and untar imagenet dataset, generate TFRecords format dataset without changing the image size <br>
```
   python ./utils/preprocess/preprocess-imagenet.py \
        --local_scratch_dir=[YOUR DIRECTORY] \
        --imagenet_username=[imagenet account \
        --imagenet_access_key=[imagenet access key]
```
2. Resize to 480px shortest size using script *tensorflow_image_resizer.py*

```
  python ./utils/preprocess/tensorflow_image_resizer.py -d imagenet \
       -i [PATH TO TFRECORD TRAINING DATASET] \
       -o  [PATH TO RESIZED TFRECORD TRAINING DATASET] \
       --subset_name train \
       --num_preprocess_threads 60 \
       --num_intra_threads 2 \
       --num_inter_threads 2
  python ./utils/preprocess/tensorflow_image_resizer.py -d imagenet \
       -i [PATH TO TFRECORD VALIDATION DATASET] \
       -o [PATH TO RESIZED TFRECORD VALIDATION DATASET] \
       --subset_name validation \
       --num_preprocess_threads 60 \
       --num_intra_threads 2 \
       --num_inter_threads 2
```


### Train model using the prepared dataset

#### Train and evluate without Horovod support
-  Train
```
python ./cnn/aws_tf_cnn.py
      --num_epochs=90 \
      --batch_size=256 \
      --display_every 100 \
      --data_dir=[PATH TO TFRECORD TRAINING DATASET] \
      --log_dir=[PATH TO CHECKPOINT DIR] \
      -m resnet50 \
      --num_gpus=8 \
      --fp16
```
- Evaluate (Top-1 and Top-5 validation accuracy)
```
python ./cnn/aws_tf_cnn.py
      --num_epochs=90 \
      --batch_size=256 \
      --display_every 100 \
      --data_dir=[PATH TO TFRECORD VALIDAGTION DATASET] \
      --log_dir=[PATH TO CHECKPOINT DIR] \
      -m resnet50 \
      --num_gpus=8 \
      --fp16 \
      --eval
```

#### Train and evluate with Horovod support
We recommend you to install horovod and used horovod based script to train, which could speed up the training. Please follow the [guide](https://github.com/uber/horovod/blob/master/docs/gpus.md) to enable Horovod.

- Train
```
mpiexec --allow-run-as-root --rankfile rankfile \
        --hostfile hostfile -np 8 python -u aws_tf_hvd_cnn.py \
        --batch_size=256 --num_epochs=90 --fp16 \
        --data_dir [PATH TO TFRECORD TRAINING DATASET] \
        --model resnet50 --log_dir /home/ubuntu/results/hvd_0327 \
        --display_every 100
```

- Evaluate (Top-1 and Top-5 validation accuracy)
```
python -u aws_tf_hvd_cnn.py --batch_size=256 \
       --num_epochs=90 --data_dir [PATH TO TFRECORD VALIDAGTION DATASET] \
       --model resnet50 --log_dir [PATH TO CHECKPOINT DIR] \
       --display_every 100  \
       --eval
```