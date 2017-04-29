---
title: Logistic回归
tags:
  - logistic
  - Python
  - 机器学习
id: 1047
categories:
  - Python
date: 2016-05-14 14:07:05
---

# 前言

我们会在这里介绍最优化算法。

假设现在有一些数据点，我们用一条曲线对其进行拟合，这个拟合过程就叫做回归。利用Logistic回归进行分类的主要思想是：根据现有的数据对分类边界建立回归公式，并由此进行分类。训练分类器时的做法就是寻找最佳的拟合参数，使用的是最优化算法，接下来介绍这个而值型输出分类器的数学原理。

# Logistics回归的一般过程

1.  收集数据
2.  准备数据：需要进行距离计算，所以要求数据类型为数值型
3.  分析数据
4.  训练算法：大部分时间将用于训练，训练的目的是找到最佳的分类回归系数
5.  测试算法
6.  使用算法：我们需要输入一些数据，并将其转换为对应的结构化数值，接着，给予训练好的回归系数就可以对这些数值进行简单的回归计算，判定它们属于哪个类别，然后就可以在输出的类别上做一些其他的分析工作。

## 基于Logistic回归和Sigmoid函数的分类

### 基于Logistics回归的优缺点

优点：计算代价不高，易于理解和实现

缺点：容易欠拟合，分类精度可能不高

适用的数据类型：数值型和标称型数据

所以这里我们需要的函数应该是能够接受所有的输入并且预测出类别。例如，在两个类的情况下，上述函数输出0或者1，这就是海维赛德阶跃函数（heaviside step function），或者直接称之为单位阶跃函数。这里我们常常适用`sigmoid`函数来取代海维赛德阶跃函数，`sigmoid`<!--more-->函数的具体计算公式是：\[\sigma(z)=\frac{1}{1+e^{-z}}\]

[![sigmoid](/wp-content/uploads/2016/05/sigmoid.png)](/wp-content/uploads/2016/05/sigmoid.png)

图给出了`sigmoid`函数在不同坐标尺度下的两条曲线图，当x为0的时候`sigmoid`函数随着x增大逐渐逼近于1，而反之则近0，当横坐标的值足够的大时候，`sigmoid`函数看起来就很像一个阶跃函数了。

为了实现Logistic回归分类器，我们可以在每个特征上都乘上一个回归系数，然后吧搜有的结果值相加，带入到`sigmoid`函数之中，进而得到一个范围在0-1之间的数值，任何大于0.5的数据被分在1，而小于0.5的则被分如0类，所以Logistic回归也可以被视为一种**概率估计**。

## 基于最优化方法的最佳回归系数确定

sigmoid函数输入记为z，可以通过这个公式得出：

\[z=w_{0}x_{0}+w_{1}x_{1}+w_{2}x_{2}+w_{3}x_{3}+...w_{n}x_{n}\]

如果采用向量的写法，上述公式可以写成$$z=w^{T}x$$，他表示将这两个数值的向量对应元素想成然后全部相加得到z值，其中向量x是分类器的输入数据，向量w也就是我们需要的最佳参数，为了尽可能的精确，需要用到一些最优化理论的一些知识。

### 梯度上升法

要找到某个函数的最大值，最好的方法就是沿着这个函数的梯度方向探寻，如果梯度记为$$\nabla$$，则函数f(x,y)的梯度有下面的式子表示：\[\nabla f(x,y)=\left( \begin{matrix} \frac{\partial f(x,y)}{\partial x} \\ \frac{\partial f(x,y)}{\partial y} \end{matrix}\right)\]

这是机器学习中最容易造成混淆的地方，但是在数学上不难，这个梯度意味着耀眼x的方向移动$$\frac{\partial f(x,y)}{\partial x}$$，沿y的方向移动$$\frac{\partial f(x,y)}{\partial y}$$。其中，函数f(x,y)必须在待计算点上有定义并且可微。

[![梯度上升算法](/wp-content/uploads/2016/05/梯度上升算法.png)](/wp-content/uploads/2016/05/梯度上升算法.png)

