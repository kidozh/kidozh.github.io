---
title: '[MineCraft]Minecraft在虚拟云上建站'
tags:
  - minecraft
id: 876
categories:
  - 未分类
date: 2016-01-21 23:58:03
---

# 服务器申请

首先我们来获得一个服务器，目前国内比较成熟的是[腾讯云](http://www.qcloud.com/)和[阿里云](https://www.aliyun.com)，对于学生，他们都有不同的优惠。腾讯的最低配置是1元/月，阿里是10元/月。当然你也可以使用国外的VPS，DigitalOcean和linode，但是国外服务器可能访问缓慢以及结账较为麻烦，所以在这里我们可以使用阿里或者腾讯云。

![](/wp-content/uploads/2016/01/012116_1557_MineCraftMi1.png)

配置情况如下：

*   操作系统 CentOS 6.5 64位/Ubuntu 14.04 LTS 64位
*   CPU 1核
*   内存 1GB
*   系统盘 8GB(云硬盘)
*   数据盘 0GB
*   公网带宽 1Mbps

如果规模是5人的话，这个还是可以很好的运行的，如果你觉得有点延迟的话，升级带宽就可以啦。

# 配置服务器

首先，我们最好还是使用Linux服务器，因为会比较稳定，但是需要注意的是操作者最好能懂得一些基本的Shell命令行。

其次，这里我们必须配置服务器信息，你可以使用密码或者公钥来登陆，为了简便起见，这里我使用了密码登陆。

# 登录服务器

为了操作我们的服务器，我们需要使用Putty和xftp。

首先，为了使用命令行，在windows下我们可以使用putty，[这里](http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe)就有下载链接。由于我们还需要上传文件到服务器，我们也需要一个FTP工具，xftp，[这里](http://dx2.xiazaiba.com/Soft/X/Xftp_5.0.680.0_XiaZaiBa.zip)就有下载地址，我们可以使用个人/家庭版来免费使用这款软件。

会到服务器控制台，待到系统安装完毕之后，打开Putty，填入服务器公网：

![](/wp-content/uploads/2016/01/012116_1557_MineCraftMi2.png)

点击Open登陆，然后再弹出的窗口之中输入用户名root和密码。密码默认在Linux中不显示。

![](/wp-content/uploads/2016/01/012116_1557_MineCraftMi3.png)

首先需要更新系统，敲入命令：`yum -y update`

等待包更新完毕后，敲入命令：`yum -y upgrade`

然后就建立了基本服务器配置

# 建立MC服务器

首先我们需要安装Java环境。我的办法是本地下载Java的RPM安装包，然后通过xftp的SFTP连接并上传到服务器，然后在服务器端安装，这样速度会比较快一点。

打开Java的下载页面：[Java Download](http://www.java.com/zh_CN/download/manual.jsp)，然后选择我们的服务器系统对应版本。选择"Linux x64 RPM".

![](/wp-content/uploads/2016/01/012116_1557_MineCraftMi4.png)

下载完毕后，打开xftp软件，点击新建(New)，然后Host中填入你的公网IP，协议选择SFTP，在下边的登陆信息中填入你的用户名和密码。

![](/wp-content/uploads/2016/01/012116_1557_MineCraftMi5.png)

弹出的窗口选择第二个即可：接受并保存（Accept and Save）。在右边的窗口即可显示你的服务器中文件信息了，左边是你的计算机中的文件。

在右边的窗格，路径输入"/usr"，然后右键新建文件夹，名为"java",左边的窗格中找到下载好的RPM包，点击右键，选择传输（Transfer）即可。

![](/wp-content/uploads/2016/01/012116_1557_MineCraftMi6.png)

然后回到Putty，我们需要在服务器中安装Java以及一个工具：Screen。

首先我们在命令行中执行：`yum -y install screen`

![](/wp-content/uploads/2016/01/012116_1557_MineCraftMi7.png)
> GNU Screen是一款由GNU计划开发的用于命令行终端切换的自由软件。用户可以通过该软件同时连接多个本地或远程的命令行会话，并在其间自由切换。> 常用Screen 命令：
> 
> *   <span style="line-height: 1.25;">· screen -S mc //新建一个叫mc的Screen</span>
> *   <span style="line-height: 1.25;">· screen -r mc //返回名为mc的Screen</span>
> *   <span style="line-height: 1.25;">· 键盘按Ctrl + A //退出刚创建的Screen</span>
> *   <span style="line-height: 1.25;">· screen -ls //显示所有的Screen</span>
> *   <span style="line-height: 1.25;">· exit //在Screen中使用可以关闭当前Screen会话</span>

更多资料参考：[linux screen 命令详解](http://www.cnblogs.com/mchina/archive/2013/01/30/2880680.html) By David Camp

安装完后，等到RPM上传成功之后，依次执行下列命令，用于安装Java环境：

`cd /usr/java`

`rpm -ivh jre- //此处按键盘的Tab键即可自动补全，你上传的文件名`

![](/wp-content/uploads/2016/01/012116_1557_MineCraftMi8.png)

上述操作执行完毕后，输入以下命令:

`java -version`

若提示如下，即说明已经Java环境已安装成功。

![](/wp-content/uploads/2016/01/012116_1557_MineCraftMi9.png)

然后我们需要修改Java的配置文件及环境变量，首先查看我们的Java文件夹的名字，在Putty中依次输入如下命令：

·`cd /usr/java`·

`ls –al`

![](/wp-content/uploads/2016/01/012116_1557_MineCraftMi10.png)

如图，我的文件夹名为：jre1.8.0_71，复制一下这个名字。

接下来依次执行下列命令（一次一行）：

`echo 'export JAVA_HOME=/usr/java/jre1.8.0_71' &gt;&gt; /etc/profile`

这句中的jre1.8.0_1即为刚才的名字。

`echo 'export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar'&gt;&gt; /etc/profile`

`echo 'export PATH=$PATH:$JAVA_HOME/bin' &gt;&gt; /etc/profile`

OK，至此Java环境已配置完毕。

# 下载MC服务器

这一步我简化了，我直接去MCBBS上下了一个简化版(主要是懒得配置MOD之间的关系了)，把文件上传即可。

![](/wp-content/uploads/2016/01/012116_1557_MineCraftMi11.png)

这里实际上我上传的地方是/home/mcServer

# 设置服务器端的文件

首先着上传的时间安装Screen。

趁首先创建个新的Screen，命名为mc，用于启动管理MC服务器：

`screen -S mc`

然后切换到mcserver目录：

`cd /home/mcServer`

解压zip文件到本目录：

`unzip mcserver.zip`

建立启动脚本文件：

`vim start.sh `

新建start.sh文件，弹出编辑器窗口，粘贴内容如下：
<pre>#!/bin/sh 
java -Xmx768M -Xms512M -jar /home/mcserver/minecraft_server.1.7.10.jar
</pre>

![](/wp-content/uploads/2016/01/012116_1557_MineCraftMi12.png)

其中的minecraft_server.1.7.10.jar为你的服务器文件，即当前目录下你上传的server.jar文件名。

执行命令，赋予脚本执行权限。

`chmod 777 start.sh`

# 启动MC服务器

首先还是要配置server.properties，这一点按照[mc wiki properties](http://minecraft-zh.gamepedia.com/Server.properties)上配置就可以了

Done~!

搭建完成，用下载好的MC1.7.10的客户端连接测试一下~

直接连接服务器，输入自己服务器的IP地址即可.

下次我们使用Putty连接服务器时，只要使用命令：

`screen -r mc`即可回到我们的MC服务器状态啦~

# 域名服务

这点和我们之前的架设博客很相似，当我们想隐藏我们的ip的时候就可以用这个了

只要通过A记录解析就可以了

![](/wp-content/uploads/2016/01/012116_1557_MineCraftMi13.png)

参考来源：[http://sintonblog.win/mc-build-2/](http://sintonblog.win/mc-build-2/)