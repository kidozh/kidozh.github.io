---
title: '[Python] 科学计算：Python VS. MATLAB(3)----线性代数基础'
tags:
  - MATLAB
  - Python
id: 333
categories:
  - Python
date: 2015-05-03 14:40:53
---

<span style="font-family:微软雅黑; font-size:14pt">按：在介绍工具之前先对理论基础进行必要的回顾是很必要的。没有理论的基础，讲再多的应用都是空中楼阁。本文主要设涉及线性代数和矩阵论的基本内容。先回顾这部分理论基础，然后给出MATLAB，继而给出Python的处理。个人感觉，因为Python是面向对象的，操纵起来会更接近人的正常思维；而MATLAB大多是以函数实现的，是向对象施加的一个操作。比如，A是一个矩阵，它有一个属性attr。用Python更可能是A.attr，而用MATLAB更可能是attr(A)。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**一、线形代数理论基础**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">    线形代数（linear algebra）是数学的一个分支，研究矩阵理论、向量空间、线性变换和有限维线形方程组等内容。
</span>

<span style="font-family:微软雅黑; font-size:14pt">    比较重要的思想有：1.线性代数的核心内容是研究有限维线性空间的结构和线性空间的线性变换；2.向量的线性相关性是研究线性空间结构与线性变换理论的基础；3.矩阵是有限维线性空间的线性变换的表示形式；4.线性方程组的求解问题是n维空间到m维空间线性映射求核和全体原象的问题；5.行列式是研究这些问题的一个工具。
</span>

<span style="font-family:微软雅黑; font-size:14pt">    主要内容有：1.矩阵运算：加减乘除、转置、逆矩阵、行列式、矩阵的幂、伴随矩阵；2.矩阵分块、秩、迹；3.解方程；4.线性相关；5.向量空间；6.特征值和特征向量；7.对称、相似；8.二次标准型；9.线性空间和基变换；10.正交空间；11.矩阵对角化；13.矩阵分解；14.重要数字特征。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**二、MATLAB的处理**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">**1.建立矩阵**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">MATLAB中，矩阵是默认的数据类型。它把向量看做1×N或者N×1的矩阵。
</span>

<span style="font-family:微软雅黑; font-size:14pt">%建立了一个行向量，不同元素之间使用空格或者逗号分开都是可以的。
</span>

<span style="font-family:微软雅黑; font-size:14pt">A=[1,2,3]   或者  A=[1 2 3]
</span>

<span style="font-family:微软雅黑; font-size:14pt">%建立一个矩阵，使用分号隔开不同的行。
</span>

<span style="font-family:微软雅黑; font-size:14pt">A=[1,2,3;4,5,6]
</span>

<span style="font-family:微软雅黑; font-size:14pt">%那么，建立一个列向量就好办了。每行一个元素，分号分开即可。当然也可以使用行向量的转置（一个撇号表示转置）。
</span>

<span style="font-family:微软雅黑; font-size:14pt">A=[1;2;3]   或者   A=[1,2,3]'
</span>

<span style="font-family:微软雅黑; font-size:14pt">MATLAB内置了很多特殊的矩阵生成函数，建立特殊矩阵十分方便。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**i)第一组用来生成特殊规则的矩阵。如全零、全一、随机、等步长等形式。**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">**X=zeros(m,n)**   
</span>

<span style="font-family:微软雅黑; font-size:14pt">%生成一个m*n的全0矩阵。同理，**ones(m,n)**生成一个全1矩阵；**eye(m,n)**生成一个单位阵。它们的重要作用在于预先分配矩阵空间，所以，在预知矩阵规模但是不知道矩阵具体数据的情况下，先用这几个函数生成一个矩阵，对提高运算速度十分有用。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**X=rand(m,n)**  
</span>

<span style="font-family:微软雅黑; font-size:14pt">%生成一个平均分布的随机矩阵，数值区间[0,1]。同理，**randn(m,n)**生成一个服从正态分布的随机矩阵。注意，这些所谓的随机实际上都是伪随机。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**v=linspace(a,b,n)**   
</span>

<span style="font-family:微软雅黑; font-size:14pt">%产生线性空间矢量。a和b分别是起点和终点，n是本区间内的点数，默认100个点。同理，**logspace(a,b,n)**产生对数空间矢量。不过它默认点数是50个。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**v=1:0.1:10**   
</span>

