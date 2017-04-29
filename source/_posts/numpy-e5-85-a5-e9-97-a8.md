---
title: Numpy入门
tags:
  - numpy
  - Python
  - 科学计算
id: 1034
categories:
  - Python
date: 2016-05-09 19:00:33
---

# 前言

很久都没有用过numpy来做科学计算了，现在Python的机器学习这么火，而机器学习很多代码都需要用numpy、scipy来构建，所以我现在开始进行一些温习吧

# ndarray对象

## 创建

我们需要创建数组并且对其进行操作。

我们可以通过给array函数传递python的序列对象创建数组，如果传递的是多层嵌套序列，将创建多维数组。
<pre class="lang:python decode:true">a = numpy.array([1,2,3,4])# the list can be replaced with tuple
b = numpy.array((1,2,3,4))
c = numpy.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])</pre>

 数组的类型可以通过dtype来获取：
<pre class="lang:python decode:true">&gt;&gt;&gt; print c.dtype
int64</pre>

 数组的大小可以通过shape获得或者修改：
<pre class="lang:python decode:true">print a.shape,c.shape
(4,) (3, 4)</pre>

这里的大小和列表的大小保持一致。而当变更shape的时候，例如(3,4)-&gt;(4,3)的时候，并不是对数组进行转置，而只是改变每个轴的大小，**数组元素在内存中的位置并不发生改变**。
<pre class="lang:python decode:true">c.shape = 4,3
print c

[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]</pre>

 当某个轴为-1的时候，蒋根据数组元素的个数自动计算此轴的长度，也就是说，如果你变更的shape是2,-1那么其就会自动计算为2,6
<pre class="lang:python decode:true">c.shape = 2,-1
print c

[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]]</pre>

 使用数组的`reshape`的方法，可以创建一个变更尺寸的新数组，而原数组的shape保持不变。但是**新数组和原数组仍然共享数据存储内存区域**，所以修改任意一个数组的元素都会**变更**另一个数组的内容。
<pre class="lang:default decode:true">d = c.reshape((2,-1))
print d

[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]]</pre>

 数组的元素可以通过`dtype`属性获得，上面例子中的参数序列的元素都是`int`，因此创建的数组的元素类型也是整数，你可以通过指定`dtype`参数来指定元素类型。
<pre class="lang:default decode:true">e = numpy.array([1,2,3,4],dtype=numpy.float)</pre>

 numpy中的数据类型转换，不能直接改原数据的`dtype`。只能用函数`astype()`。

而python会自带一些函数来创建数组，可以不需要使用python对象转换为array对象。

### arange

类似于`range`，通过指定开始、结果以及步长来创建一个一维数组。

### linspace

通过开始设置开始、终值和元素个数来创建等差一维数组，可以通过设置`endpoint`来指定是否包括终值。
<pre class="lang:python decode:true">numpy.linspace(0,1,12)
array([ 0\.        ,  0.09090909,  0.18181818,  0.27272727,  0.36363636,
        0.45454545,  0.54545455,  0.63636364,  0.72727273,  0.81818182,
        0.90909091,  1\.        ])</pre>

### logspace

和`linspace`一样，不过创建等比数列。下面这个例子产生1（10^0）到100（10^2），有20个元素的等比数列。
<pre class="lang:python decode:true">numpy.logspace(0,2,20)
array([   1\.        ,    1.27427499,    1.62377674,    2.06913808,
          2.6366509 ,    3.35981829,    4.2813324 ,    5.45559478,
          6.95192796,    8.8586679 ,   11.28837892,   14.38449888,
         18.32980711,   23.35721469,   29.76351442,   37.92690191,
         48.32930239,   61.58482111,   78.47599704,  100\.        ])</pre>

### 其他

此外使用`frombuffer`，`fromstring`，`fromfile`等函数可以从字节中创建数组

下面以`fromstring`<!--more-->为例子，在Python之中，字符串实质上是字节序列，每个字符占一个字节，如果从字符串中创建一个64bit的整数数组的话，所得到的数组正好是字符串中每个ASCII编码：
<pre class="lang:python decode:true">&gt;&gt;&gt; s="abcdefgh"
&gt;&gt;&gt; numpy.fromstring(s,dtype=numpy.int64)
array([7523094288207667809])
&gt;&gt;&gt; numpy.fromstring(s,dtype=numpy.int8)
array([ 97,  98,  99, 100, 101, 102, 103, 104], dtype=int8)</pre>

 如果从字符串中创建一个16bit的整数数组，那么相邻的两个字节就表示一个证书，把字节98和97当做一个16bit的证书，那么他的值就是98*256+97=25185。可以看出内存中是以**低位字节在前**（little endian）的方式保存数据的。

当然，我们使用C语言的二进制写了一组`double类`型的数值的时候，我们读文件的时候，需要通过`fromstring`函数将其转换为`float64`类型的数组。

### 函数创建数组

fromfunction函数的第一个参数为每个数组元素的函数，第二个参数为数组的大小（其支持多维数组），所以第二个数组必须为一个元祖。

