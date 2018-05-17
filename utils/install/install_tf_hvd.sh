#!/bin/bash
# 
# install tensorflow and horovod on AWS DLAMI
#
# usage: sh install_tf_hvd.sh
#

# install tensorflow and horovod
pip install tensorflow_gpu && pip install --no-cache-dir horovod
