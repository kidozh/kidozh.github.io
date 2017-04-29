---
title: '[Python]使用国内的Python源加速pip'
tags:
  - pip
  - Python
id: 809
categories:
  - Python
date: 2016-01-09 17:53:01
---

Python下用的最多的包安装工具就是easy_install和pip，但是他们都是从Python官方的Pypi源上寻找并下载资源，由于国内网络原因，有时候连接和速度就不是那么理想，跟淘宝的RubyGems镜像源一样，于是便有了国内的PyPi镜像源，如今天说的豆瓣PyPi镜像。

豆瓣PyPi镜像：[http://pypi.douban.com/simple/](http://pypi.douban.com/simple/)

<span style="line-height: 32.64px;">使用方法：</span>
<pre class="lang:sh decode:true ">sudo easy_install -i http://pypi.douban.com/simple/ flask 
sudo pip install -i http://pypi.douban.com/simple/ flask</pre>

 <span style="color: #444444; font-family: 'Classic Grotesque W01', Arial, 'Hiragino Sans GB', STHeiti, 'Microsoft YaHei', 'WenQuanYi Micro Hei', SimSun, sans-serif; font-size: 17px; line-height: 32.64px;">要配制成默认的话，需要创建或修改配置文件（linux的文件在~/.pip/pip.conf，windows在%HOMEPATH%\pip\pip.ini），修改内容为：</span>
<pre class="lang:default highlight:0 decode:true">[global]
index-url = http://pypi.douban.com/simple</pre>

 <span style="color: #444444; font-family: 'Classic Grotesque W01', Arial, 'Hiragino Sans GB', STHeiti, 'Microsoft YaHei', 'WenQuanYi Micro Hei', SimSun, sans-serif; font-size: 17px; line-height: 32.64px;">然后用pip的时候自动就会用此镜像源了</span>

另附上一个阿里云的PyPi源：[http://mirrors.aliyun.com/pypi/simple/](http://mirrors.aliyun.com/pypi/simple/)