---
title: bcrypt的使用方法
tags:
  - bcrypt
  - 密码
  - 网页
id: 1417
categories:
  - 网页
date: 2016-11-28 00:29:32
---

# 前言

还是因为倒腾lab.npuacm.info，看了网上的一些关于密码存储的报道，再加上我之前开发Django的经验，我选择bcrypt作为加密密码的方法。

bcrypt作为一种非常有力的加密手法。它的口令必须是8至56个字符，并将在内部被转化为448位的密钥。然而，所提供的所有字符都具有十分重要的意义。密码越强大，您的数据就越安全。

# 安装

最简单的还是使用pip了：

<pre class="lang:default decode:true ">$ pip install bcrypt</pre>

# 用法

哈希然后检查这个值是否正确很简单：

<pre class="lang:python decode:true ">import bcrypt
password = b"super secret password"
# Hash a password for the first time, with a randomly-generated salt
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# Check that a unhashed password matches one that has previously been
#   hashed
if bcrypt.hashpw(password, hashed) == hashed:
     print("It Matches!")
else:
     print("It Does not Match :(")</pre>

# 可调节的工作轮次

bcrypt的特性之一是可调的工作轮次。调节这个轮次，你只需要传入round的参数就可以了。`bcrypt.gensalt(rounds=12)` 默认的就是12

<pre class="lang:python decode:true ">import bcrypt
password = b"super secret password"
# Hash a password for the first time, with a certain number of rounds
hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
# Check that a unhashed password matches one that has previously been
#   hashed
if bcrypt.hashpw(password, hashed) == hashed:
    print("It Matches!")
else:
    print("It Does not Match :(")</pre>

# 可调节的前缀

你也可以调整bcrypt的前缀来决定其会兼容谁，你可以传递2a或者2b（默认值）来决定。

<pre class="lang:python decode:true ">bcrypt.gensalt(prefix=b"2b") </pre>

# 兼容的版本

其可以运行于Python2.6+、3.2+以及PyPy之上。