图示中的梯度上升算法沿着梯度方向移动了一步。可以看到，梯度算子总是纸箱函数值增长最快的方向，所谓移动方向，而没有提到移动量的大小。这个量值成为步长，记为$$\alpha$$。用向量表示的话，梯度上升算法的迭代公式如下：\[\omega:=\omega+\alpha\nabla_{w}f(w)\] 这个公式会一直被迭代执行，知道达到某个停止条件为止，例如迭代次数达到某个值或者达到某个允许的误差范围。

### 梯度下降算法

这里下降和上升的算法是一样的：\[\omega:=\omega+\alpha\nabla_{w}f(w)\] 梯度上升算法用于求函数的最大值，而梯度下降算法用来求函数的最小值。

## 训练算法

我们可以找到包含两个数值型特征：X1和X2。在此数据集上，我们通过梯度上升算法找到最佳的回归系数，也就是拟合出Logistic回归模型的最佳参数。
<pre class="lang:python decode:true">from numpy import *

def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)             #convert to NumPy matrix
    labelMat = mat(classLabels).transpose() #convert to NumPy matrix
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))
    for k in range(maxCycles):              #heavy on matrix operations
        h = sigmoid(dataMatrix*weights)     #matrix mult
        error = (labelMat - h)              #vector subtraction
        weights = weights + alpha * dataMatrix.transpose()* error #matrix mult
    return weights</pre>

 第一个函数就是打开`testSet.txt`并且逐行读取。每行的前两个值分别是X1和X2，第三个值是数据对应的类别标签。此外为了方便计算，该函数还将X0的值设定为1.0，接下来的这个函数就是`sigmoid`函数了。

梯度上升算法实在`gradAscent`中完成的，这个函数具有两个参数`dataMatIn`，其为二维的NumPy数组，每列分别代表每个不同的特征，每行代表训练样本，所以其包含了两个特征X1和X2再加上每个训练特征X0，这里`dataMatIn`里存放的实际上是100*3的矩阵，第二个则是类别标签，其是一个1*100的行向量。为了便于计算，需要将该行向量转换为列向量，做法是将原向量转置，在将其赋给`labelMat`。接下来的代码得到的矩阵大小，在设置一些梯度上升算法所需要的参数。

变量`alpha`是向目标移动的步长，`maxCycles`是迭代次数。在for循环完成之后，会返回训练好的回归系数，需要强调数组的是都是矩阵计算。

## 分析数据：给出决策边界

上面已经给出了一组回归系数，其确定了不同类别数据之间的分割线：
<pre class="lang:python decode:true">def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat,labelMat=loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0] 
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()</pre>

 程序之中的代码是直接用Matplotlib画出来的，我们需要指出的是在18行 我们指定了`sigmoid`函数为0，而0正是类别1和0的分界处。因此我们设定$$0=w_{0}x_{0}+w_{1}x_{1}+w_{2}x_{2}$$<span style="line-height: 1.42857; background-color: transparent;">，然后解出X2和X1的关系式（分割线的方程有，注意X0=1）</span>

[![Logistic](/wp-content/uploads/2016/05/Logistic.png)](/wp-content/uploads/2016/05/Logistic.png)

这个分类的结果相当的不错，再图上来看知错分了两到三个点，但是这个方法却进行了大量的计算，所以我们仍然需要对这个算法进行改进。

## 训练算法：随机梯度上升

梯度上升算法在每次更新回归系数的时候都需要遍历整个数据集，这个方法在处理大数据的时候，其计算复杂度就太高了，改进方法就是一次只用一个样本点来更新回归数据，这个方法就被成为随机梯度上升算法。由于可以在新样本到来的时候对分类器进行增量式更新，因而随机梯度上升算法是一个**在线学习算法**。
<pre class="lang:python decode:true">def stocGradAscent0(dataMatrix, classLabels):
    m,n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)   #initialize to all ones
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i]*weights))
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights</pre>

 可以看到，这个算法和梯度上升算法很相似，但是仍有一些区别，首先，h和error都是向量，而前者前部都是数值，第二，前者没有矩阵转换过程，所有的数据类型都是NumPy数组。这样我们验证结果可以发现，随机梯度上升算法并不是最佳分类线。而且迭代出现明显的收敛的特征：

