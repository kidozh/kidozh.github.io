---
title: '[Python] 科学计算：Python VS. MATLAB（5）----常微分方程数值解'
tags:
  - MATLAB
  - Python
id: 344
categories:
  - Python
date: 2015-05-03 14:45:00
---

**一、常微分方程的一般理论**
		

凡含有参数，未知函数和未知函数导数 (或微分) 的方程，称为微分方程，有时简称为方程，未知函数是一元函数的微分方程称作常微分方程，未知数是多元函数的微分方程称作偏微分方程。微分方程中出现的未知函数最高阶导数的阶数，称为微分方程的阶。


**二、使用Python**
		

scipy中提供了用于解常微分方程的函数odeint()，完整的调用形式如下：


**scipy.integrate.odeint**(**func, y0, t**, args=(), Dfun=None, col_deriv=0, full_output=0, ml=None, mu=None, rtol=None, atol=None, tcrit=None, h0=0.0, hmax=0.0,hmin=0.0, ixpr=0, mxstep=0, mxhnil=0, mxordn=12, mxords=5, printmessg=0)
实际使用中，还是主要使用前三个参数，即微分方程的描写函数、初值和需要求解函数值对应的的时间点。接收数组形式。这个函数，要求微分方程必须化为标准形式，即dy/dt=f(y,t,)。而我们会发现，高阶方程的标准化工作，其实是解微分方程最主要的工作。下面是一个二阶常微分方程的例子，通过这个例子，学会变化标准形式的方法。 
典型的二阶方程：y"+a*y'+b*y=0 ，不满足标准式。变量替换，假设输入是Y=[y,y']，输出是Y'=[y',y"]，那么方程就化为了Y'=F(Y,t)的形式。我们知道Y[0]=y, Y[1]=y'，所以输出形式就是：


y'=Y[1]


y"=-a*y'-b*y=-a*Y[1]-B*Y[0]


有了这个形式，我们很容易写出Python代码：

from scipy.integrate import odeint
from pylab import *


def deriv(y,t):        # 返回值是y和y的导数组成的数组


    a = -2.0
    b = -0.1
    return array([ y[1], a*y[0]+b*y[1] ])


time = linspace(0.0,50.0,1000)
yinit = array([0.0005,0.2])     # 初值
y = odeint(deriv,yinit,time)



figure()
plot(time,y[:,0],label='y')    #y[:,0]即返回值的第一列，是y的值。label是为了显示legend用的。
hold('on')
plot(time,y[:,1],label="y'")     #y[:,1]即返回值的第二列，是y'的值
xlabel('t')
ylabel('y')
legend()
show()


[![](/wp-content/uploads/2015/05/050315_0644_PythonP1.png)](http://s14.sinaimg.cn/middle/5f234d474b9c9cf78cb7d&amp;690) 


-------------------------------------------------------


**三、使用MATLAB**
		

同样，MATLAB解微分方程的第一步工作也是化简微分方程为一阶的标准形式，这个和Python是完全一样的。只是函数的编写不一样。MATLAB可以在m文件函数中定义一个函数和多个子函数，但是子函数只能由同一m文件中的函数调用。并且还要求m文件名必须和主函数同名；而Python无此限制，在此可见一斑，也能看出Python代码的相对更优美。另外，Python的索引从0开始，MATLAB的从1开始，为了这个习惯，编写函数的时候也要有所注意。


MATLAB在这里也有一个优势，就是提供了多个求解函数，以应对时间需求、精度需求和刚性问题等要求。这就比scipy中的函数灵活了不少。如果使用scipy，只能自己编写函数了！


这些函数几乎统一的调用方式是：[to,yo]=solver(func,tspan,y0,options)


其中，solver是ode45(最常用)、ode23、ode23t、ode23s、ode23tb等


例1：y"+4*y=3*sin(t)  y(0)=1,y'(0)=0


定义一个函数，描写这个微分方程：


function dy=fun1(t,y)


dy(1,1)=y(2)


dy(2,1)=3*sin(t)-4*y(1)


将这个函数存为fun1.m, 然后写一个脚本调用它，解方程。不妨这个脚本就叫做callfun1.m


tspan=[0,5];
y0=[1,0];
[t,y]=ode45(@fun1,tspan,y0);
figure;
plot(t,y(:,1),'k-');
hold on
plot(t,y(:,2),'k:');
xlabel('t');


画出来的图是这样子的：


[![](/wp-content/uploads/2015/05/050315_0644_PythonP2.png)](http://s14.sinaimg.cn/middle/5f234d474b9c9cfe9297d&amp;690)
		

**三、对比**
		

下面用Python实现MATLAB部分的例子。


from scipy.integrate import odeint
from pylab import *


#定义函数


def deriv(y,t):
    return array([ y[1], 3*sin(t)-4*y[0] ])


#设置初值和t区间


time = linspace(0.0,5.0,1000)
yinit = array([1,0])
#解方程并绘图


y = odeint(deriv,yinit,time)


figure()
plot(time,y[:,0],label='y') 
hold('on')
plot(time,y[:,1],label="y'") 
xlabel('t')
ylabel('y')
legend()
show()
结果如图，可以和MATLAB绘制出来的对比一下：


[![](/wp-content/uploads/2015/05/050315_0644_PythonP3.png)](http://s1.sinaimg.cn/middle/5f234d474b9c9d0633870&amp;690)
		

-------------------------


下面用MATLAB实现Python部分的例子。


函数脚本（fun1.m）：


function dy=fun1(t,y)
dy(1,1)=y(2)
dy(2,1)=-2.0*y(1)-0.1*y(2)


调用脚本（callfun1.m）：


tspan=[0,50];
y0=[0.0005,0.2];
[t,y]=ode45(@fun1,tspan,y0);
figure;
plot(t,y(:,1),'k-');
hold on
plot(t,y(:,2),'k:');
xlabel('t');


绘图结果：


[![](/wp-content/uploads/2015/05/050315_0644_PythonP4.png)](http://s9.sinaimg.cn/middle/5f234d474b9c9d0d7c238&amp;690)
		

补充说明：


MATLAB还可以使用inline的形式调用函数。比如：


tspan=[0,5];
y0=[1,0]
fun1=inline('[y(2);3*sin(t)-4*y(1)]','t','y');    %注意这一句
[t,y]=ode45(fun1,tspan,y0);
figure;
plot(t,y(:,1),'k-');
hold on
plot(t,y(:,2),'k:');
xlabel('t');


这时候，不需要关心文件名的问题了，但是这种写法明显不利于推广和模块化，所以不推荐使用这样的形式。