---
title: '[ACM][PC^2]PC^2手册'
tags:
  - PC^2
id: 166
categories:
  - 算法
date: 2015-04-11 16:21:43
---

    首先，本参考完全来自SSSSky，发布者不享有任何版权，如有侵权，请留言，我将以最快的速度删除之。
 

    PC2操作手册：
 

1.  配置pc2v9.ini文件
 

    在主服务器上的pc2v9.ini文件，写成以下内容：
 
```default
[client]

server=localhost:50002
```


其中50002为pc2网络进程的端口号。
 

在客户端的pc2v9.ini文件，写成以下内容：
 
```default
[client]

server=192.168.0.100:50002
```


其中192.168.0.100为比赛服务器的IP地址
 

在写好pc2v9.ini文件后，将其拷贝至bin目录下。
 

二、在配置好pc2v9.ini文件以后，在服务器上需要做以下几件事情：
 

1、打开pc2server，用户名和密码均默认为site1（在默认情况下，除了admin以外，所    有的用户名和密码均为账户类型+数字编号）。
 

在进入pc2server后需要设置比赛密码，之后不要关闭pc2server，执行以下步骤
 

2、打开pc2admin，默认账户为root，密码为administrator1
 

    2.1、在Accounts标签下，选中root（即administrator1)账户，点击下方的edit，修改root的密码
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC21.png)
 

    2.2、点击下方的Generate，生成需要的各种账户（暂不考虑账户名和密码）
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC22.png)
 

如果有需要的话，可以在Edit中给各个账户设置各种权限
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC23.png)
 

    2.3、在Languages标签下，点击Add，添加比赛用的语言。
 

注意：在评测之前，请检查是否将C,C++编译器的bin目录添加入评测机的环境变量，否则在评测时会报错，检查方法：
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC24.png)
 

显示如图即正常。
 

    2.4、在Problem标签下，点击Add，添加题目
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC25.png)
 

在Input Data File下 点击Browse，添加题目的输入数据文件。
 

在Answer File下，添加题目的输出数据文件。
 

然后转至Judging type标签，配置如图 如果需要把初步判题的结果（Auto judge的结果）返回给参赛队伍，就勾选Send Pre.....项
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC26.png)
 

再转至Validator标签，配置如图，如果不设置Validator，则judge账户无法自动判此题
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC27.png)
 

    2.5、在Auto Judge标签下，设置每个judge自动判哪题
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC28.png)
 

    2.6、在Times标签下设置服务器上比赛的时间
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC29.png)
 

设置好后，点击下方的start开启比赛。
 

开启比赛后，请一定注意保证服务器不会出问题（上次校赛因为服务器中途自动重启，导致最后需要加时）
 

2.  在一台比赛机上打开pc2team，输入一个team账户和密码，测试网络是否连通。如提示无法连接server，检查pc2v9.ini文件和网络连通问题。
 
3.  打开评测机，打开pc2judge
 

            2.4.1、如果开启了auto judge，pc2会自动判归属于该judge的题（在上面auto judge步骤中设置)，裁判需要做的是在New Runs标签下，选择某个提交，点击下方的Request Run
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC210.png)
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC211.png)
 

针对情况选择接受auto judge的判断或者选择一种judgement 判断此次提交并将结果返回给参赛队伍。（选手接收到的信息如下图：）
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC212.png)
 

    2.4.2、裁判还负有回答选手提问的责任：
 

在New Clars标签下，会看到选手针对某个问题的提问，选择某个提问，可以对该提问进行回答
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC213.png)
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC214.png)
 

    2.5、打开pc2board
 

    2.6、将bin目录下html目录下的榜单导出
 

4.  关于账户文件导入：
 

    pc2支持用文件导入账户数据，前提是已经生成了足够的账户（也就是说导入的账户数据是对已经生成的账户的覆盖）。
 

只需写一个txt文件按如下格式
 

![](/wp-content/uploads/2015/04/041115_0820_ACMPC2PC215.png)
 

其中site表示该账户所在的服务器
 

account为唯一账户号（也是对原账户覆盖操作的依据）
 

displayname为此账户在榜单上显示的名字
 

password 密码
 

permdisplay 是否允许此账户出现在榜单上
 

<tab> 键盘上的tab键
 

注意，文件请保存成ansi格式，这样虽然会造成在pc2board中显示乱码，但是在board生成的html文件中仍为正常中文
 

然后在pc2admin中Account标签下点击load，找到该文件即可
 