[![Logistic](/wp-content/uploads/2016/05/Logistic.png)](/wp-content/uploads/2016/05/Logistic.png)

这里我们也给出三个参数的迭代次数和值的关系，由于数据集并不是线性可分的，所以存在一些不能正确分类的样本点，在每次迭代的过程的时候会引发系数的剧烈波动，这里我们希望算法能够避免来回波动，并且快速收敛到某个值。

[![iterationCycle](/wp-content/uploads/2016/05/iterationCycle.png)](/wp-content/uploads/2016/05/iterationCycle.png)

上图就展示了随机梯度上升算法在多次迭代过程中的回归系数变化情况，首先可以发现X3快速就进入了收敛，而1和2则需要更多次的迭代。并且在大的波动停止之后，还有一些小的周期性波动。

所以我们需要改进我们的随机梯度算法：
<pre class="lang:default decode:true">def stocGradAscent1(dataMatrix, classLabels, numIter=500):
    m,n = shape(dataMatrix)
    weights = ones(n)   #initialize to all ones

    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.0001    #apha decreases with iteration, does not 
            randIndex = int(random.uniform(0,len(dataIndex)))#go to 0 because of the constant
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]

            del(dataIndex[randIndex])

    return weights
</pre>

 这里我们只来介绍我们改进的地方，首先，在`alpha`每次迭代的时候都会调整，这样能够环节数据波动以及高频波动，虽然`alpha`会随着迭代次数不断减小，但是不会减小到0，如果需要处理的问题是动态变化的，那么可以适当加大上述常数项以确保新的值获得更大的回归系数。另外，在降低`alpha`的函数中，alpha每次减小1/(j+i)，其中j为迭代次数，i是样本点的下标，这样当`j&lt;&lt;max(i)`的时候，`alpha`就不是严格下降的。避免参数的严格下降也常见于模拟退火算法之中。

程序的第二点改变在随机选取样本来更新回归系数，这种方法将会减小周期性波动，这种方法每次随机从队列中选取一个值，并且删除这个值之后在进行下一次的迭代。

此外，改进的算法还增加了迭代次数作为第三个参数。

[![randomGradAscentIter](/wp-content/uploads/2016/05/randomGradAscentIter.png)](/wp-content/uploads/2016/05/randomGradAscentIter.png)

上图给出了每次迭代的时候各个回归系数的变动情况，这里我们能看出一些不同，首先由于stocGradAscent1可以收敛的更快，所以我们这里仅仅对数组进行了20次遍历，那么我们看一下结果，我这里丧心病狂的进行了4500次迭代。。。

[![gradAscent](/wp-content/uploads/2016/05/gradAscent.png)](/wp-content/uploads/2016/05/gradAscent.png)

从结果上来看，这个结果还是比较理想的～

# 实例：预测病马的死亡率

这里我们会食用logistic回归来预测患有疾病马的存活率，这里的数据包括686个样本和28个特征。

另外需要指出的是，该数据还有一个问题，数据集中有30%的值是缺失的。首先我们一个关注如何处理数据集中缺失的数据，然后再利用Logistic回归和随机梯度上升算法来预测病马的生死。

## 准备数据：处理数据中的缺失值

数据的缺失是一个非常棘手的问题，假设有100个样本和20个特征，有的时候数据相当的昂贵，扔掉或者重新获取都是不可取的，所以给出了一些可选的方法：

*   使用可用的特征均值来填补缺失值
*   使用特殊值来填补缺失值，如-1
*   忽略有缺失值的样本
*   使用相似的样本均值填补缺失值
*   使用别的算法预测缺失值

现在，我们对下一届要用的数据集进行预处理，使其可用顺利的使用分类算法。在预处理阶段需要做两件事情：