一维：
<pre class="lang:python decode:true">def func(i):
    return i%4+1

print numpy.fromfunction(func,(10,))

[ 1\.  2\.  3\.  4\.  1\.  2\.  3\.  4\.  1\.  2.]</pre>

 二维：
<pre class="lang:python decode:true">def func2D(i,j):
    return (i+1)*(j+1)

print numpy.fromfunction(func2D,(9,9))

[[  1\.   2\.   3\.   4\.   5\.   6\.   7\.   8\.   9.]
 [  2\.   4\.   6\.   8\.  10\.  12\.  14\.  16\.  18.]
 [  3\.   6\.   9\.  12\.  15\.  18\.  21\.  24\.  27.]
 [  4\.   8\.  12\.  16\.  20\.  24\.  28\.  32\.  36.]
 [  5\.  10\.  15\.  20\.  25\.  30\.  35\.  40\.  45.]
 [  6\.  12\.  18\.  24\.  30\.  36\.  42\.  48\.  54.]
 [  7\.  14\.  21\.  28\.  35\.  42\.  49\.  56\.  63.]
 [  8\.  16\.  24\.  32\.  40\.  48\.  56\.  64\.  72.]
 [  9\.  18\.  27\.  36\.  45\.  54\.  63\.  72\.  81.]]</pre>

## 存取元素

数组元素的存取方式和Python标准的标准相同：

### 使用整数下标获取数组中某个元素
<pre class="lang:default highlight:0 decode:true">a[5]</pre>

### 获取数组的一个切片，左半闭集
<pre class="lang:python decode:true">a[3:5]</pre>

省略开始下标，表示从a[0]开始
<pre class="lang:python decode:true">a[:5]</pre>

表示数组从后向前数
<pre class="lang:python decode:true">a[:-1]</pre>

范围中的第三个参数为步长，隔一个参数取一个元素，步长为负的时候，开始下表必须大于结束下标
<pre class="lang:python decode:true">a[1:-1:2]</pre>

和Python序列不同，通过下标范围获取的新数组仍然和原始数组**共享**一块数据空间，修改的方式和上面一致。

### 使用整数序列

当使用整数序列对数组元素进行存储的时候，将使用整数序列的每个元素作为下标，整数序列可以是列表或者数组，**新数组和原始数组不共享数据空间**。
<pre class="lang:python decode:true">&gt;&gt;&gt; x = numpy.arange(10,1,-1)
&gt;&gt;&gt; x
array([10,  9,  8,  7,  6,  5,  4,  3,  2])
&gt;&gt;&gt; x[[3,3,1,8]]
array([7, 7, 9, 2])
&gt;&gt;&gt; b = x[numpy.array([3,3,-3,8])]
&gt;&gt;&gt; b
array([7, 7, 4, 2])
&gt;&gt;&gt; x
array([10,  9,  8,  7,  6,  5,  4,  3,  2])
&gt;&gt;&gt; x[[3,5,1]]= -1,-2,-3
&gt;&gt;&gt; x
array([10, -3,  8, -1,  6, -2,  4,  3,  2])
&gt;&gt;&gt; 
</pre>

 在上面的第三个例子之中，获取x中下标为3,3,1,8的4个元素，组成一个新的数组。

### bool数组

当使用bool数组作为下标取数组x中的元素时，将收集数组x中所有在数组b中对应下标为`True`的元素，**使用bool数组作为下标获得的数组不和原始数组共享数据空间**。
<pre class="lang:default decode:true">a = numpy.arange(5,0,-1)

print a[numpy.array([True,False,True,False,False])] 

[5 3]</pre>

 这里是bool数组，bool数组的下标为0,2的元素为`True`，因此获取a中下标为0,2的元素
<pre class="lang:python decode:true">print a[[True,False,True,False,False]]

[4 5 4 5 5]</pre>

 上面是bool列表，把`True`当做1，`False`当做0，按照整数序列方式获取a中的元素。

同样的`bool`数组也可以用来修改元素。

这里说明的是，bool数组一般不是手工产生，而是使用`bool`运算的`ufunc`函数产生。
<pre class="lang:default decode:true">&gt;&gt;&gt; x = numpy.random.rand(10)
&gt;&gt;&gt; x
array([ 0.95269729,  0.20907106,  0.08637803,  0.27252325,  0.57886525,
        0.759558  ,  0.15980624,  0.10516475,  0.83847977,  0.38377675])
&gt;&gt;&gt; x&gt;0.5
array([ True, False, False, False,  True,  True, False, False,  True, False], dtype=bool)
&gt;&gt;&gt; x[x&gt;0.5]
array([ 0.95269729,  0.57886525,  0.759558  ,  0.83847977])
</pre>

 `x&gt;0.5`会将数组中的每个元素和0.5进行比较，得到一个bool数组，`True`表示x中对应的值大于0.5。

而`x&gt;0.5`返回的bool数组收集x中的元素，其返回所有大于0.5的元素的数组。

## 多维数组

多维数组存取和一维数组类似，因为其具有多个轴，因此它的下标需要多个值来表示，Numpy采用元祖（`tuple`）作为数组的下标。

