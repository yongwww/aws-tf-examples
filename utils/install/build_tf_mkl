# Launch a AMZ DL AMI (Ubuntu)
#Install Bazel with --user, it will be installed at /home/ubuntu/.bazel
wget https://github.com/bazelbuild/bazel/releases/download/0.13.1/bazel-0.13.1-installer-linux-x86_64.sh
chmod +x bazel-0.13.1-installer-linux-x86_64.sh
./bazel-0.13.1-installer-linux-x86_64.sh --user
source /home/ubuntu/.bazel/bin/bazel-complete.bash  

#Create and activate a virtual envirnoment. 
conda create -n tf1.8_mkl-master_build python=3.6 
source activate tf1.8_mkl-master_build

#Git clone MKLDNN master branch
git clone https://github.com/intel/mkl-dnn.git

#Git clone tensorflow master branch
git clone https://github.com/tensorflow/tensorflow.git
cd tensorflow
./configure
#Build based on broadwell, this will work on SKX and will use AVX512 as it jit compiled.
bazel build --config=mkl  --copt="-mfma" --copt="-mavx2" --copt="-march=broadwell" \
--copt="-O3" -s -c opt //tensorflow/tools/pip_package:build_pip_package

#This will create a bazel cache directory at /home/ubuntu/.bazel/bazel/_bazel_ubuntu/
#Find the correct cache folder name. During the build process, it should be printing that cache folder name.

#For EXAMPLE if the the cache directory name is "5e31cf4ff73bf2b9254653feb9a03f61", copy the git cloned MKLDNN contents to it.
#Assuming the MKLDNN is cloned to home directory /home/ubuntu/mkl-dnn, copy the contents to the bazel cache directory

cp -pra /home/ubuntu/mkl-dnn/* /home/ubuntu/.cache/bazel/_bazel_ubuntu/5e31cf4ff73bf2b9254653feb9a03f61/external/mkl_dnn/

#Build again
bazel build --config=mkl  --copt="-mfma" --copt="-mavx2" --copt="-march=broadwell" \
--copt="-O3" -s -c opt //tensorflow/tools/pip_package:build_pip_package

#Build the Python Wheel
./bazel-bin/tensorflow/tools/pip_package/build_pip_package /home/ubuntu/ 

#Remove any existing TensorFlow installation, which is unlikely if this is created in the new virtual envirnoment.
pip uninstall tensorflow

#pip install the wheel
pip install /home/ubuntu/<name_of_the_wheel>.whl
