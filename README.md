# aws-tf-examples
### Prepare tfrecords ImageNet dataset
1. Create ImageNet account via official website [http://image-net.org](http://image-net.org).
2. Download and uncompress ImageNet dataset by executing *./build_imagenet_data/download-imagenet.sh*
3. Run *generate_tfrecord_protos.sh* to generate TenforFlow format dataset, do not select to resize
4. Resize to 480px shortest size using script *tensorflow_image_resizer.py*

```
python tensorflow_image_resizer.py -i /path/to/imagenet-full-tfrecord/ -o /path/to/imagenet-new-tfrecord/ --subset_name train
python tensorflow_image_resizer.py -i /path/to/imagenet-full-tfrecord/ -o /path/to/imagenet-new-tfrecord/ --subset_name validation
```


### Train model using the prepared dataset

```
python ./cnn/nvcnn_new.py
 --num_epochs=90
 --batch_size=256
 --display_every 100
 --data_dir=[PATH TO TFRECORD DATASET]
 --log_dir=[PATH TO CHECKPOINT DIR]
 -m resnet50
 --num_gpus=8
 --fp16
```

### Evaluate (Top-1 and Top-5 validation accuracy)
```
python ./cnn/nvcnn_new.py
 --num_epochs=90
 --batch_size=256
 --display_every 100
 --data_dir=[PATH TO TFRECORD DATASET]
 --log_dir=[PATH TO CHECKPOINT DIR]
 -m resnet50
 --num_gpus=8
 --fp16
 --eval
```