需要指出的是元祖是**不需要**圆括号的。例如`x,y=y,x`就是用元祖来交换变量值的一个例子。

使用数组切片语法访问多维数组的元素。那么可以使用下面的语句来创建这个数组。
<pre class="lang:python decode:true">a = numpy.arange(0,60,10).reshape(-1,1) + numpy.arange(0,6)</pre>

 这个语句就会创建下面这样的数组：
<pre class="lang:default decode:true">[[ 0  1  2  3  4  5]
 [10 11 12 13 14 15]
 [20 21 22 23 24 25]
 [30 31 32 33 34 35]
 [40 41 42 43 44 45]
 [50 51 52 53 54 55]]</pre>

 首先上面的加数创建了一个竖列的数组，而加上了一个横列的数组就变成了这样了。

取多维数组的方式和取一维原理类似，都是可以通过索引值取某一列或行切片取某一列或一行，你可以想象成一个横竖线所交汇或者围成矩形的位置就是所取的数组。

`a[(0,1,2,3,4)(1,2,3,4,5)]`:用于存取数组下标和仍然是一个有两个元素的元祖，元祖中的每个元素都是整数序列，分别对应于数组的第0轴和第1轴.从两个序列的对应位置取出两个证书组成下标：`a[0,1],a[1,2]...`

`a[3:,[0,2,5]]`：下标中的第0轴是一个范围，其选取第三行之后的所有行，他选取第0,2,5三列。

在进行存取的时候也是可以使用Bool数组来存储的。

## 结构数组

在C语言之中可以通过`struct`关键字定义结构类型，结构中的字段占据连续的内存空间，每个结构体占用的内存大小都相同，因此可以很容易的定义结构数组。只要`numpy`中的结构定义和C语言中的定义相同，`Numpy`就可以很方便的读取C语言的结构数组的二进制数据，转换为`numpy`的结构数组。
<pre class="lang:python decode:true">personType = numpy.dtype({
    'names':['name','age','weight'],
    'formats':['S32','i','f']
    })

kido = numpy.array([("zhang",32,75.5),("wang",24,65.2)],dtype=personType)</pre>

 在创建对象`personType`，其通过字典参数描述结构类型的各个字段，字典中有两个关键字，names，formats，每个关键字对应的值都是一个列表。`names`定义结构中的每个字段名，`formats`则是定义每个字段的类型。这里我们援引`numpy`的官方指南，给出`formats`的字符串所代表的意思：

*   'b'boolean 布尔值
*   'i'(signed) integer 有符号的整数
*   'u'unsigned integer 无符号的整数
*   'f'floating-point 浮点数
*   'c'complex-floating point 复数浮点数
*   'O'(Python) objects Python对象
*   'S', 'a'(byte-)string X字节的字符串
*   'U'Unicode unicode对象
*   'V'raw data (void) 空

然后我们调用`array`创建数组，通过关键字参数`dtype`指定所处案件数组的元素类型。而在`struct`之中，我们常常用以下符号来描述字段值的字节顺序：

*   | 忽视字节顺序
*   &lt; 低位字节在前
*   &gt; 高位字节在前

结构数组的存取方式和一般数组相同，通过索引或者字段可以取得元素，此时元素是一个结构，这里可以像字典一样通过字符串下标取得或者修改对应的字段值。
<pre class="lang:default decode:true">a[0]["name"]</pre>

我们不但可以获得结构元素的某个字段，还可以直接获得结构数组的字段，其返回的是原始数组的师徒，因此可以通过修改a[0]改变a[0]["age"]。
<pre class="lang:python decode:true">b = a[:]["age"]
b[0] = 40</pre>

通过调用`a.tostring`或者`a.tofile`的方法，可以直接输出数组a的二进制形式，并且可以利用下面的C代码提取处文件数据。
<pre class="lang:c decode:true"># include &lt;stdio.h&gt;

struct person{
    char name[32];
    int age;
    float weight;
};

struct person p[2];

int main ()
{
    FILE *fp;
    int i;
    fp = fopen("test.bin","rb");
    fread(p,sizeof(struct person),2,fp);
    fclose(fp);
    for (int i=0;i&lt;2;i++){
        printf("%s %d %f\n",p[i].name,p[i].age,p[i].weight);
    }
    return 0;
}
</pre>

### 内存对齐

C语言结构为了寻址方便，会自动的添加一些用于填充的字节，这个被称为内存对齐。由于内存对齐问题，在name和age中间会填充两个字节，最终的结构体大小不变。因此为了解决numpy所配置的内存大小不符合C语言对齐规范，可以在创建`dtype`对象的时候，传递参数`align = True`，这样内存对齐问题就能够解决了。

结构类型之中也可以包括其他的结构类型，下面的语句创建一个有一个字段的f1的结构，f1的值是另一个结构，他有字段f2，其类型为16bit整数。
<pre class="lang:python decode:true">numpy.dtype([('f1',[('f2',numpy.int16)])])</pre>

# ufunc运算