<span style="font-family:微软雅黑; font-size:14pt">%产生一个线性的矢量。规格是---起点：步长值：终点
</span>

<span style="font-family:微软雅黑; font-size:14pt">ii)第二组用来在原有矩阵基础上获得一个具有某些特征的矩阵。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**X=diag(v,k)**和**v=diag(X,k)** 
</span>

<span style="font-family:微软雅黑; font-size:14pt">%前者用矢量v中的元素生成一个对角矩阵，k是对角移位因子，默认为0，即主对角。k&gt;0，对角线右移。后者返回矩阵X的对角元素，存在矢量v中。k的意义相同。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**X1=triu(X,k)和X1=tril(X,k)**  
</span>

<span style="font-family:微软雅黑; font-size:14pt"> %分别产生矩阵X的上三角矩阵和下三角矩阵。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**fliplr(X)/flipud(X)/rot90(X)**   
</span>

<span style="font-family:微软雅黑; font-size:14pt">%这都是对矩阵的翻转操作，获得新的矩阵。分别是左右翻转（left-right）、上下翻转（up-down）和逆时针旋转90°操作。
</span>

<span style="font-family:微软雅黑; font-size:14pt">iii)第三组用来生成一些具有理论价值的，往往是以数学家命名的矩阵。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**magic(n)**生成行列相加均为同一个数字的方阵。**pascal(n)**生成帕斯卡尔矩阵。**hilb(n)**生成希尔伯特矩阵。**vander(v)**生成范德蒙德矩阵。等等。
</span>

<span style="font-family:微软雅黑; font-size:14pt">这些矩阵一般都有相应的学术背景，用到的时候，可以用命令help elmat在最后一个栏目中看看有没有自己要找的特殊矩阵，如果有，点进去进一步研究即可。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**2.矩阵的特征信息**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">**size(X)**  %获得矩阵X的行、列数。比如，X是一个3*5的矩阵，p=size(X)返回p=[3 5]
</span>

<span style="font-family:微软雅黑; font-size:14pt">**length()**   %对于矢量，返回的是矢量的长度；对数组，返回的是数组最长的那一个维度的长度。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**ndims()**   %相当于length(size(x))。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**numel()**   %数组中元素的个数。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**isempty()**和**isequal()**等**is***型函数    %测试矩阵是否满足某些条件
</span>

<span style="font-family:微软雅黑; font-size:14pt">**[V,D] = eig(A)**  %矩阵A的特征值D和特征向量V。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**k = rank(A)**   %矩阵A的秩
</span>

<span style="font-family:微软雅黑; font-size:14pt">**b = trace(A)**  %矩阵A的迹，即对角线元素之和
</span>

<span style="font-family:微软雅黑; font-size:14pt">**d = det(X)**    %方阵A的行列式
</span>

<span style="font-family:微软雅黑; font-size:14pt">**Y = inv(X)**   %矩阵X的逆矩阵
</span>

<span style="font-family:微软雅黑; font-size:14pt">**n = norm(X,option)**   %矩阵或者向量的范数，具体使用用到再说
</span>

<span style="font-family:微软雅黑; font-size:14pt">**c = cond(X)**    %矩阵X的条件数
</span>

<span style="font-family:微软雅黑; font-size:14pt">**3.矩阵分解**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">矩阵分解是矩阵论的重要内容。常用的分解形式在MATLAB中都有函数予以实现，并且有些分解考虑了多种情况。常见的如：eig()、qr()、schur()、svd()、chol()、lu()等。具体使用的时候
</span>

<span style="font-family:微软雅黑; font-size:14pt">**4.矩阵运算**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">MATLAB默认的是矩阵运算，所以如果想要按元素依次计算，在原来运算符前加一个.号。比如.*表示按元素相乘。
</span>

<span style="font-family:微软雅黑; font-size:14pt">每一个运算符都有一个对应的函数。如：
</span>

<span style="font-family:微软雅黑; font-size:14pt">**A+B=plus(A,B)、A-B=minus(A,B)**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">**A*B=mtimes(A,B)、A.*B=times(A,B)**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">**A/B=mrdivide(A,B)、A./B=rdivide(A,B)、A\B=mldivide(A,B)、A.\B=ldivide(A,B)**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">**A^B=mpower(A,B)、A.^B=power(A,B)**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">**A'=ctranspose(A)、A.'=transpose(A)**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">其中的前缀m自然是表示matrix的意思。没有m前缀的就是按元素进行的意思。最后那个转置操作，c前缀表示的是按照复数操作进行转置。
</span>