1 . 所有的缺失值都必须使用一个实数值替代，因为NumPy数据类型不允许包含缺失值。这里选择0来替换所有的缺失值，恰好能够适用于Logistic回归。这样做的直觉在于，我们需要一个在更新的时候不会影响系数的值。<span style="line-height: 1.42857; background-color: transparent;">
</span>
<pre class="lang:python decode:true">weights = weights + alpha * error * dataMatrix[randIndex]</pre>

 如果dataMatrix的某种特征对应值为0，那么这个特征的系数就不会做更新，即：
<pre class="lang:python decode:true">weights = weights</pre>

 另外由于sigmoid(0)=0.5，也就是他对结果的预测不具有任何倾向性。给予这个原因，缺失值用0替代既能够保留现有的数据，不需要对优化算法进行修改。此外该数据集中的特征值一般不为0，因此其也在某种程度上满足“特殊性”这个要求。

2 . 如果我们已经在测试数据集中发现了一条数据的类别标签已经缺失，那么我们就应该丢弃这个数据，因为类别标签很难用一个合适的值将其替换。采用Logistic回归进行分类的时候，这种做法是很合适的，而如果采用类似KNN的方法就不大可行。

## 测试算法：用logistic回归进行分类

使用logistic回归方法进行分类并不需要做很多工作，所需做的只是把测试集上每个特征向量乘以最优化方法得来的回归系数，然后将每个乘积求和，最终输入到`sigmoid`函数即可。

那么我们来看看实际运行效果吧：
<pre class="lang:python decode:true">def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob &gt; 0.5: return 1.0
    else: return 0.0

def colicTest():
    frTrain = open('horseColicTraining.txt'); frTest = open('horseColicTest.txt')
    trainingSet = []; trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainWeights = stocGradAscent1(array(trainingSet), trainingLabels, 1000)
    errorCount = 0; numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr), trainWeights))!= int(currLine[21]):
            errorCount += 1
    errorRate = (float(errorCount)/numTestVec)
    print "the error rate of this test is: %f" % errorRate
    return errorRate

def multiTest():
    numTests = 10; errorSum=0.0
    for k in range(numTests):
        errorSum += colicTest()
    print "after %d iterations the average error rate is: %f" % (numTests, errorSum/float(numTests))
</pre>

 第一个函数`classifyVector`，他以回归系数和特征向量来作为输入来计算对应的`sigmoid`值。

接下来的函数`colicTest`，用于打开测试和训练集，并对数据进行格式化处理的标签。该函数首先导入训练及，数据最初有三个标签，分别代表马的三中情况：“仍存活”、“已经死亡”和“已经安乐死”。为了方便，我们对后两者合并为“未能存活”这个标签。数据导入之后使用函数`stocGradAscent`来计算回归系数向量，这里能够自由设定迭代次数。在系数计算完成之后，导入测试集并且计算分类错误率。总体看来`coliTest`具有完全独立的功能。

最后一个`multiTest`，其功能是调用`coliTest`10次并且求结果的平均值。
<pre class="lang:default decode:true">the error rate of this test is: 0.313433
the error rate of this test is: 0.253731
the error rate of this test is: 0.253731
the error rate of this test is: 0.358209
the error rate of this test is: 0.388060
the error rate of this test is: 0.402985
the error rate of this test is: 0.388060
the error rate of this test is: 0.358209
the error rate of this test is: 0.328358
the error rate of this test is: 0.358209
after 10 iterations the average error rate is: 0.340299</pre>

# 小结

Logistic回归的目的是寻找一个非线性函数`sigmoid`的最佳拟合参数，求解过程可以由最优化算法完成，其中最常用的就是梯度上升法，也可以简化为随机梯度上升算法。

梯度随机上升算法能更好的节省计算资源。此外随机梯度上升是一个在线算法，其能够在新数据到来的时候就完成参数更新，而不需要读取整个数据集进行批处理计算。那么在下一篇我们会介绍SVM，支持向量自动机（support vector machine）