ufunc是universal function的缩写，其能够对数组每个元素进行操作的函数，numpy内置的许多`ufunc`函数都是在C语言的层面上实现的，所以他们的计算速度非常的快。
<pre class="lang:python decode:true">&gt;&gt;&gt; import numpy
&gt;&gt;&gt; x = numpy.linspace(0,2*numpy.pi,10)
&gt;&gt;&gt; y = numpy.sin(x)
&gt;&gt;&gt; y
array([  0.00000000e+00,   6.42787610e-01,   9.84807753e-01,
         8.66025404e-01,   3.42020143e-01,  -3.42020143e-01,
        -8.66025404e-01,  -9.84807753e-01,  -6.42787610e-01,
        -2.44929360e-16])
&gt;&gt;&gt; 
</pre>

 先用`linspace`产生一个从0到$$2\pi$$的等距离的10个数，然后将其传递给`sin`函数，由于其是一个`ufunc`函数，因此他对x的每个元素求正弦值并且返回结果，赋值给y，计算后x值没有改变，而是新创建了一个数组，如果我们希望覆盖的话，可以把被覆盖的数组作为第二个参数传递给`ufunc`函数。
<pre class="lang:default decode:true">t = numpy.(x,x)</pre>

 那么我们来比较一下`numpy.sin`和Python标准库`math.sin`的计算速度：
<pre class="lang:default decode:true">import numpy
import time
import math

x = [i * 0.001 for i in xrange(1000000)]
start = time.clock()
for i,t in enumerate(x):
    x[i] = math.sin(t)
print "# math.sin : ",time.clock()-start

# This is numpy
x = [i * 0.001 for i in xrange(1000000)]
x = numpy.array(x)
start = time.clock()
numpy.sin(x,x)
print "# numpy.sin : ",time.clock()-start</pre>

 最终的结果numpy比标准的math库快太多了。
<pre class="lang:python decode:true">/usr/bin/python2.7 /home/exbot/PycharmProjects/scienceCaculate/numpyExample.py
# math.sin :  0.251233
# numpy.sin :  0.040183</pre>

这得利于`numpy.sin`在C语言级别的循环运算，`numpy.sin`同样也支持单个数值求正弦，但是比`math.sin`慢多了：

代码如下
<pre class="lang:python decode:true">__author__ = 'exbot'
import numpy
import time
import math

x = [i * 0.001 for i in xrange(1000000)]
start = time.clock()
for i,t in enumerate(x):
    x[i] = math.sin(t)
print "# math.sin : ",time.clock()-start

# This is numpy
x = [i * 0.001 for i in xrange(1000000)]
for i,t in enumerate(x):
    x[i] = numpy.sin(t)
print "# numpy.sin : ",time.clock()-start</pre>

结果：
<pre class="lang:default decode:true"># math.sin :  0.242994
# numpy.sin :  2.011833</pre>

 注意的是`numpy.sin`的计算速度只有`math.sin`的1/10,这是因为`numpy.sin`支持数组和单个计算，其C语言内部实现比math.sin复杂很多，如果我们在同样的Python级别进行循环的话，就会看出差异了。

另外，`numpy.sin`返回的类型是`numpy.float64`而`math.sin`则是返回标准的`float`型。

`numpy`之中还有各式各样的函数来提供计算，除了`sin`这种单输入函数外，还有其他的，诸如`add`这种函数，`add`会把两个等shape的array每个元素对应想家，和`sin`一样，如果你要覆盖的话，指定第三个参数为覆盖的数列就可以了。
<table border="0" cellspacing="0"><colgroup span="2" width="85"></colgroup><tbody><tr><td style="text-align: center;" align="left" height="17">+</td><td style="text-align: center;" align="left">加法</td></tr><tr><td style="text-align: center;" align="left" height="17">-</td><td style="text-align: center;" align="left">减法</td></tr><tr><td style="text-align: center;" align="left" height="17">*</td><td style="text-align: center;" align="left">乘法</td></tr><tr><td style="text-align: center;" align="left" height="20">/</td><td style="text-align: center;" align="left">根据是否激活future_.division分为整数的除法和浮点数的除法</td></tr><tr><td style="text-align: center;" align="left" height="17">//</td><td style="text-align: center;" align="left">总是对除法的商求整</td></tr><tr><td style="text-align: center;" align="left" height="17">**</td><td style="text-align: center;" align="left">幂函数</td></tr><tr><td style="text-align: center;" align="left" height="17">%</td><td style="text-align: center;" align="left">取余</td></tr></tbody></table>

根据Python的重载规则，`add`可以简写为a+b。

通过对于`ufunc`的调用，可以实现各种算式的数值计算，而有时候这种算式不容易编写，而针对Python的计算函数却很容易使用Python实现，这个时候就可以用`fromfunc`函数将一个计算单元的函数转换成`ufunc`函数来对数组进行计算了。

下面我们演示一个分段函数，也就是三角波。

[![figure_1](/wp-content/uploads/2016/05/figure_1.png)](/wp-content/uploads/2016/05/figure_1.png)

