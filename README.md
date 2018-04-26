# aws-tf-examples
### Prepare TFRecord format ImageNet dataset
image-net.org hosts the raw dataset, it is required to get your specific imagenet account and related access key from  [http://image-net.org](http://image-net.org) to download the dataset.

1. Download and untar imagenet raw dataset, generate TFRecord format dataset <br>
```
   python ./utils/preprocess/preprocess_imagenet.py \
             --local_scratch_dir=[YOUR DIRECTORY] \
             --imagenet_username=[imagenet account] \
             --imagenet_access_key=[imagenet access key]
```
2. Resize image to 480px shortest side, maintaining original aspect ratio

```
  python ./utils/preprocess/tensorflow_image_resizer.py \
            -d imagenet \
            -i [PATH TO TFRECORD TRAINING DATASET] \
            -o  [PATH TO RESIZED TFRECORD TRAINING DATASET] \
            --subset_name train \
            --num_preprocess_threads 60 \
            --num_intra_threads 2 \
            --num_inter_threads 2
  python ./utils/preprocess/tensorflow_image_resizer.py \
            -d imagenet \
            -i [PATH TO TFRECORD VALIDATION DATASET] \
            -o [PATH TO RESIZED TFRECORD VALIDATION DATASET] \
            --subset_name validation \
            --num_preprocess_threads 60 \
            --num_intra_threads 2 \
            --num_inter_threads 2
```


### Train and evaluate ResNet50 using the resized TFrecord format ImageNet dataset

#### Train and evaluate with Horovod support
We recommend installing horovod and using the horovod based script to train for a better performance.(Please follow the [guide](https://github.com/uber/horovod/blob/master/docs/gpus.md) to enable Horovod) The rankfile and hostfile are used to help pin CPUs to the socket near the appropriate GPU, they are supposed to be edited as needed based on the specific computation environment. 

- Train ResNet50
```
mpiexec --allow-run-as-root --rankfile rankfile --hostfile hostfile -np 8 \
        python -u aws_tf_hvd_cnn.py \
        --model resnet50 --batch_size=256 --num_epochs=90 --fp16\
        --data_dir [PATH TO TFRECORD TRAINING DATASET] \
        --log_dir [PATH TO RESULT]] \
        --display_every 100 
```

- Evaluate (Top-1 and Top-5 validation accuracy)
```
python -u aws_tf_hvd_cnn.py --batch_size=256 \
       --num_epochs=90 --data_dir [PATH TO TFRECORD VALIDAGTION DATASET] \
       --model resnet50 --log_dir [PATH TO RESULT] \
       --display_every 100  \
       --eval
```

#### Train and evaluate without Horovod support (Optional)
-  Train resnet50
```
python ./cnn/aws_tf_cnn.py
            --num_epochs=90 \
            --batch_size=256 \
            --display_every 100 \
            --data_dir=[PATH TO TFRECORD TRAINING DATASET] \
            --log_dir=[PATH TO CHECKPOINT DIR] \
            --model=resnet50 \
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
            --model=resnet50 \
            --num_gpus=8 \
            --fp16 \
            --eval
```