<span style="font-family:微软雅黑; font-size:14pt">此外，还有一些比较常用的运算：
</span>

<span style="font-family:微软雅黑; font-size:14pt">**C=cross(A,B)**  
</span>

<span style="font-family:微软雅黑; font-size:14pt">%矢量叉乘。类似的，C=dot(A,B)  是矢量点乘
**B = prod(A,dim)**   
</span>

<span style="font-family:微软雅黑; font-size:14pt">%数组元素的乘积，默认按列计算。dim=1是列，dim=2是按行。这个概念很重要！！
类似的，B = sum(A,dim)   求数组元素的和。dim意义和以上同。
**expm()**   
</span>

<span style="font-family:微软雅黑; font-size:14pt">%矩阵指数运算。与此类似的**logm(), sqrtm()。**其中，**funm(A,fun)**用来计算矩阵A对通用函数fun的函数值。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**5.矩阵索引**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">选择使用矩阵中的某些元素，就是所谓的矩阵索引了。
</span>

<span style="font-family:微软雅黑; font-size:14pt">A(:,j)   %选取矩阵A的所有行，第j列，同理，A(i,:)是第i行，所有列
</span>

<span style="font-family:微软雅黑; font-size:14pt">A(:,j:k)    %所有行，第j列至第k列（起点和终点均含）
</span>

<span style="font-family:微软雅黑; font-size:14pt">**三、Python的处理**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">Python使用NumPy包完成了对N-维数组的快速便捷操作。使用这个包，需要导入numpy。SciPy包以NumPy包为基础，大大的扩展了numpy的能力。为了使用的方便，scipy包在最外层名字空间中包括了所有的numpy内容，因此只要导入了scipy，不必在单独导入numpy了！但是为了明确哪些是numpy中实现的，哪些是scipy中实现的，本文还是进行了区分。以下默认已经：import numpy as np 以及 impor scipy as sp
</span>

<span style="font-family:微软雅黑; font-size:14pt">下面简要介绍Python和MATLAB处理数学问题的几个不同点。1.MATLAB的基本是矩阵，而numpy的基本类型是多为数组，把matrix看做是array的子类。2.MATLAB的索引从1开始，而numpy从0开始。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**1.建立矩阵**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">a1=np.array([1,2,3],dtype=int)   #建立一个一维数组，数据类型是int。也可以不指定数据类型，使用默认。几乎所有的数组建立函数都可以指定数据类型，即dtype的取值。
</span>

<span style="font-family:微软雅黑; font-size:14pt">a2=np.array([[1,2,3],[2,3,4]])   #建立一个二维数组。此处和MATLAB的二维数组（矩阵）的建立有很大差别。
</span>

<span style="font-family:微软雅黑; font-size:14pt">同样，numpy中也有很多内置的特殊矩阵：
</span>

<span style="font-family:微软雅黑; font-size:14pt">b1=np.zeros((2,3))    #生成一个2行3列的全0矩阵。注意，参数是一个tuple：(2,3)，所以有两个括号。完整的形式为：zeros(shape,dtype=)。相同的结构，有**ones()**建立全1矩阵。**empty()**建立一个空矩阵，使用内存中的随机值来填充这个矩阵。
</span>

<span style="font-family:微软雅黑; font-size:14pt">b2=identity(n)   #建立n*n的单位阵，这只能是一个方阵。
</span>

<span style="font-family:微软雅黑; font-size:14pt">b3=eye(N,M=None,k=0)    #建立一个对角线是1其余值为0的矩阵，用k指定对角线的位置。M默认None。
</span>

<span style="font-family:微软雅黑; font-size:14pt">此外，numpy中还提供了几个like函数，即按照某一个已知的数组的规模（几行几列）建立同样规模的特殊数组。这样的函数有**zeros_like()、empty_like()、ones_like()，**它们的参数均为如此形式：zeros_like(a,dtype=)，其中，a是一个已知的数组。
</span>

<span style="font-family:微软雅黑; font-size:14pt">c1=np.arange(2,3,0.1)   #起点，终点，步长值。含起点值，不含终点值。
</span>

