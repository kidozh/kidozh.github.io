---
title: 使用Keras建立生成对抗网络
date: 2017-08-09 00:35:13
tags:
---

# 前言

生成对抗网络（英语：Generative Adversarial Network，简称GAN）是非监督式学习的一种方法，通过让两个神经网络相互博弈的方式进行学习。该方法由扬·古德费洛等人于2014年提出。

生成对抗网络由一个生成网络与一个判别网络组成。生成网络从潜在空间（latent space）中随机采样作为输入，其输出结果需要尽量模仿训练集中的真实样本。判别网络的输入则为真实样本或生成网络的输出，其目的是将生成网络的输出从真实样本中尽可能分辨出来。而生成网络则要尽可能地欺骗判别网络。两个网络相互对抗、不断调整参数，最终目的是使判别网络无法判断生成网络的输出结果是否真实。

虽然说GAN听起来很简单，但是要构建这样的一个模型却不是那么轻而易举。在GAN之中，有两个相关联的深度网络，当训练的时候他们都会发生梯度的反向传播。深度卷积生成对抗网络（Deep Convolutional GAN）就是这样一种典型的GAN。

在这篇文章之中，我们会介绍如何通过Keras构建一个DCGAN。我们将会利用它来学习如何编写一个手写的数字，就好像MNIST数据集一样。

# 判别网络

判别网络能够很好的判断图片是否是一个真实的图像，如图所示，其也就是一个很常见的卷积神经网络。对于MNIST数据库，其驶入就是一张28\*28\*1的图片。最终的sigmoid激活函数是告诉这张图片是真实的图片的概率。这个和典型的CNN模型最大的区别就是在层与层之间判别网络丢失了池化层。这个时候，一个有步长的卷积就用来下采样了。在每个CNN层使用的激活函数是leaky Relu函数（LeakyRelU是修正线性单元（Rectified Linear Unit，ReLU）的特殊版本，当不激活时，LeakyReLU仍然会有非零输出值，从而获得一个小梯度，避免ReLU可能出现的神经元“死亡”现象。即，$$f(x)=alpha * x for x < 0$$  $$f(x) = x for x>=0$$）。为了阻止过拟合，Dropout层被使用了

{% asset_img GANdiscriminator.png 判别网络 %}

```python
class DCGAN(object):
    def __init__(self,img_rows=28,img_cols=28,img_channel=1):
        self.img_rows = img_rows
        self.img_cols = img_cols
        self.img_channel = img_channel
        self.D = None  # discriminator
        self.G = None  # generator
        self.AM = None  # adversarial model
        self.DM = None  # discriminator model

    def discriminator(self,depth=64,dropout=0.5,cnn_layers_num=4):
        if self.D:
            return self.D
        self.D = Sequential()
        # In: 28 * 28 * 1, depth = 1
        # Out: 14 * 14 * 64, depth = 64

        input_shape = (self.img_cols,self.img_rows,self.img_channel)
        for i in range(cnn_layers_num):
            if i == 0:
                self.D.add(Conv2D(depth*2**0,5,strides=2,padding='same',activation=LeakyReLU(alpha=0.2),
                                  input_shape=input_shape))
            else:
                self.D.add(Conv2D(depth * 2 ** 0, 5, strides=2, padding='same', activation=LeakyReLU(alpha=0.2)))

            self.D.add(Dropout(dropout))

        self.D.add(Flatten())
        self.D.add(Dense(1))
        self.D.add(Activation('sigmoid'))
        self.D.summary()
        return self.D
```

# 生成网络

生成网络则是为了生成虚假的图片的。在下图里，虚假的图片会从一个100维的噪声中生成（噪声均部于-1.0至1.0之间）。这里我们使用了一个对卷积求逆的操作，也称为反卷积（需要反卷积的情况通常发生在用户想要对一个普通卷积的结果做反方向的变换。例如，将具有该卷积层输出shape的tensor转换为具有该卷积层输入shape的tensor。同时保留与卷积层兼容的连接模式）。不同于在DCGAN之中分别步长求卷积，因为生成网络需要生成更加符合实际情况的手写图片，所以在前三层之中上采样都被使用。在每层网络之间，样本规范也被使用来使得学习变得稳定。每个层的激活函数就是Relu。最终激活函数sigmoid的输出就是虚假的图片。最开始的Dropout层的断开率取在0.3到0.5之间。

{% asset_img GANgenerator.png 生成网络 %}


```python
    def generator(self,momentum=0.9):
        if self.G:
            return self.G
        self.G = Sequential()
        dropout = 0.4
        depth = 64 * 4
        dim = 7
        # In: 100
        # Out: dim x dim x depth
        self.G.add(Dense(dim * dim * depth, input_dim=100))
        self.G.add(BatchNormalization(momentum=momentum))
        self.G.add(Activation('relu'))
        self.G.add(Reshape((dim, dim, depth)))
        self.G.add(Dropout(dropout))

        for i in range(3):
            self.G.add(UpSampling2D())
            self.G.add(Conv2DTranspose(int(depth / 2**(i+1)), 5, padding='same'))
            self.G.add(BatchNormalization(momentum=0.9))
            self.G.add(Activation('relu'))

        # Out: 28 * 28 * 1
        self.G.add(Conv2DTranspose(1,5,padding='same'))
        self.G.add(Activation('sigmoid'))
        self.G.summary()
        return self.G
```

# GAN模型

到现在为止，我们还没有生成模型。那么现在我们就动手构建训练用的模型吧。我们需要辨别和生成模型。

## 辨别模型

