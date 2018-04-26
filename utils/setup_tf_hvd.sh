#!/bin/bash
# 
# conda install tensorflow and horovod on AWS DLAMI
#
# usage: sh setup_tf_hvd.sh condaEnvName tfBinaryURL
#
# example: sh setup_tf_hvd.sh tensorflow_horovod  \
#             https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.7.0-cp36-cp36m-linux_x86_64.whl


if [ "$#" -ne 2 ]; then
    echo "Invalid number of parameters"
fi

# create conda environment
conda create -n "$1" -y pip python="3.6"

# activate package
source activate $1

# install tensorflow
source activate $1; pip install --ignore-installed --upgrade "$2"

# install horovod
source activate $1; pip install --no-cache-dir horovod
