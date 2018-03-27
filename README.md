# aws-tf-examples
### Prepare tfrecords ImageNet dataset
In order to download imagenet dataset, you should create an ImageNet account via [http://image-net.org](http://image-net.org). Then you will have your account and access key.

1. Download and untar imagenet dataset, generate TFRecords format dataset without changing the image size <br>
```
   python preprocess-imagenet.py \
        --local_scratch_dir=[YOUR DIRECTORY] \
        --imagenet_username=[imagenet account \
        --imagenet_access_key=[imagenet access key]
```
2. Resize to 480px shortest size using script *tensorflow_image_resizer.py*

```
  python tensorflow_image_resizer.py -d imagenet \
       -i [PATH TO TFRECORD TRAINING DATASET] \
       -o  [PATH TO RESIZED TFRECORD TRAINING DATASET] \
       --subset_name train \
       --num_preprocess_threads 60 \
       --num_intra_threads 2 \
       --num_inter_threads 2
  python tensorflow_image_resizer.py -d imagenet \
       -i [PATH TO TFRECORD VALIDATION DATASET] \
       -o [PATH TO RESIZED TFRECORD VALIDATION DATASET] \
       --subset_name validation \
       --num_preprocess_threads 60 \
       --num_intra_threads 2 \
       --num_inter_threads 2
```


### Train model using the prepared dataset

```
python ./cnn/nvcnn.py
      --num_epochs=90 \
      --batch_size=256 \
      --display_every 100 \
      --data_dir=[PATH TO TFRECORD DATASET] \
      --log_dir=[PATH TO CHECKPOINT DIR] \
      -m resnet50 \
      --num_gpus=8 \
      --fp16
```

### Evaluate (Top-1 and Top-5 validation accuracy)
```
python ./cnn/nvcnn.py
      --num_epochs=90 \
      --batch_size=256 \
      --display_every 100 \
      --data_dir=[PATH TO TFRECORD DATASET] \
      --log_dir=[PATH TO CHECKPOINT DIR] \
      -m resnet50 \
      --num_gpus=8 \
      --fp16 \
      --eval
```
