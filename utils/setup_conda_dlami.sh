#!/bin/bash
# 
# used to set up a conda package for tensorflow + horovod on DLAMI

# create conda package
conda create -n tensorflow_horovod -y pip python=3.6

# activate package
source activate tensorflow_horovod

# install tensorflow
source activate tensorflow_horovod; pip install --ignore-installed --upgrade \
    https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.7.0-cp36-cp36m-linux_x86_64.whl 

# install horovod
source activate tensorflow_horovod; pip install --no-cache-dir horovod
