# -*- coding: UTF-8 -*-
# author = kidozh

# Step 1 : preparing data
words = []
with open('Jay_Chou.txt','r') as f:
    lyrics = f.read().split()
    # use jieba to cut the words
    import jieba
    for everySentence in lyrics:
        words.extend(jieba.cut(everySentence))


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


# Build and train skip-gram model

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