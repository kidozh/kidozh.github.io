---
title: 解决Ubuntu下网易云音乐无法打开
date: 2018-10-21 14:37:07
tags: 
    - Ubuntu
    - 网易云音乐
---

> 来源： https://blog.jae.sh/article/w96dk0.html

# 背景

网易云音乐最近升级到了v1.1这个版本，但是自从我氪了一波音乐包之后，在Ubuntu下网易云音乐就打不开了，之前以为是江南皮革厂的梗，然后搜了之后才发现很多人有相似的问题，所以在这里介绍一下如何解决这个问题。

# 环境

+ Ubuntu 16.04 LTS + Unity
+ 网易云音乐 v1.1

# 问题描述

+ 无法使用图标启动
+ 在使用命令行`netease-cloud-music`启动的时候输出错误`Local file: "" ("netease-cloud-music")`
+ 当使用管理员权限运行的时候就可以正常开启

# 解决方法

1. 将`netease-cloud-music`二进制文件加入到`sudoer`组
    修改`/etc/sudoers`文件，追加一句话`YOURNAME ALL = NOPASSWD: /usr/bin/netease-cloud-music`,替换这句话中的`YOURNAME`为你登录的用户名，建议使用`sudo visudo`来编辑`/etc/sudoers`文件,防止出错。
2. 修改网易云音乐桌面快捷方式,加入`sudo`
    ```shell
    sudo vim /usr/share/applications/netease-cloud-music.desktop
    ```
    修改`Exec=netease-cloud-music %U`这行为`Exec=sudo netease-cloud-music %U`,加上`sudo`,这样点击网易云音乐图标就是以管理员权限启动的了，且不用输入密码。