<span style="font-family:微软雅黑; font-size:14pt">c2=np.linspace(1,4,10)    #起点，终点，区间内点数。起点终点均包括在内。同理，有logspace()函数
</span>

<span style="font-family:微软雅黑; font-size:14pt">d1=np.linalg.companion(a)    #伴随矩阵
</span>

<span style="font-family:微软雅黑; font-size:14pt">d2=np.linalg.triu()/tril()   #作用同MATLAB中的同名函数
</span>

<span style="font-family:微软雅黑; font-size:14pt">e1=np.random.rand(3,2)    #产生一个3行2列的随机数组。同一空间下，有randn()/randint()等多个随机函数
</span>

<span style="font-family:微软雅黑; font-size:14pt">fliplr()/flipud()/rot90()    #功能类似MATLAB同名函数。
</span>

<span style="font-family:微软雅黑; font-size:14pt">xx=np.roll(x,2)   #roll()是循环移位函数。此调用表示向右循环移动2位。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**2.数组的特征信息**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">先假设已经存在一个N维数组X了，那么可以得到X的一些属性，这些属性可以在输入X和一个.之后，按tab键查看提示。这里明显看到了Python面向对象的特征。
</span>

<span style="font-family:微软雅黑; font-size:14pt">X.flags    #数组的存储情况信息。
</span>

<span style="font-family:微软雅黑; font-size:14pt">X.shape    #结果是一个tuple，返回本数组的行数、列数、……
</span>

<span style="font-family:微软雅黑; font-size:14pt">X.ndim   #数组的维数，结果是一个数
</span>

<span style="font-family:微软雅黑; font-size:14pt">X.size    #数组中元素的数量
</span>

<span style="font-family:微软雅黑; font-size:14pt">X.itemsize    #数组中的数据项的所占内存空间大小
</span>

<span style="font-family:微软雅黑; font-size:14pt">X.dtype    #数据类型
</span>

<span style="font-family:微软雅黑; font-size:14pt">X.T   #如果X是矩阵，发挥的是X的转置矩阵
</span>

<span style="font-family:微软雅黑; font-size:14pt">X.trace()    #计算X的迹
</span>

<span style="font-family:微软雅黑; font-size:14pt">np.linalg.det(a)   #返回的是矩阵a的行列式
</span>

<span style="font-family:微软雅黑; font-size:14pt">np.linalg.norm(a,ord=None)    #计算矩阵a的范数
</span>

<span style="font-family:微软雅黑; font-size:14pt">np.linalg.eig(a)    #矩阵a的特征值和特征向量
</span>

<span style="font-family:微软雅黑; font-size:14pt">np.linalg.cond(a,p=None)    #矩阵a的条件数
</span>

<span style="font-family:微软雅黑; font-size:14pt">np.linalg.inv(a)    #矩阵a的逆矩阵
</span>

<span style="font-family:微软雅黑; font-size:14pt">**3.矩阵分解**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">常见的矩阵分解函数，numpy.linalg均已经提供。比如cholesky()/qr()/svd()/lu()/schur()等。某些算法为了方便计算或者针对不同的特殊情况，还给出了多种调用形式，以便得到最佳结果。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**4.矩阵运算**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">np.dot(a,b)用来计算数组的点积；vdot(a,b)专门计算矢量的点积，和dot()的区别在于对complex数据类型的处理不一样；innner(a,b)用来计算内积；outer(a,b)计算外积。
</span>

<span style="font-family:微软雅黑; font-size:14pt">专门处理矩阵的数学函数在numpy的子包linalg中定义。比如np.linalg.logm(A)计算矩阵A的对数。可见，这个处理和MATLAB是类似的，使用一个m后缀表示是矩阵的运算。在这个空间内可以使用的有cosm()/sinm()/signm()/sqrtm()等。其中常规exp()对应有三种矩阵形式：expm()使用Pade近似算法、expm2()使用特征值分析算法、expm3()使用泰勒级数算法。在numpy中，也有一个计算矩阵的函数：funm(A,func)。
</span>

<span style="font-family:微软雅黑; font-size:14pt">**5.索引**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">numpy中的数组索引形式和Python是一致的。如：
</span>

<span style="font-family:微软雅黑; font-size:14pt">x=np.arange(10)
</span>