我们很容易就给出了三角波的函数：
<pre class="lang:python decode:true">def triangleWave(x,c,c0,hc):
    x = x-int(x)
    if x&gt;c :
        r = 0.0
    elif x&lt;c0:
        r = x/c0*hc
    else:
        r = (c-x)/(c-c0)*hc
    return r</pre>

 显然triangleWave只能计算单个数值，而无法对数组进行处理，我们可以使用下面的方法先使用列表包容，计算出一个list，然后使用array函数把列表转换为数组：
<pre class="lang:python decode:true">x = numpy.linspace(0,2,1000)
y = numpy.array([triangleWave(t,0.6,0.4,1.0) for t in x])</pre>

 这种做法每次都需要使用列表包容来调用函数，对于多维数组而言是非常麻烦的，我们就可以使用frompyfunc来解决这个问题。
<pre class="lang:python decode:true">triangleWaveUfunc = numpy.frompyfunc(lambda x:triangleWave(x,0.6,0.4,1.0),1,1)
y = triangleWaveUfunc(x)</pre>

 `frompyfunc`的调用格式为`frompyfunc(func,nin,nout)`，其中`func`是计算单个元素的函数，`nin`是输入参数的个数，`nout`是输出的个数，这里由于c,c0,hc都是固定值，所以我们用一个`lambda`函数进行包装。不过还有一种方法：
<pre class="lang:python decode:true">def triangleFunc(c,c0,hc):
    def trifunc(x):
        x = x-int(x)
        if x&gt;=c:
            r = 0.0
        elif x&lt;c0:
            r = x/c0*hc
        else:
            r = (c-x)/(c-c0)*hc
        return r
    return numpy.frompyfunc(trifunc,1,1)

x= numpy.linspace(0,2,1000)
alternativeY = triangleFunc(0.6,0.4,1.0)(x)</pre>

 我们通过函数`triangleFunc`包装三角波的三个参数，在其内部定义一个三角波函数`trifunc`。`trifunc`函数会在调用的时候采用`triangleFunc`的参数进行计算，最后其返回一个`frompyfunc`的转换结果。

需要主意的是用`frompyfunc`的得到的函数计算出的数组元素为`object`，所以还需要再次<span class="lang:python decode:true  crayon-inline ">y2.astype(numpy.float64)</span> 将其转换为双精度浮点数。

## 广播

当我们使用`ufunc`函数队两个数组进行计算的时候，`ufunc`会对这两个数组对应的元素进行计算，因此它要求这两个数组具有相同的大小，若两个数组的大小不同的话，会进行下面的广播处理：

1.  让所有的输入数组都想其中shape最长的看齐，shape中不足的部分通过加1补齐
2.  输出数组的shape是输入数组shape各轴上的最大值
3.  如果输入数组的某个轴和输出数组对应轴的长度相同或者其长度为1时，这个数组能够用来计算，否则出错
4.  当输入数组的某个轴长度为1时，沿着此轴运算时都能够用此轴上的**第一组值**

那么还是给出栗子把：

先创建一个二维的数组a，其`shape`为6,1，创建一个一维数组b，其`shape`为5, ，计算a和b的和，得到一个加法表，其相当于计算`a`,`b`中所有元素的和，得到一个`shape`为6,5的数组：
<pre class="lang:python decode:true">&gt;&gt;&gt; a = numpy.arange(0,60,10).reshape(-1,1)
&gt;&gt;&gt; b = numpy.arange(0,5)
&gt;&gt;&gt; c = a+b
&gt;&gt;&gt; a 
array([[ 0],
       [10],
       [20],
       [30],
       [40],
       [50]])
&gt;&gt;&gt; b
array([0, 1, 2, 3, 4])
&gt;&gt;&gt; c
array([[ 0,  1,  2,  3,  4],
       [10, 11, 12, 13, 14],
       [20, 21, 22, 23, 24],
       [30, 31, 32, 33, 34],
       [40, 41, 42, 43, 44],
       [50, 51, 52, 53, 54]])
&gt;&gt;&gt; 
</pre>

 由于a，b的`shape`长度（也就是`ndim`属性）不同，根据规则1，需要让b的shape向a对齐，于是将b的`shape`前面加1，补齐为（1,5）.相当于做了以下计算：
<pre class="lang:python decode:true">&gt;&gt;&gt; b.shape = 1,5
&gt;&gt;&gt; b
array([[0, 1, 2, 3, 4]])
</pre>

 这样加法运算的两个输入数组的`shape`分别为(6,1)和(1,5)，根据规则2，输出数组的各个轴的长度为输入数组各个轴上的长度的最大值，可知输出数组`shape`为(6,5)。

由于b的第0轴上的长度为1，而a的第0轴的长度为6，因此为了让它们在第0轴上能够相加，所以需要将b在第0轴的长度扩展为6，这相当于：
<pre class="lang:default decode:true">&gt;&gt;&gt; b.shape = 1,5
&gt;&gt;&gt; b = b.repeat(6,axis=0)
&gt;&gt;&gt; b
array([[0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4]])
</pre>

 由于a的第1轴的长度为1，而b的第1轴长度为5，因此为了让它们在第1轴上能够相加，需要将a在第1轴上的长度扩展为5，这相当于：
