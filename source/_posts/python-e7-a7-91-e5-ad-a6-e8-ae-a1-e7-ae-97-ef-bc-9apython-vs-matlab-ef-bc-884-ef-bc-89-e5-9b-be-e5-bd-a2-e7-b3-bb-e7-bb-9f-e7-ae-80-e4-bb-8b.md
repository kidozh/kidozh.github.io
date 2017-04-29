---
title: '[Python] 科学计算：Python VS. MATLAB（4）----图形系统简介'
tags:
  - MATLAB
  - Python
id: 338
categories:
  - Python
date: 2015-05-03 14:43:03
---

<span style="font-family:Microsoft YaHei UI; font-size:14pt">**一、一般概念**
		</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">图形系统就是用来实现所谓的可视化的。在学习具体的命令之前，先了解一个可视化的图形具有哪些特征，以及这些特征具有什么关系。有了一个宏观的了解之后，记住几个核心的命令，等遇到具体问题时候查询相关文档或者查看类似图形别人的代码即可。就以我们在纸上作图作为比拟：
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">首先，我们需要一张白纸。这张白纸，就是一个所谓的figure。我们可以给这个figure取一个名字，写在这张纸的正中间。如果这是一系列纸中的一张，可能还会给它一个标号，比如第1页、第2页。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">然后，我们在这张纸上确定把图画在什么位置，即确定坐标轴（axes）这一张纸有几个坐标轴？坐标轴的刻度范围？线性的还是对数的？是方形的？双侧坐标轴的？等等。在画线区域，还可以考虑加网格。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">下面，我们可以在已有的坐标中画上我们需要的功能曲线了，也就是由一个个点连成的线。连线的方式有很多选择，比如直角坐标系、极坐标、饼状图、箭头图等。对于这些点或者线，我们可以控制它的风格：比如颜色、比如宽度等等。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">最后，要给图线添加一些说明文字，比如坐标轴的物理意义、图中曲线、符号的图例、这个图整体的标题、图中某些点的含义等等。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">**二、MATLAB的实现**
		</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">以一个简单的例子，大致给出MATLAB绘图的一般方法。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">t1=0:0.1:4
t2=0:0.05:4    %准备一些数据
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">figure()    %准备那张白纸
subplot(211)    %子图绘图
plot(t1,sin(2*pi*t1),'--g*')    %线形、颜色、点的表示法
title('sine function demo')    %标题文字
xlabel('time(s)')   
ylabel('votage(mV)')    %XY轴的文字
xlim([0.0,5.0])
ylim([-1.2,1.2])    %XY轴的区间范围
grid on    %加网格
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">subplot(212)
plot(t2,exp(-t2),':r')
hold on   %保持上一条线
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">plot(t2,cos(2*pi*t2),'--b')
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">xlabel('time')
ylabel('amplitude')
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">效果如图：
</span>

[![](/wp-content/uploads/2015/05/050315_0642_PythonP1.png)](http://s10.sinaimg.cn/middle/5f234d474b963d6917899&amp;amp;690)<span style="font-family:Microsoft YaHei UI; font-size:14pt">
		</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">**三、Python的实现**
		</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">实现上面相同的例子。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">Python用来绘图的工具包是matplotlib。翻译一段matplotlib主页上的话："matplotlib是一个Python 2D绘图库，提供多种可跨平台的硬拷贝格式的出版质量的图形及交互环境。"、"matplotlib努力让容易的事情继续容易，让难的事情尽量容易。"
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">网址（[http://matplotlib.sourceforge.net/gallery.html](http://matplotlib.sourceforge.net/gallery.html)）给出了各种常见的和一些不常见的图形实例，都有源码。在使用的时候，看到自己需要的图形，找到源码，填入自己的数据以及说明文字，一个漂亮的图就产生了！另外，对于3D作图，尽管matplotlib本身不提供，但是强有力的add-ons已经加入，完全可以胜任常规3D作图。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">初级用户建议使用pylab模式，pylab中包括了matplotlib.pyplot的所有绘图命令，以及numpy和matplotlib.mlab中的函数，在这个模式下，和MATLAB的绘图命令和套路几乎是完全一样的；高级用户建议使用matplotlib，可以进行更多的细节控制。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">方式一：
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">from pylab import *    #引入兼容MATLAB包：pylab
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">
t1=arange(0.0,4.0,0.1)
t2=arange(0.0,4.0,0.05)    #准备一些数据，注意和MATLAB的不同
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">figure()   
subplot(211)   
plot(t1,sin(2*pi*t1),'--g*')
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">title('sine function demo')   
xlabel('time(s)')
ylabel('votage(mV)')   
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">xlim([0.0,5.0])
ylim([-1.2,1.2])   
grid('on')    #控制网格显示和grid(True)效果一样。不带参数的grid()起到toggle的作用。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">subplot(212)
plot(t2,exp(-t2),':r')
hold('on')    #前一条线保持。用法和grid类似。
plot(t2,cos(2*pi*t2),'--b')
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">xlabel('time')
ylabel('amplitude')
show()    #这是和MATLAB很大的不同，这个命令用完，图形才会出来。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">效果如图：
</span>

[![](/wp-content/uploads/2015/05/050315_0642_PythonP2.png)](http://s8.sinaimg.cn/middle/5f234d474b963d74770e7&amp;amp;690)<span style="font-family:Microsoft YaHei UI; font-size:14pt">
		</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">方式二:
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">import matplotlib.pyplot as plt
import numpy as np    #导入包
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">t1=np.arange(0.0,4.0,0.1)
t2=np.arange(0.0,4.0,0.05)     #准备一些数据
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">fig = plt.figure()    #准备好这张纸，并把句柄传给fig
ax1 = fig.add_subplot(211)    #使用句柄fig添加一个子图
line1, = plt.plot(t1,np.sin(2*np.pi*t1),'--*')   #绘图，将句柄返给line1 
plt.title('sine function demo')   
plt.xlabel('time(s)')
plt.ylabel('votage(mV)')   
plt.xlim([0.0,5.0])
plt.ylim([-1.2,1.2])   
plt.grid('on')    #以上语句不难理解
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">##这种方式的优势和不同在以下语句体现。因为句柄的引入，让我们更加的面向对象，思路也更加清晰。代码的
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">##可读性也更高了。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">plt.setp(line1,lw=2,c='g')    #通过setp函数，设置句柄为line1的线的属性，c是color的简写
line1.set_antialiased(False)    #通过line1句柄的set_*属性设置line1的属性
plt.text(4,0,'$\mu=100,\\sigma=15$')    #添加text，注意，它能接受LaTeX哟！
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">ax2=fig.add_subplot(212)
plt.plot(t2,np.exp(-t2),':r')
plt.hold('on') 
plt.plot(t2,np.cos(2*np.pi*t2),'--b')
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">效果如图：
</span>

[![](/wp-content/uploads/2015/05/050315_0642_PythonP3.png)](http://s16.sinaimg.cn/middle/5f234d474b963d7e139af&amp;amp;690)<span style="font-family:Microsoft YaHei UI; font-size:14pt">
		</span>