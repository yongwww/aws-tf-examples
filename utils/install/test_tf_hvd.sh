#!/bin/bash
# 
# test tensorflow and horovod on AWS DLAMI
#
# usage: sh test_tf_hvd.sh 
#

git clone https://github.com/tensorflow/benchmarks
cd benchmarks/scripts/tf_cnn_benchmarks/ 
mpirun -np 8 -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH python tf_cnn_benchmarks.py --variable_update horovod --model resnet101 --batch_size 64
