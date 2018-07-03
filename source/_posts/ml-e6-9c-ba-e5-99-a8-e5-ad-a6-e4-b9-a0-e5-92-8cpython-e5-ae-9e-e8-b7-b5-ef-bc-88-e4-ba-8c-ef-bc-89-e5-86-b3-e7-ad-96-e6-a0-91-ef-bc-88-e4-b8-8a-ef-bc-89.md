---
title: '[ML]机器学习和Python实践（二）决策树（上）'
tags:
  - Python
  - 机器学习
id: 418
categories:
  - Python
  - 深度学习
  - 算法
date: 2015-11-21 19:30:15
---

# 1\. 决策树是什么？

在数学流程图里，经常有一些IF-ELSE的判定，当这种逻辑行为形成一连串的行为时，就可以画成一棵树，每个节点代表判定条件或者是某个状态，我们称之为决策树。下图就是一个很典型的决策树，长方形代表判定模块，椭圆形代表终止模块，表示已经得出结论，终止运行。

[caption id="attachment_430" align="aligncenter" width="573"][![决策树](/wp-content/uploads/2015/11/决策树.png "决策树")](/wp-content/uploads/2015/11/决策树.png) 来源：百度百科[/caption]

下面是百度百科的解释：
> 决策树(Decision Tree）是在已知各种情况发生概率的[基础](http://baike.baidu.com/subview/123417/8037007.htm)上，通过构成决策树来求取净现值的[期望](http://baike.baidu.com/subview/18713/8337948.htm)值大于等于零的概率，评价项目风险，判断其可行性的决策分析方法，是直观运用概率分析的一种图解法。由于这种决策分支画成图形很像一棵树的枝干，故称决策树。在机器学习中，决策树是一个预测模型，他代表的是对象属性与对象值之间的一种映射关系。Entropy = 系统的凌乱程度，使用算法[ID3](http://baike.baidu.com/view/66078.htm), [C4.5](http://baike.baidu.com/view/3122901.htm)和C5.0生成树算法使用熵。这一度量是基于信息学理论中熵的概念。决策树是一种树形结构，其中每个内部节点表示一个属性上的测试，每个分支代表一个测试输出，每个叶节点代表一种类别。分类树（决策树）是一种十分常用的分类方法。他是一种监管学习，所谓监管学习就是给定一堆样本，每个样本都有一组属性和一个类别，这些类别是事先确定的，那么通过学习得到一个分类器，这个分类器能够对新出现的对象给出正确的分类。这样的机器学习就被称之为监督学习。 

# 2.决策树的构造

首先，我们必须清楚决策树的优缺点。

决策书的优点有：

*   计算复杂度不高
*   输出结果容易理解
*   对中间值的缺失不敏感
*   可以处理不相关特征数据

缺点：

*   可能会产生过度匹配的问题

适用的数据类型：

*   数值型
*   标称型

其次，我们在构造决策树的时候必须解决的第一个问题就是，当前数据集上的哪个特征在划分数据分类的时候起到了决定性作用（此处可能会使用到信息论来划分数据集）。所以我们必须评估每个特征，在完成之后，原始的数据集就被花分成几个数据子集，这些子集会出现在第一个决策点的所有分支上，当某个分支下的数据属于同一个类型的时候，则该数据无需进行划分，反之，则需要重复划分数据子集的过程。划分数据子集的算法和划分原始数据集的方法相同，直至所有具有相同类型的数据均在一个数据子集内。

决策树的一般流程：

1.  收集数据
2.  准备数据：树的构造算法只适合于标称型数据，因此数据必须离散化
3.  分析数据：可以使用任何方法，但是必须检查图形是否符合预期
4.  训练数据：构造树的数据结构
5.  测试算法：使用经验树计算错误率
6.  使用算法：可以用于任何监督学习算法

伪代码如下：

```
if  数据集中每个子项属于同一分类：
	return 类标签
else：
	寻找划分数据集最好的特征
	划分数据集
	创建分支节点
		for 子集 in 每个划分的子集：
			迭代本过程
	return 分支节点
```
上面函数是个递归函数，在这个过程的之后，我们就可以知道怎么去转换成Python代码。 在决策算法中，使用[ID3算法](https://zh.wikipedia.org/wiki/ID3%E7%AE%97%E6%B3%95 "ID3算法")（也有使用二分法划分数据的）。 

# 3.信息增益

划分数据集的原则就有减少数据的熵（这个提法最早来自于香农），熵定义为信息的期望值。

首先，我们定义带分类的事物划分在多个分类里面，则符号\(x_{i}\)的信息定义为：

 \(l(x_{i})=\log_{2}p(x_{i}) \)

其中$$ p(x_{i}) $$是选择该分类的概率。

为了计算熵，我们需要计算所有类别所有可能值包含的信息期望值，通过下面的公式可以得到：

\(H=-\sum_{i=1}^{n} p(x_{i})\log_{2}p(x_{i})\)

其中n是分类的数目。

下面我们就开始确定鱼类的决策，注意了，我在博客里给出的代码可能有问题，我会在**下**篇给出工程文件。
<table style="height: 138px;" width="779"><tbody><tr><td>   </td><td>不浮出水是否能够生存</td><td>是否有脚蹼</td><td>属于鱼类</td></tr><tr><td>1</td><td>是</td><td>是</td><td>是</td></tr><tr><td>2</td><td>是</td><td>是</td><td>是</td></tr><tr><td>3</td><td>是</td><td>否</td><td>否</td></tr><tr><td>4</td><td>否</td><td>是</td><td>否</td></tr><tr><td>5</td><td>否</td><td>是</td><td>否</td></tr></tbody></table>

## 3.1 计算给定数据集的香农熵
```python
from math import log

def clacShannonEnt (dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet: # 为所有的可能进行分类
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel]=0
		labelCounts[currentLabel] += 1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob*log(prob,2) # 以2为底求对数
	return shannonEnt
```


其代码的意思十分简洁了当：

*   计算数据集中实例的数目
*   创建一个数据字典，其键值是最后一列的数值。若当前键值不存在则扩展字典将当前键值加入字典
*   使用所有的类标签的发生频率来计算类别出现的概率

在建立树的文件中，我们使用上面的伪代码函数就可以得到简单的判定数据集的程序，当然你可以输入自己的createDataSet()函数：
```python
def createDataSet():
	dataSet=[['1','1',yes],
		['1','1',yes],
		['1','0',no],
		['0','1',no],
		['0','1',no]
	]
	labels = ['no surfacing','flippers']
	return dataSet,labels
```


熵越高，则混合的数据越多，当我们添加更多的类的时候，香农熵在一般情况下增大，通过获取熵，我们就可以按照最大信息增益的方法划分数据集。

当然，基尼不纯度也可以度量集合的无序程度，你可以_点击这里(__http://www.cnblogs.com/ceys/archive/2012/08/04/2622928.html__)_查看这几种情况的细微差别，简而言之，基尼不纯度大概可以理解为从一个数据集中随机选取子项，度量其被错误分类到其他分组里的概率。

_例如 一个随机事件X ，P(X=0) = 0.5 ,P(X=1)=0.5。那么基尼不纯度就为  <wbr></wbr> P(X=0)*(1 - P(X=0)) +  <wbr></wbr> <wbr></wbr>P(X=1)*(1 - P(X=1)) <wbr></wbr> = 0.5。 <wbr></wbr>一个随机事件Y ，P(Y=0) = 0.1 ,P(Y=1)=0.9。那么基尼不纯度就为P(Y=0)*(1 - P(Y=0)) +  <wbr></wbr> <wbr></wbr>P(Y=1)*(1 - P(Y=1)) <wbr></wbr> = 0.18。很明显 X比Y更混乱，因为两个都为0.5 很难判断哪个发生。而Y就确定得多，Y=0发生的概率很大。而基尼不纯度也就越小。所以基尼不纯度也可以作为 衡量系统混乱程度的标准。_

## 3.2划分数据集

分类算法需要测量信息熵，还需要划分数据集，度量划分数据集的熵，就可以判断当前是否正确的划分了数据集。首先，我们可以理解其过程为将散落在二维空间内的点云，在数据之间使用一条线，将其分成两个部分。

那么我们就需要按照特定特征来划分数据集了
```python
def spiltDataSet(dataSet, axis, value): # 划分数据集
	retDataSet = []  # 创建新的list对象
	for featVec in dataSet:
		if featVec[axis] == value: # 抽取
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet
```


 上面的代码使用了三个输入参数，待划分的数据集，划分数据的特征，需要返回的特征的值。在这个函数里面，我们遍历每个数据集中的每个元素，一旦发现符合要求的值，就将其添加到新创建的列表之中。接下来，我们将会遍历整个数据集，循环计算香农熵和spiltDataSet函数，找到最好的特征划分方式，熵计算将会告诉我们如何划分数据集。

## 3.3选择最好的数据集划分方式

首先，再划分数据集之前，我们需要计算整个数据集的原始香农熵，并且保存下来与划分后的数据集的熵值进行比较，我们首先应当遍历数据集中的所有特征，使用列表推导来创建新的列表。其次，我们应当遍历当前特征中的所有唯一属性值，并且对每个特征划分一次数据集，然后计算数据集的新熵并加以求和，信息增益是熵的减少。最后比较全部特征中的信息增益，返回最好划分的索引值即可。
```default
def chooseBestFeatureToSpilt(dataSet) :
	numFeatures = len(dataSet[0])-1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0
	bestFeature = -1
	for i in range(numFeatures) :
		featList = [example[i] for example in dataSet] # 创建唯一的分类标签列表
		uniqueVals = set(featlist)
		newEntropy = 0.0
		for value in uniqueVals :
			subDataSet = spiltDataSet(dataSet, i, value) # 计算每一种划分方式的信息熵
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob*calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if infoGain>baseEntropy ： # 计算最好的信息增益
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature
```

