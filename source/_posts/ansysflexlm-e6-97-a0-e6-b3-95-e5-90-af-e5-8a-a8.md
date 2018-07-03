---
title: '[ANSYS]FLEXlm无法启动'
tags:
  - ANSYS
id: 951
categories:
  - 机械
date: 2016-03-29 17:41:56
---

# 前言

在我们使用ANSYS Workbench的时候，经常会碰到证书服务的鬼畜问题，尤其是安装了UG NX之后，这个问题更为严重，因为他们的证书文件往往会占用同一个端口，这样就导致两者不可兼得。这篇博客意在说明当这种情况发生的时候我们可以怎样操作来使得FLEXlm启动。

# 问题的来源

## license的问题

license里面server后面的hostname和物理地址一定要与电脑本身的匹配，也就是说物理地址一定要是本地连接下面的Physical address才行。如果你的电脑开了蓝牙，无线网等，都各自会有一个对应的physical address，但是默认生成的license会采用第一个，不管这个是不是本地连接下面的。所以在生成license后，一定亲自检查，如果不对，手动修改即可。查看物理地址命令：ipconfig/all。安装ansys，记住填写hostname的时候，一定填自己的计算机名（曾见过有人写的自己的名字），如果错了，在ansys client licensing 里面启动Client ANSLIC_ADMIN utility 修改即可。

## 中文路径

安装的时候必须英文路径（国外的软件，不管是什么软件，安装一般最好都采用英文路径）。

## 端口冲突

FLEXlm not running，很有可能就是端口冲突，这个以前发现过，有的软件就会互相冲突。解决办法：在dos界面下输入`netstat -a -o`

找到**1055**端口对应pid值，然后启动任务管理器，打开“查看-选项列”，勾选pid选项，找到pid值对应的映像名称，结束进程；打开打开Server ANSLIC_ADMIN Utility ， 点击stop the ANSYS,lnc.License Manager,再点击start the ANSYS,lnc.License Manager，看看FLEXlm是不是变成running了点击start the ANSYS,lnc.License Manager，看看FLEXlm是不是变成running了。这里由于UG的证书文件往往和这货端口号一致，所以经常鬼畜。。。