<pre class="lang:python decode:true">&gt;&gt;&gt; a = a.repeat(5,axis=1)
&gt;&gt;&gt; a
array([[ 0,  0,  0,  0,  0],
       [10, 10, 10, 10, 10],
       [20, 20, 20, 20, 20],
       [30, 30, 30, 30, 30],
       [40, 40, 40, 40, 40],
       [50, 50, 50, 50, 50]])
</pre>

 经过上述处理之后，a和b就可以按照对应元素进行相加运算了。

当然，在numpy内部不会真正的将长度为1的轴用`repeat`函数进行扩展，如果这样做的话就太浪费空间了。

由于这种广播计算很常用，因此numpy提供了一个快速产生如上面a,b数组的方法：`ogrid`对象。
<pre class="lang:python decode:true">&gt;&gt;&gt; x,y = numpy.ogrid[0:5,0:5]
&gt;&gt;&gt; x
array([[0],
       [1],
       [2],
       [3],
       [4]])
&gt;&gt;&gt; y
array([[0, 1, 2, 3, 4]])
</pre>

 ogrid是一个非常有趣的对象，它像一个多维数组一样，用切片组元作为下标作为下标进行存取，返回的是一组可以用来广播计算的数组。其切片下标有两种形式：

*   开始值:结束值:步长（和`numpy.arange`类似）
*   开始值:结束值:长度j，当第三个参数为_虚数_的时候，其会返回的数组的长度（和`numpy.linspace`类似）

## orgid为什么不是函数

利用`ogrid`的返回值，我能很容易计算x,y网格面上各点的值，或者x,y,z网格体上各点的值。上面是回执三维曲面$$xe^{x^{2}-y^{2}}$$的程序：
<pre class="lang:python decode:true">import numpy
from mayavi.mlab import *

x,y = numpy.ogrid[-2:2:20j,-2:2:20j]
z = x*numpy.exp(-x**2-y**2)
p1 = surf(x,y,z,warp_scale="auto")</pre>

## ufunc的方法

`ufunc`还有其他的用法，这种方法只对两个输入一个输出的ufunc函数有效，其他的ufunc对象调用这些方法会抛出`ValueError`异常。

`reduce`方法和Python的`reduce`函数类似，他会沿着`axis`轴对`array`进行操作，相当于将&lt;op&gt;运算符插入到沿axis轴的所有子数组或者元素之中。
<pre class="lang:python decode:true">&lt;op&gt;.reduce(array=,axis=0,dtype=None)</pre>

 例如：
<pre class="lang:python decode:true">&gt;&gt;&gt; numpy.add.reduce([1,2,3])
6
</pre>

还有针对多维的`reduce`：
<pre class="lang:python decode:true">&gt;&gt;&gt; numpy.add.reduce([[1,2,3],[4,5,6]],axis=1)
array([ 6, 15])</pre>

`accumulate`方法和`reduce`方法类似，只是它返回的数组和输入的数组的shape相同，保存所有的中间计算数组。
<pre class="lang:python decode:true ">&gt;&gt;&gt; numpy.add.accumulate([1,2,3])
array([1, 3, 6])
&gt;&gt;&gt; numpy.add.accumulate([[1,2,3],[4,5,6]],axis=1)
array([[ 1,  3,  6],
       [ 4,  9, 15]])</pre>

 `reduceat`方法计算多组`reduce`的结果，通过`indices`参数指定一系列`reduce`的起始和终了位置：
<pre class="lang:python decode:true ">&gt;&gt;&gt; a = numpy.array([1,2,3,4])
&gt;&gt;&gt; numpy.add.reduceat(a,indices=[0,1,0,2,0,3,0])
array([ 1,  2,  3,  3,  6,  4, 10])
</pre>

 对于indices中的每个元素会调用reduce计算出一个值来，因此最终的计算结果的长度和indices的长度相同。出了最后一个元素以外，都按照下列计算得出：
<pre class="lang:python decode:true ">if indices[i]&lt;indices[i+1] :
    result[i] = numpy.reduce(a[indices[i]]:indices[i+1])
else:
    result[i] = a[indices[i]]</pre>

 而对于最后一个元素如下计算：
<pre class="lang:python decode:true ">numpy.reduce(a[indices[-1]:])</pre>

 因此下面的例子中，结果的每个元素如下计算而得
<pre class="lang:default decode:true ">1 : a[0] = 1
2 : a[1] = 2
3 : a[0] + a[1] = 1 + 2
3 : a[2] = 3
6 : a[0] + a[1] + a[2] = 1 + 2 + 3 = 6
4 : a[3] = 4
10: a[0] + a[1] + a[2] + a[3] = 1 + 2 + 3 + 4 = 10</pre>

 可以看出<span class="lang:python decode:true  crayon-inline ">result[::2]</span> 和a相等，而<span class="lang:python decode:true  crayon-inline ">result[1::2]</span> 和`numpy.add.accumulate(a)`相等。