<span style="font-family:微软雅黑; font-size:14pt">print x[2]    #单个元素，从前往后正向索引。注意下标是从0开始的。
</span>

<span style="font-family:微软雅黑; font-size:14pt">print x[-2]    #从后往前索引。最后一个元素的下标是-1
</span>

<span style="font-family:微软雅黑; font-size:14pt">print x[2:5]    #多个元素，左闭右开，默认步长值是1
</span>

<span style="font-family:微软雅黑; font-size:14pt">print x[:-7]    #多个元素，从后向前，制定了结束的位置，使用默认步长值
</span>

<span style="font-family:微软雅黑; font-size:14pt">print x[1:7:2]   #指定步长值
</span>

<span style="font-family:微软雅黑; font-size:14pt">x.shape=(2,5)    #x的**shape**属性被重新赋值，要求就是元素个数不变。2*5=10
</span>

<span style="font-family:微软雅黑; font-size:14pt">print x[1,3]    #二维数组索引单个元素，第2行第4列的那个元素
</span>

<span style="font-family:微软雅黑; font-size:14pt">print x[0]   #第一行所有的元素
</span>

<span style="font-family:微软雅黑; font-size:14pt">y=np.arange(35).reshape(5,7)    #**reshape()**函数用于改变数组的维度
</span>

<span style="font-family:微软雅黑; font-size:14pt">print y[1:5:2,::2]    #选择二维数组中的某些符合条件的元素
</span>

<span style="font-family:微软雅黑; font-size:14pt">-------------------------------------------------分割线-------------------------------------------------
</span>

<span style="font-family:微软雅黑; font-size:14pt">作为第一篇正式的介绍技术操作的文章，终于写完了，很费劲。恰恰就是在这个费劲的过程中，让我能更好的认识两者的区别和联系，同时梳理了展开的思路，摸索出了进一步学习的方法。
</span>

<span style="font-family:微软雅黑; font-size:14pt">我们可以看到，MATLAB中实现了的函数或者功能，在numpy中都有了对应，并且有些实现的更好。当然，这只是冰山一角。如果你不愿意通读文档（很枯燥，谁也不愿意干！）也应该有理由相信，Python有能胜任工作的实现已经存在。后面的内容，将不再这样列出各种函数和功能，而是以某一个实际问题为核心，进行专题式的研究。至于全方位的了解，请自己查阅文档。有个经验之谈，就是，应该充分的利用文档中的【see also】功能，依此追踪下去，必然会获得关于某主题的全方位的认识。比如，在查阅ones()的时候，MATLAB的【see also】就给出了complex|eye|true|zeros四个链接。这就说明，这几个函数其实是有关联的，点进去进行简单的学习，找到共性，那么，可能很多人都遇到过的最大的困惑——那么多函数怎么记住呀？——就已经解决了。因为，我们不需要记住所有的函数，我们只需要记住有那么回事，只需要记住一个类似的函数，就可以很轻易的在用的时候顺藤摸瓜找出需要的函数。
</span>

<span style="font-family:微软雅黑; font-size:14pt">下面简单的给出MATLAB和Python的自查自学方法吧！
</span>

<span style="font-family:微软雅黑; font-size:14pt">**1.MATLAB**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">help 函数名  
</span>

<span style="font-family:微软雅黑; font-size:14pt">%在控制台给出某函数或者主题的帮助信息
</span>

<span style="font-family:微软雅黑; font-size:14pt">doc  函数名 
</span>

<span style="font-family:微软雅黑; font-size:14pt">%在帮助浏览器中给出帮助信息，这个界面更友好。在help browser中既有MATLAB整个产品的浏览左窗口，也有一个搜索框。同时还有大量存在的超链接。就一个感兴趣的主题，点下去，全面学习。不过要记住:别分神哦~~点到最后都忘了自己究竟要做什么！
</span>

<span style="font-family:微软雅黑; font-size:14pt">lookfor 关键词   
</span>

<span style="font-family:微软雅黑; font-size:14pt">%这是一个模糊寻找，含有关键词的词条入口都会给出来
</span>

<span style="font-family:微软雅黑; font-size:14pt">**2.Python**
		</span>

<span style="font-family:微软雅黑; font-size:14pt">help(np.array)    #查看关于array的帮助信息
</span>

<span style="font-family:微软雅黑; font-size:14pt">help(np.add)  #查看关于add的帮助信息
</span>