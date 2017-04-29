---
title: '解决Python安装包时候的error: Unable to find vcvarsall.bat问题'
tags:
  - Python
id: 1458
categories:
  - Python
date: 2017-01-23 07:13:38
---

# 前言

现在Windows开发Python，需要装一个名为`hcluster`的包，然后就开始报[error: Unable to find vcvarsall.bat](http://stackoverflow.com/questions/2817869/error-unable-to-find-vcvarsall-bat)的错误。stackoverflow上面已经讲的很清楚了，所以这就只是一个翻译贴了。

# 安装Microsoft Visual C++ Compiler for Python 2.7

地址在这里：[http://www.microsoft.com/en-us/download/details.aspx?id=44266](http://www.microsoft.com/en-us/download/details.aspx?id=44266)

这样你就直接运行就可以了。需要注意的事情，你必须合理的设置环境变量的值以确保其能正常使用。

按照这样来说也应该没问题了，但是很不幸的，也可能出差错。

注意，在正常情况下，你需要避免下项发生。

# 配置Visual Studio的环境变量

在使用setup.py安装程序包时，Python 2.7就会搜索已安装的Visual Studio。所以假设你已经安装了VS，那么在上述情况不成功的时候，你还需要在运行python setup.py install的之前，需要设定临时的环境变量。

设置的环境变量应该与你的VS版本有关。

*   Visual Studio 2010 (VS10): `SET VS90COMNTOOLS=%VS100COMNTOOLS%`
*   Visual Studio 2012 (VS11): `SET VS90COMNTOOLS=%VS110COMNTOOLS%`
*   Visual Studio 2013 (VS12): `SET VS90COMNTOOLS=%VS120COMNTOOLS%`
*   Visual Studio 2015 (VS14): `SET VS90COMNTOOLS=%VS140COMNTOOLS%`

# 后记

更多的答案，你可以直接查阅[StackOverFlow](http://stackoverflow.com/questions/2817869/error-unable-to-find-vcvarsall-bat)关于这个问题的答案。

&nbsp;