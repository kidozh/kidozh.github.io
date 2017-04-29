---
title: 用git部署网站代码到生产环境VPS
tags:
  - git
  - VPS
  - 网页
id: 1480
categories:
  - 未分类
date: 2017-04-05 19:28:27
---

# 前言

之前开发网页的时候，经常要把代码传到自己的VPS上，平常用FTP传整个代码很慢，所以就像到了用Git push到VPS上。

# 创建仓库

&nbsp;

<pre class="lang:sh decode:true ">cd /var
mkdir git &amp;&amp; cd git
mkdir your_site.git &amp;&amp; cd your_site.git
git init --bare</pre>

`--bare`的意思是，该文件夹是我们的代码仓库，它将不会放源代码而只是做版本控制。

## Hook钩子

我们将会使用`post-receive`钩子

<pre class="lang:sh decode:true ">ls</pre>

你可以看到有hooks文件夹已经为我们创建好了,而且里面也有各种钩子的样例

<pre class="lang:sh decode:true ">cd hooks</pre>

创建我们自己的`post-receive`

<pre class="lang:sh decode:true ">vim post-receive</pre>

输入下面的命令到这个文件之中：

<pre class="lang:sh decode:true ">#!/bin/sh
git --work-tree=生产环境网站文件夹位置 --git-dir=/var/git/your_site.git checkout -f</pre>

`git-dir`指的是仓库的地址， `work-tree`则是存放代码的位置，也就是我们的网站的源代码的位置。 接下来则是要保证它可以运行：

<pre class="lang:sh decode:true ">chmod +x post-receive</pre>

## 本地

一般情况是你已经有了自己的git项目了，那么只需要添加vps的仓库地址就行了

    git remote add myVPS-sitename ssh://user@mydomain.com/var/git/your_site.git`</pre>

    'myVPS-sitename'只是这个远程连接的名称，你可以同时有多个远程连接，每次push的时候指定名称即可将代码上传到不同的仓库。

    如果你本地还没有项目代码：

    <pre>`cd 项目地址
    git init`</pre>

    添加一个README.ME文件后

    <pre>`git add .
    git commit -m "项目初始"`</pre>

    接下来我们便可以将代码push到vps了：

    <pre>`git push myVPS-sitename master

`master`指定的是master分支，如果你有其他分支也可以push其他分支。.

## 总结

这只是最基本的设置，利用hook结合一些自己编写的脚本我们还可以做很多事情。