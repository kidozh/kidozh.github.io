---
title: Ubuntu 16.04+OpenCL+Tensorflow+Keras配置参考
date: 2017-07-08 21:16:56
tags:
---

# 前言

平常正儿八经的拿CPU跑Tensorflow也问题不大，直到最近我跑了一个RNN模型之后，CPU的300+s的一个epoch实在让我无法忍受了，所以痛定思痛的我选择了GPU来跑算法。但是很尴尬的是，我用的是农企的显卡，跑不了主流的CUDA，在经过两三天的配置之后，终于成功的配置好了开启OpenCL支持的Tensorflow了，跑LSTM还是很愉快的。

# 安装Ubuntu 16.04 LTS

因为目前农企实质上已经不支持fglrx了，而且对于我的显卡`Advanced Micro Devices, Inc. [AMD/ATI] Mars [Radeon HD 8670A/8670M/8750M] `来说，fglrx驱动总是一堆问题，所以我果断选择了16.04这个版本。在这个版本，开源驱动被支持，比如`Radeon`以及`AMD GPU Pro`。

# 准备工作

首先你需要安装`cmake`以及其他编译经常需要的工具。

```shell
## install build essentials
sudo apt-get install cmake
sudo apt-get update && sudo apt-get install build-essential
```

接下来需要安装鼎鼎大名的`boost`以及`libssl`

```shell
sudo apt-get install libssl0.9.8:i386
sudo apt-get install libboost-all-dev

sudo apt-get install libgtest-dev
cd /usr/src/gtest
sudo cmake .
sudo make
sudo mv libg* /usr/lib/
```



# 安装 Python

建议使用anaconda来安装Python 3.5。

现在主流的包和库都支持Python 3并且有些库（例如Django）已经明确宣称不支持Python 2，同时，Python 3 对Unicode良好的兼容性对于开发有中文的数据来说，非常省心。

其实这里推荐anaconda的主要原因还是因为`Theano`。因为如果你想使用带有`OpenCL`支持的`Theano`，你就必须使用其后端`libgpuarray`。而这个包在`issue`里面明确对不使用`conda`安装该库的用户提供非常有限的支持。还有一点就是anaconda自带了众多的科学计算库，一步到位确实非常省心。

## 对不使用anaconda的少年的说明

对于不想安装anaconda的少年（conda速度真的不多说，推荐使用清华tuna的源），自然我提出一些小小的参考。

你需要安装numpy等一众科学计算的库，你可能还需要安装BLAS、MKL等一系列库以求支持TF。建议知道这些东西的人手工配齐库。

如果遇到问题，百度或者google吧。

# 安装OpenCL

就我来说，AMD网上的驱动几乎不能成功。所以我选择了一种非常优雅的方式，apt安装。

> Ubuntu 16.04 has an mesa-opencl-icd package, as well as the libclc-* packages that should be enough to support open source OpenCL on AMD hardware.

```shell
$ sudo add-apt-repository ppa:paulo-miguel-dias/mesa 
$ sudo apt-get update
$ sudo apt-get install libclc-amdgcn mesa-opencl-icd
```

## 移除这个PPA

```shell
$ sudo apt-get install ppa-purge
$ sudo ppa-purge ppa:oibaf/graphics-drivers
```

更多的信息你可以参考这篇博文：[https://laanwj.github.io/2016/05/06/opencl-ubuntu1604.html](https://laanwj.github.io/2016/05/06/opencl-ubuntu1604.html)

# 为Theano安装的准备

*如果你不需要安装Theano，那么你可以跳过这一项，下面这项目会自动引用系统自带的Python，与下面所说的安装Python有所出入。*

*Theano sucks*

为`theano`的支持安装`clblas`库

```shell
## clBlas
sudo apt-get install git
git clone https://github.com/clMathLibraries/clBLAS.git
cd clBLAS/
mkdir build
cd build/
sudo apt-cache search openblas
sudo apt-get install libopenblas-base libopenblas-dev
sudo apt-get install liblapack3gf liblapack-doc liblapack-dev
cmake ../src
make
sudo make install
```

接下来安装libgpuarray

```shell
git clone https://github.com/Theano/libgpuarray.git
cd libgpuarray
mkdir Build
cd Build
cmake .. -DCMAKE_BUILD_TYPE=Release -DOPENCL_INCLUDE_DIRS=/opt/AMDAPPSDK-3.0-0-Beta/include
make
sudo make install
cd ..
sudo apt-get install cython
sudo apt-get install python-numpy python-scipy python-dev python-pip python-nose g++ libopenblas-dev git
python setup.py build
sudo python setup.py install
```

安装 Theano

```shell
## Theano
pip install Theano
sudo pip install Theano
```

# 安装Tensorflow

## 安装computeCPP

这个库真的挺奇怪的，但是安装带有OpenCL支持的Tensorflow却不得不需要这个奇怪的库。首先你需要在其官网上注册一个账号来下载ComputeCPP，和牙膏厂一个尿性，然后解压后放到`/usr/lib`或者其他你能看得到的位置。

Tensorflow对于OpenCL的支持至今都是很有限的，所以你需要的是使用**源码**来安装Tensorflow而不是优雅的使用`pip3 install tensorflow-gpu`（都怪农企喜欢造挖矿卡）

直接参考Tensorflow的如何编译源码来安装就可以了。需要注意的是在enable Tensorflow support那块需要选择**是**，而CUDA那一块则要选择**否**。假设出现了要你选择OpenCL路径地方的时候，他显示的那个路径一般都是没有错的。所以这个时候你需要检查那个路径下是否生成了`libOpencl.so`这类型的文件。

这里就是英文的说明了：[https://www.tensorflow.org/install/install_sources](https://www.tensorflow.org/install/install_sources)

# 安装Keras

一句话 `pip3 install keras`

# 如何知道我是用了OpenCL

和使用CPU一般出现的TF让你编译TF到那些奇奇怪怪的（AXS是什么）格式，我的就会出现这种信息：

```
2017-07-07 20:35:24.377623: I tensorflow/compiler/xla/service/platform_util.cc:58] platform Host present with 8 visible devices
2017-07-07 20:35:24.378838: I tensorflow/compiler/xla/service/service.cc:198] XLA service 0xaa19620 executing computations on platform Host. Devices:
2017-07-07 20:35:24.378870: I tensorflow/compiler/xla/service/service.cc:206]   StreamExecutor device (0): <undefined>, <undefined>
```

# 后记

为了pip安装得快，你可以使用一些镜像库，比如中科大，淘宝以及清华tuna等的源。这里我比较推荐学生（比如边家村职业技术学院的少年）使用清华的源来避开锐捷的追杀。下面就是使用的方法：

[https://mirrors.tuna.tsinghua.edu.cn/help/pypi/](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

然后Theano这块我怎么都没安装好，显示的是libgpuarray对我的显卡支持有限，反正错误我看不懂Orz。

最后祝各位电脑不要爆炸。