`outer`方法，`&lt;op&gt;.outer(a,b)`方法的计算等同于如下程序：
<pre class="lang:python decode:true ">a.shape += (1,)*b.ndim
&lt;op&gt;(a,b)
a = a.squeeze()</pre>

 其中`squeeze`的功能是剔除数组a中长度为1的轴。
<pre class="lang:python decode:true ">&gt;&gt;&gt; numpy.multiply.outer([1,2,3,4,5],[2,3,4])
array([[ 2,  3,  4],
       [ 4,  6,  8],
       [ 6,  9, 12],
       [ 8, 12, 16],
       [10, 15, 20]])
</pre>

 可以看出通过`outer`的方法计算的结果是乘法表。乘法表最终是通过广播的方法计算出来的。

# 矩阵运算

NumPy和Matlab不一样，对于多维数组的运算，缺省状况下并不使用矩阵运算，如果你希望对数组进行矩阵运算的话，可以调用相应的函数。
> matrix对象
> 
> numpy提供了`matrix`类，使用`matrix`类创建的是矩阵对象，它们的加法乘除运算缺省用的是矩阵方式计算，因此用法和matlab十分类似。由于NumPy中同事存在`ndarray`和`matrix`对象，因此用户很容易将两者弄混。这和Python的“显式优于隐式”的原则，因此并不推荐在较为复杂的程序之中使用`matrix`。
> <pre class="lang:python decode:true ">&gt;&gt;&gt; a = numpy.matrix([[1,2,3],[5,5,6],[7,9,9]])> 
> &gt;&gt;&gt; a*a**-1> 
> matrix([[  1.00000000e+00,   0.00000000e+00,   0.00000000e+00],> 
>         [  4.44089210e-16,   1.00000000e+00,   4.44089210e-16],> 
>         [  0.00000000e+00,  -4.44089210e-16,   1.00000000e+00]])> 
> </pre>

 矩阵的乘法可以使用`dot`函数进行计算，对于二维数组，他计算的是矩阵乘积，而一维则是点积。当需要将一维数组当做列向量或者行向量进行矩阵计算的时候，推荐先使用`reshape`函数将一维数组转换为二维数组。
<pre class="lang:python decode:true ">&gt;&gt;&gt; a.reshape((-1,1))
array([[1],
       [2],
       [3]])
&gt;&gt;&gt; a.reshape((1,-1))
array([[1, 2, 3]])
</pre>

 除了`dot`计算乘积以外，NumPy还提供了`inner`和`outer`等多种计算乘积的函数。这些函数计算乘积的方式不同，尤其是当对于多维数组的时候更容易弄混。

## dot

对于两个一维数组，计算的是这两个数组对应的下标元素的乘积和（内积），对于二维数组，计算的是两个数组的矩阵乘；对于多维数组，他的通用计算公式如下，即结果数组中的每个元素都是：数组a的最后一维上的所有元素与数组b的倒数第二位上的所有元素的乘积和：
<pre class="lang:python decode:true ">dot(a,b)[i,j,k,m] = sum(a[i,j,:]*b[k,:,m])</pre>

 下面以两个三维数组乘积演示一下`dot`乘积的计算结果：

首先创建两个三维数组，这两个数组的最后两维满足矩阵乘积的条件：
<pre class="lang:python decode:true ">&gt;&gt;&gt; a = numpy.arange(12).reshape(2,3,2)
&gt;&gt;&gt; b = numpy.arange(12,24).reshape(2,2,3)
&gt;&gt;&gt; c = numpy.dot(a,b)
&gt;&gt;&gt; a
array([[[ 0,  1],
        [ 2,  3],
        [ 4,  5]],

       [[ 6,  7],
        [ 8,  9],
        [10, 11]]])
&gt;&gt;&gt; b
array([[[12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23]]])
&gt;&gt;&gt; c
array([[[[ 15,  16,  17],
         [ 21,  22,  23]],

        [[ 69,  74,  79],
         [ 99, 104, 109]],

        [[123, 132, 141],
         [177, 186, 195]]],

       [[[177, 190, 203],
         [255, 268, 281]],

        [[231, 248, 265],
         [333, 350, 367]],

        [[285, 306, 327],
         [411, 432, 453]]]])
&gt;&gt;&gt; 
</pre>

` dot`乘积的结果c可以视为分组矩阵的乘积：
<pre class="lang:python decode:true ">&gt;&gt;&gt; numpy.alltrue(c[0,:,0,:] == numpy.dot(a[0],b[0]))
True
&gt;&gt;&gt; numpy.alltrue(c[1,:,0,:] == numpy.dot(a[1],b[0]))
True
&gt;&gt;&gt; numpy.alltrue(c[0,:,1,:] == numpy.dot(a[0],b[1]))
True
&gt;&gt;&gt; numpy.alltrue(c[1,:,1,:] == numpy.dot(a[1],b[1]))
True
</pre>

## inner