下面就显示了如何生成辨别模型的keras代码。由于我们使用了sigmoid作为激活函数，所以我们使用了**对数损失**作为损失函数。**RMSProp**作为优化器比起Adam来说能生成更实际的虚假图像。这里的学习率是**0.0008**。权重的decay和梯度的削减将会在接下来的训练中使得学习过程变得稳定化。decay需要随着调整学习率进行相应的调整。

```python
    def discriminator_model(self):
        if self.DM:
            return self.DM
        optimizer = RMSprop(lr=0.0002, decay=6e-8, clipvalue=1.0)
        self.DM = Sequential()
        self.DM.add(self.discriminator())
        self.DM.compile(loss='binary_crossentropy', optimizer=optimizer, \
                        metrics=['accuracy'])
        return self.DM
```

## 对抗模型

对抗网络就像是生成网络和辨别网络铺垫如图所示。生成器尽力去欺骗辨别器并且同时习得反馈的内容。其他的部分和辨别模型一致，只不过减小了学习率和对应的权重的decay。

```python
    def adversarial_model(self):
        if self.AM:
            return self.AM
        optimizer = RMSprop(lr=0.0001, decay=3e-8, clipvalue =1.0)
        self.AM = Sequential()
        self.AM.add(self.generator())
        self.AM.add(self.discriminator())
        self.AM.compile(loss='binary_crossentropy', optimizer=optimizer,metrics=['accuracy'])
        return self.AM
```

{% asset_img GANadversarialmodel.png 对抗模型 %}

# 训练

**对抗生成网络的训练强烈建议在较强的GPU下进行！**

训练就是最困难的部分了。我们需要先确定辨别器是否能够单独辨别真实以及虚假的图片。接下来，辨别器和对抗网络一个接着一个的训练。图片也显示了这个过程。

{% asset_img GANtraining.png 训练 %}

在训练的过程中固定一方，更新另一方的网络权重，交替迭代，在这个过程中，双方都极力优化自己的网络，从而形成竞争对抗，直到双方达到一个动态的平衡（纳什均衡），此时生成模型 G 恢复了训练数据的分布（造出了和真实数据一模一样的样本），判别模型再也判别不出来结果，准确率为 50%，约等于乱猜。

当固定生成网络 G 的时候，对于判别网络 D 的优化，可以这样理解：输入来自于真实数据，D 优化网络结构使自己输出 1，输入来自于生成数据，D 优化网络结构使自己输出 0；当固定判别网络 D 的时候，G 优化自己的网络使自己输出尽可能和真实数据一样的样本，并且使得生成的样本经过 D 的判别之后，D 输出高概率。

```python
            images_train = self.x_train[np.random.randint(0,\
                self.x_train.shape[0], size=batch_size), :, :, :]
            noise = np.random.uniform(-1.0, 1.0, size=[batch_size, 100])
            images_fake = self.generator.predict(noise)
            x = np.concatenate((images_train, images_fake))
            y = np.ones([2*batch_size, 1])
            y[batch_size:, :] = 0
            d_loss = self.discriminator.train_on_batch(x, y)

            y = np.ones([batch_size, 1])
            noise = np.random.uniform(-1.0, 1.0, size=[batch_size, 100])
            a_loss = self.adversarial.train_on_batch(noise, y)
```

由于其深度，训练一个GAN模型需要很大的耐心，下面有些需要注意的事宜：

| 问题 | 方法 |
| ---- | ---- |
| 生成一个类似于噪声的图像 | 在辨别器和生成器上使用dropout层，比较低的随机断开率（0.3-0.6之间）就会生成一个比较真实的图像 |
| 辨别器的损失很快的收敛到0使得生成器无法学习|不要预先训练辨别器，而需要使得它的学习率大于对抗网络的学习率。使用一个不同的训练噪声的样本 |
|生成的图像还是很像噪声| 检查激活函数，样本规范层以及随机断开层是否正确的应用于正确的序列之中|
|如何获得正确的训练/模型参数|先开始选用一些从论文中已知的结果。在训练2000或更多步之后，每隔500或者1000步之后观察参数的结果|

代码参考：[https://github.com/roatienza/Deep-Learning-Experiments/blob/master/Experiments/Tensorflow/GAN/dcgan_mnist.py](https://github.com/roatienza/Deep-Learning-Experiments/blob/master/Experiments/Tensorflow/GAN/dcgan_mnist.py)

# 样本的输出

下图显示了输出图形的进化，后面的图形已经非常完美了。

{% asset_img GANsampleresult.png 对抗生成网络的结果 %}

# 常见问题

有人反应在1000步之后的图像不甚理想，如下面所示。

{% asset_img GANQA1.png 结果1 %}

{% asset_img GANQA2.png 结果2 %}

这是因为GAN对于参数的初始化非常的敏感，这也就是为什么GAN很难应用的原因。参数的参数化在不同的CPU上有不一样的方法。

# 如何生成视频呢？

论文见下[https://arxiv.org/abs/1609.02612](https://arxiv.org/abs/1609.02612)

# 特殊的技巧

请见博文Wasserstein GAN，里面介绍了如何克服GAN难训练的原因以及解决方法

# 参考来源

> + [https://medium.com/towards-data-science/gan-by-example-using-keras-on-tensorflow-backend-1a6d515a60d0](https://medium.com/towards-data-science/gan-by-example-using-keras-on-tensorflow-backend-1a6d515a60d0)
> + [http://www.cnblogs.com/Charles-Wan/p/6238033.html](http://www.cnblogs.com/Charles-Wan/p/6238033.html)