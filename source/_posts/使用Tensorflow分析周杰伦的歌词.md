---
title: 使用Tensorflow分析周杰伦的歌词
date: 2017-05-10 13:52:50
tags:
---

# 前言

最近一直在看TensorFlow的东西，也不知道怎么做才好，借着TF的word2vec的例子，我来分析一下周杰伦所唱的歌。

# 准备

首先，我准备了周杰伦唱过的歌的歌词，你可以在这里[周杰伦唱过的歌](Jay_Chou.txt)下载这个例子。当然你有更好的例子的话，欢迎联系[本弱](mailto:kidozh@kidozh.com)

根据TF官方的数据，其给的是一个英文的分词表，所以移花接木的，这里可以使用中文分词工具`jieba`来处理歌词的分词。

```python
words = []
with open('Jay_Chou.txt','r') as f:
    lyrics = f.read().split()
    # use jieba to cut the words
    import jieba
    for everySentence in lyrics:
        words.extend(jieba.cut(everySentence))
```

这里的`words`是用于记录分词后的周杰伦的歌词的一个列表。

# 创建一个字典来方便检索数据

这里根据TF的入门指导，选择字典来检索数据，并且为后面`skip-gram` 模型的生成提供指导。

```python
import collections
cnt = collections.Counter(words)
# print 15 most common
print(cnt.most_common(15),len(cnt.keys()))

# sample is 925
vocabularySize = 600

# build the dictionary and replace unknown figure with UNK
def buildDataset(words, vocabularySize):
    '''
    build the count dictionary for words
    :param words: a list containing different words
    :param vocabularySize: how many words will be choosen to analysis the lyrics
    :return: data,count[(words,cnt),...],dict(words->cnt),reversedict(cnt->words)
    '''
    count = [['UNK',-1]]
    # choose 499 words
    count.extend(collections.Counter(words).most_common(vocabularySize-1))
    dictionary = {}
    # place a rank according to `most common`
    for word,_ in count:
        dictionary[word] = len(dictionary)

    data = []
    unknownCnt = 0

    # traverse all the words and get its rank corresponding to data
    for word in words:
        # if this words in most common 499, then label it
        if word in dictionary:
            # return its index in common dictionary
            index = dictionary[word]
        else:
            # it belongs to unknown word
            index = 0
            unknownCnt += 1
        # set up a mapping between word and index
        data.append(index)
    # update unknown number
    count[0][1] = unknownCnt
    reverseDict = dict(zip(dictionary.values(),dictionary.keys()))
    return data,count,dictionary,reverseDict

data,countList,dictionary,reverseDict = buildDataset(words,vocabularySize)

# remove original data for saving memory
del words,lyrics

print('Most Common words',countList[:5])
# get first letter
print('Sample data', data[:10], [reverseDict[i] for i in data[:10]])
```

这里使用`collection`这个高效的容器来检索前600个出现次数最多的词，并且检索出来。然后将检索的前600个字编号。

创建一个索引数组，遍历原始数据中的列表，如果当前遍历对象是600个字中的一员，那么对应索引数组中的成员就赋予600个字的标号，如果不是，程序就会认为其是不可识别的，将其指向未知这个字符（UNK）的标号（应该是0），遍历结束后，补充上更新后的不可识别的字符。这样数据就转换成了一个带有索引编号的数组，一个字符计数的字典，一个标号的字典以及其反式字典。


然后删除掉原始数据，以便节省内存空间。


# 建立skip-gram模型

## 什么是skip-gram模型？

和词袋模型相反，`skip-gram`是通过从一个文字来预测的上下文。

其实, 用一个向量唯一标识一个word已经提出有一段时间了. Tomáš Mikolov的word2vec算法的一个不同之处在于, 他把一个word映射到高维(50到300维), 并且在这个维度上有了很多有意思的语言学特性, 比如单词”Rome”的表达`vec(‘Rome’)`, 可以是`vec(‘Paris’) – vec(‘France’) + vec(‘Italy’)`的计算结果.