和`dot`乘积一样，对于两个一维数组，计算的是这两个数组对应下标元素的乘积和；对于多维数组，它计算的结果数组中的每个元素都是：数组a和b的最后一维的内积，因此数组a和b的最后一维的长度必须相同：
<pre class="lang:python decode:true ">inner(a,b)[i,j,k,m] = sum(a[i,j,:]*b[k,m,:])</pre>

下面的是`inner`乘积的演示：
<pre class="lang:python decode:true ">&gt;&gt;&gt; a = numpy.arange(12).reshape(2,3,2)
&gt;&gt;&gt; b = numpy.arange(12,24).reshape(2,3,2)
&gt;&gt;&gt; c = numpy.inner(a,b)
&gt;&gt;&gt; a
array([[[ 0,  1],
        [ 2,  3],
        [ 4,  5]],

       [[ 6,  7],
        [ 8,  9],
        [10, 11]]])
&gt;&gt;&gt; b
array([[[12, 13],
        [14, 15],
        [16, 17]],

       [[18, 19],
        [20, 21],
        [22, 23]]])
&gt;&gt;&gt; c
array([[[[ 13,  15,  17],
         [ 19,  21,  23]],

        [[ 63,  73,  83],
         [ 93, 103, 113]],

        [[113, 131, 149],
         [167, 185, 203]]],

       [[[163, 189, 215],
         [241, 267, 293]],

        [[213, 247, 281],
         [315, 349, 383]],

        [[263, 305, 347],
         [389, 431, 473]]]])
&gt;&gt;&gt; 
&gt;&gt;&gt; c[0,0,0,0] == numpy.inner(a[0,0],b[0,0])
True
&gt;&gt;&gt; c[0,1,1,0] == numpy.inner(a[0,1],b[1,0])
True
&gt;&gt;&gt; c[1,2,1,2] == numpy.inner(a[1,2],b[1,2])
True</pre>

 矩阵中更高及的一些运算可以在Numpy线性代数字库`linalg`中找到。例如`inv`函数计算矩阵逆，`slove`函数可以用于求解多元一次方程组：
<pre class="lang:python decode:true ">&gt;&gt;&gt; a = numpy.random.rand(10,10)
&gt;&gt;&gt; a
array([[ 0.51119113,  0.01587309,  0.06756726,  0.26107582,  0.56370262,
         0.83373447,  0.9767889 ,  0.59555555,  0.46891593,  0.26305928],
       [ 0.06657669,  0.64299574,  0.31710559,  0.05816513,  0.99704149,
         0.61129615,  0.4851055 ,  0.95846369,  0.17266906,  0.69614029],
       [ 0.43214694,  0.20584426,  0.85070765,  0.76880992,  0.50606272,
         0.02250866,  0.59610836,  0.77656493,  0.26437074,  0.28279001],
       [ 0.22174128,  0.4652269 ,  0.52640362,  0.48593144,  0.91712586,
         0.27640262,  0.77170264,  0.58072642,  0.5372595 ,  0.47668177],
       [ 0.9510108 ,  0.81020259,  0.3761599 ,  0.36022875,  0.61060924,
         0.34430469,  0.18038006,  0.3399254 ,  0.06564282,  0.1147975 ],
       [ 0.02312573,  0.99414293,  0.80719027,  0.45335602,  0.92537962,
         0.99355802,  0.21572474,  0.10953976,  0.06993765,  0.21605461],
       [ 0.43476467,  0.24751591,  0.14183487,  0.34590407,  0.76004071,
         0.74512897,  0.50000311,  0.3784671 ,  0.71832824,  0.28137451],
       [ 0.24438204,  0.88371007,  0.20401232,  0.67434462,  0.9070798 ,
         0.95217587,  0.78584886,  0.9622344 ,  0.41135486,  0.1119106 ],
       [ 0.12576714,  0.36416279,  0.5116736 ,  0.57019995,  0.66191675,
         0.18258136,  0.22518437,  0.84651616,  0.96838621,  0.85809542],
       [ 0.96410503,  0.97810101,  0.67692549,  0.39055396,  0.82143376,
         0.69225712,  0.72820017,  0.37803354,  0.92029368,  0.14296149]])
&gt;&gt;&gt; b = numpy.random.rand(10)
&gt;&gt;&gt; b
array([ 0.45544759,  0.26996341,  0.6220333 ,  0.84496224,  0.62714415,
        0.23992104,  0.17559395,  0.57079526,  0.40088325,  0.6645625 ])
&gt;&gt;&gt; x = numpy.linalg.solve(a,b)
&gt;&gt;&gt; x
array([ 0.23383105,  0.75796694, -0.51499018,  0.83980065, -0.31916981,
       -0.54809016,  1.10416325, -0.65948116, -0.36661989,  0.99766284])
&gt;&gt;&gt; numpy.sum(numpy.abs(numpy.dot(a,x)-b))
1.2490009027033011e-15
</pre>

` solve`函数有两个参数a,b。a是一个$$N*N$$的二维数组，而b是一个长度为$$N$$的二维数组，`solve`函数找到一个长度为N的一维数组x，使得a和x的矩阵乘积正好等于b，数组x就是多元一次方程组的解。