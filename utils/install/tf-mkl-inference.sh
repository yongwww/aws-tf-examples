#Example Inference benchmark on Amazon DL AMI.
#Launch a DL AMI

#Create an virtual envirnoment. 
conda create -n tf1.8_mkl-master python=3.6 
source activate tf1.8_mkl-master

#Download the tf1.8 wheel built with MKLDNN master branch on 05-31-2018
wget https://www.dropbox.com/s/y812q7zpdy4pjed/tensorflow-1.8.0-cp36-cp36m-linux_x86_64.whl
#pip install the wheel
pip install tensorflow-1.8.0-cp36-cp36m-linux_x86_64.whl

# Clone benchmark scripts
git clone https://github.com/tensorflow/benchmarks.git   
cd benchmarks/scripts/tf_cnn_benchmarks/  

#Setup num_intra_threads and num_inter_threads
num_cores=4
num_inter_t=2 

# Set MKL environment variables
export KMP_AFFINITY=granularity=fine,verbose,compact,1,0
export KMP_BLOCKTIME=1
export KMP_SETTINGS=1
export OMP_NUM_THREADS=$num_cores
export OMP_PROC_BIND=true

#Setup network
#networks=( alexnet googlenet inception3 resnet50 resnet152 vgg16 )
network=inception3

# Run Inference benchmark, please note the data format is NCHW is optimized for MKL
python tf_cnn_benchmarks.py  --data_format NCHW --model $network --batch_size 1 --num_batches 30 \
--num_intra_threads $num_cores --num_inter_threads $num_inter_t --forward_only=True