> 向量空间模型 (VSMs)将词汇表达（嵌套）于一个连续的向量空间中，语义近似的词汇被映射为相邻的数据点。向量空间模型在自然语言处理领域中有着漫长且丰富的历史，不过几乎所有利用这一模型的方法都依赖于 分布式假设，其核心思想为出现于上下文情景中的词汇都有相类似的语义。采用这一假设的研究方法大致分为以下两类：基于技术的方法 (e.g. 潜在语义分析)， 和 预测方法 (e.g. 神经概率化语言模型).

## 如何建立一个skip-gram模型？

> 建议直接参考[TensorFlow中文教程](http://www.tensorfly.cn/tfdoc/tutorials/word2vec.html)

`the quick brown fox jumped over the lazy dog`

我们首先对一些单词以及它们的上下文环境建立一个数据集。我们可以以任何合理的方式定义‘上下文’，而通常上这个方式是根据文字的句法语境的（使用语法原理的方式处理当前目标单词可以看一下这篇文献 [Levy et al](https://levyomer.files.wordpress.com/2014/04/dependency-based-word-embeddings-acl-2014.pdf).，比如说把目标单词左边的内容当做一个‘上下文’，或者以目标单词右边的内容，等等。现在我们把目标单词的左右单词视作一个上下文， 使用大小为1的窗口，这样就得到这样一个由`(上下文, 目标单词)` 组成的数据集：

`([the, brown], quick), ([quick, fox], brown), ([brown, jumped], fox), ...`

前文提到Skip-Gram模型是把目标单词和上下文颠倒过来，所以在这个问题中，举个例子，就是用`'quick'`来预测 `'the'` 和 `'brown'` ，用 `'brown'` 预测 `'quick'` 和 `'brown'` 。因此这个数据集就变成由`(输入, 输出)`组成的：

`(quick, the), (quick, brown), (brown, quick), (brown, fox), ...`

目标函数通常是对整个数据集建立的，但是本问题中要对每一个样本（或者是一个`batch_size` 很小的样本集，通常设置为`16 <= batch_size <= 512`）在同一时间执行特别的操作，称之为随机梯度下降 [SGD](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)。我们来看一下训练过程中每一步的执行。

假设用 t 表示上面这个例子中quick 来预测 the 的训练的单个循环。用 `num_noise` 定义从噪声分布中挑选出来的噪声（相反的）单词的个数，通常使用一元分布，P(w)。为了简单起见，我们就定`num_noise=1`，用`sheep`选作噪声词。接下来就可以计算每一对观察值和噪声值的损失函数了。

## 构建针对skip-gram的数据集

`skip-gram`模型可以理解为每次从一个长度为`[skipWindow...,target,skipWindow... ]`的样本中找出位于两端的元素和目标输出构成的一个`(输出,输入)`的一个样本。

```python
dataIndex = 0

import numpy as np
import random

# generate a training batch for skip-gram model
def generateSkipGramBatch(batchSize,numSkip,skipWinnow):
    '''
    generate a training batch for skip-gram model
    :param batchSize: the size of batch
    :param numSkip: How many times to reuse an input to generate a label.
    :param skipWinnow: How many words to consider left and right.
    :return: 
    '''
    global dataIndex
    assert batchSize % numSkip == 0
    assert numSkip <= 2* skipWinnow

    batch = np.ndarray(shape=(batchSize),dtype=np.int32)
    labels = np.ndarray(shape=(batchSize,1),dtype=np.int32)

    span = 2 * skipWinnow + 1 # [ skip_window target skip_window ]
    # a binary queue to filter the words
    buffer = collections.deque(maxlen=span)

    for _ in range(span):
        # construct a winnow in data
        buffer.append(data[dataIndex])
        dataIndex = (dataIndex + 1 ) % len(data)

    for i in range(batchSize // numSkip):
        # ensure target located in the center of window
        target = skipWinnow
        aviodTarget = [skipWinnow]

        for j in range(numSkip):
            while target in aviodTarget:
                # get a number that is not located in the center of window
                target = random.randint(0,span-1)
            aviodTarget.append(target)
            # pick up
            batch[i * numSkip + j ] = buffer[skipWinnow]
            labels[i * numSkip + j,0] = buffer[target]

        # join the next words
        buffer.append(data[dataIndex])
        dataIndex = (dataIndex + 1) % len(data)

    dataIndex = (dataIndex + len(data) - span) % len(data)
    return batch,labels
```

在这个函数之中，`batchSize`指的是每次选择的样本的数量，而`numSkip`指的则是每次target和周围词的复用率，`dataIndex`作为一个全局变量则是起到一个类似于指针的作用。

代码在初始化的时候，初始化了定形状的`batch`和`label`矩阵，接着，代码将会从当前`dataIndex`取`2 * skipWinnow + 1`个长度为`2 * skipWinnow + 1`压进一个长度为双端队列。接着根据指示其就会选出target周围的`numSkip`个词，接着索引指向下一个字符，继续操作。直至选出`batchSize`个样本出来。`batch`是选出的输出词，而`label`则是输入词。

# 开始skip-gram的训练

预设定条件之后，就可以开始`skip-gram`的训练了。

```python
batchSize = 128
embeddingSize = 128 # dimension of emblemding vector
skipWindow = 1 # how many words contains in both left and right direction
numSkip = 2 # how many times words will be used in sampling

# We pick a random validation set to sample nearest neighbors. Here we limit the
# validation samples to the words that have a low numeric ID, which by
# construction are also the most frequent.

validSize = 16 # Random set of words to evaluate similarity on.
validWindow = 100 # Only pick dev samples in the head of the distribution.
validExample = np.random.choice(validWindow,validSize,replace=False)
numSample = 64 # number of negative sample

import tensorflow as tf
import math

graph = tf.Graph()

with graph.as_default():
    # Input data.
    train_inputs = tf.placeholder(tf.int32, shape=[batchSize])
    train_labels = tf.placeholder(tf.int32, shape=[batchSize, 1])
    valid_dataset = tf.constant(validExample, dtype=tf.int32)
    
    with tf.device('/cpu:0'):
        # Look up embeddings for inputs.
        embeddings = tf.Variable(
            tf.random_uniform([vocabularySize, embeddingSize], -1.0, 1.0))
        embed = tf.nn.embedding_lookup(embeddings, train_inputs)

        # Construct the variables for the NCE loss
        nce_weights = tf.Variable(
            tf.truncated_normal([vocabularySize, embeddingSize],
                                stddev=1.0 / math.sqrt(embeddingSize)))
        nce_biases = tf.Variable(tf.zeros([vocabularySize]))

        # Compute the average NCE loss for the batch.
        # tf.nce_loss automatically draws a new sample of the negative labels each
        # time we evaluate the loss.
        loss = tf.reduce_mean(
            tf.nn.nce_loss(weights=nce_weights,
                           biases=nce_biases,
                           labels=train_labels,
                           inputs=embed,
                           num_sampled=numSample,
                           num_classes=vocabularySize))

        # Construct the SGD optimizer using a learning rate of 1.0.
        optimizer = tf.train.GradientDescentOptimizer(1.0).minimize(loss)

        # Compute the cosine similarity between minibatch examples and all embeddings.
        norm = tf.sqrt(tf.reduce_sum(tf.square(embeddings), 1, keep_dims=True))
        normalized_embeddings = embeddings / norm
        valid_embeddings = tf.nn.embedding_lookup(
            normalized_embeddings, valid_dataset)
        similarity = tf.matmul(
            valid_embeddings, normalized_embeddings, transpose_b=True)

        # Add variable initializer.
        init = tf.global_variables_initializer()
```

首先使用了两个占位符，其主要作为`batch`和`label`所feed的对象。由于我们没有GPU配置（渣电脑是AMD的显卡，哈哈哈）。然后建立了一个形状为`[vocabularySize, embeddingSize]`的一个嵌套的矩阵。我们用唯一的随机值来初始化这个大矩阵。

然后我们需要对批数据中的单词建立嵌套向量，TensorFlow提供了方便的工具函数。也就是`tf.nn.embedding_lookup`

对噪声-比对的损失计算就使用一个逻辑回归模型。对此，我们需要对语料库中的每个单词定义一个权重值（weight）和偏差值（baise）。(也可称之为输出权重 与之对应的 输入嵌套值)。

{% asset_img word2vec_NN.png word2vec实例 %}

所以说word2vec是只有一个隐层的全连接神经网络, 用来预测给定单词的关联度大的单词.WI 的大小是VxN, V是单词字典的大小, 每次输入是一个单词, N是你设定的隐层大小.

对于整个数据集，当梯度下降的过程中不断地更新参数，对应产生的效果就是不断地移动每个单词的嵌套向量，直到可以把真实单词和噪声单词很好得区分开。所以这里使用的是`NCE`函数。

```python
        loss = tf.reduce_mean(
            tf.nn.nce_loss(weights=nce_weights,
                           biases=nce_biases,
                           labels=train_labels,
                           inputs=embed,
                           num_sampled=numSample,
                           num_classes=vocabularySize))
```

# 训练模型

训练的过程很简单，只要在循环中使用`feed_dict`不断给占位符填充数据，同时调用`session.run`即可。

```python
# Step 5: Begin training.
num_steps = 100001
from six.moves import xrange

with tf.Session(graph=graph) as session:
    # We must initialize all variables before we use them.
    init.run()
    print("Initialized")

    average_loss = 0
    for step in xrange(num_steps):
        batch_inputs, batch_labels = generateSkipGramBatch(
            batchSize, numSkip, skipWindow)
        feed_dict = {train_inputs: batch_inputs, train_labels: batch_labels}

        # We perform one update step by evaluating the optimizer op (including it
        # in the list of returned values for session.run()
        _, loss_val = session.run([optimizer, loss], feed_dict=feed_dict)
        average_loss += loss_val

        if step % 2000 == 0:
            if step > 0:
                average_loss /= 2000
            # The average loss is an estimate of the loss over the last 2000 batches.
            print("Average loss at step ", step, ": ", average_loss)
            average_loss = 0

        # Note that this is expensive (~20% slowdown if computed every 500 steps)
        if step % 10000 == 0:
            sim = similarity.eval()
            for i in xrange(validSize):
                valid_word = reverseDict[validExample[i]]
                top_k = 8  # number of nearest neighbors
                nearest = (-sim[i, :]).argsort()[1:top_k + 1]
                log_str = "Nearest to %s:" % valid_word
                for k in xrange(top_k):
                    close_word = reverseDict[nearest[k]]
                    log_str = "%s %s," % (log_str, close_word)
                print(log_str)
    final_embeddings = normalized_embeddings.eval()

# Step 6: Visualize the embeddings.
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['PingFang SC']
matplotlib.rcParams['font.family']='sans-serif'


def plot_with_labels(low_dim_embs, labels, filename='tsne.svg'):
    assert low_dim_embs.shape[0] >= len(labels), "More labels than embeddings"
    plt.figure(figsize=(18, 18))  # in inches
    for i, label in enumerate(labels):
        x, y = low_dim_embs[i, :]
        plt.scatter(x, y)
        plt.annotate(label,
                     xy=(x, y),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')

    plt.savefig(filename)

try:
    from sklearn.manifold import TSNE
    import matplotlib.pyplot as plt

    tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000)
    plot_only = 500
    low_dim_embs = tsne.fit_transform(final_embeddings[:plot_only, :])
    labels = [reverseDict[i] for i in xrange(plot_only)]
    plot_with_labels(low_dim_embs, labels)

except ImportError:
    print("Please install sklearn, matplotlib, and scipy to visualize embeddings.")
```

# 结果

还是很尴尬的。。。

![下载观看](tsne.svg)


# 展望

可以利用这个为之后的`seq2seq`模型的建立提供支持

# 所有的代码下载

点击[这里](web2vec.py)

**Note** : 可能有乱码哦～