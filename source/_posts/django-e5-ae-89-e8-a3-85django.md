---
title: '[Django]安装Django'
tags:
  - Django
  - Python
  - 网页
id: 823
categories:
  - Python
  - 网页
date: 2016-01-13 01:44:46
---

# 1 安装Python

由于Django由Python写成，所以需要首先使用Python。由于Python 2.x和3.x的原因，所以Django对不同版本的Python的兼容性或者适用性存在偏差。

下面是Python和Django的对应关系：
<table style="width: 575px; height: 122px;" border="0" width="469" cellspacing="0" cellpadding="0"><colgroup> <col style="mso-width-source: userset; mso-width-alt: 4096; width: 96pt;" width="128" /> <col style="mso-width-source: userset; mso-width-alt: 10912; width: 256pt;" width="341" /> </colgroup><tbody><tr style="height: 16.5pt;"><td class="xl63" style="height: 16.5pt; width: 96pt;" width="128" height="22">Django 版本</td><td class="xl63" style="width: 256pt;" width="341">Python版本</td></tr><tr style="height: 16.5pt;"><td class="xl63" style="height: 16.5pt;" align="right" height="22">1.7</td><td class="xl63">2.7 and 3.2, 3.3, 3.4</td></tr><tr style="height: 15.0pt;"><td class="xl64" style="height: 15.0pt;" align="right" height="20">1.8</td><td class="xl64">2.7 and 3.2 (until the end of 2016), 3.3, 3.4, 3.5</td></tr><tr style="height: 16.5pt;"><td class="xl63" style="height: 16.5pt;" align="right" height="22">1.9</td><td class="xl63">2.7, 3.4, 3.5</td></tr></tbody></table>

对于每个版本的Python，只有最近的发行版本才能得到官方支持，在[Python Download Page](https://www.python.org/downloads/)上可以获得Python的最新版本。Django对于Python的支持将会到Python安全维护的全周期内。比如Python 3.3 的安全支持在2017年9月终止，Django 1.8LTS（长期支持版）的安全检查会在2018年4月终止，因此Django 1.8也是最后一个支持Python 3.3的Django。

在Django 1.6之前，Python 3.x系列被公认为十分稳定的版本，在生产环境中其能够得到信任的。由于更新Python版本提供了更多的特性，所以应该使用更新的Python 2.x和3.x系列。第三方应用能够自由的选择他们的依赖项。

而对于windows操作系统，需要下载MSI installer for windows，完成之后按照窗口导引就能完成安装了。

在安装完成之后，需要检查Python是否存在在环境变量Path之中。首先打开命令行，通过`python --version`检查环境变量是否被正确的设定了，如果没有，需要保证python的python可执行文件和script文件夹被正确的包含在内。例如，python 2.7安装路径位于C:\python27\，那么C:\python27\和<span style="line-height: 22.8571px;">C:\python27\Script\都需要包含在环境变量里</span>

## 2 安装Apache和mod_wsgi

由于django自带了一个轻量级的服务器，所以在仅需要测试的时候，是不必要安装Apache服务器的，但是在实际的应用环境（比如接受较大并发的访问的时候）之中的时候，安装Apache和mod_wsgi是十分必要的。

mod_wsgi主要分为两个模式：嵌入式和守护式。在嵌入式之中，mod_wsgi和mod_perl十分相似，其把Python嵌入到Apache之中，当服务器开启的时候，它将会从内存之中加载Python代码，这样使得Python代码存活在Apache服务器运行的全周期之内，这也使得其性能高于其他服务器部署方式。而对于守护式而言，mod_wsgi会创建一个独立的守护进程来处理访客的请求，这样也使得其安全性得到了提升。在需要重新部署代码的时候，不需要重启整个Apache服务器，这样使得代码部署和实际应用之间无缝衔接。具体怎么部署还是需要参考mod_wsgi的文档。

确保Apache服务器被正常开启，mod_wsgi服务得以激活，Django就会运行在任何一个版本的支持mod_wsgi的Apache服务器之上。

[官方FAQ](https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/modwsgi/)上介绍了如何配置mod_wsgi的方法，鉴于篇幅所限，不在这里介绍了。

当然Django也支持其他的部署方式，例如在nginx上的uWSGI运行Django也非常好。Django遵循着wsgi说明书（即[PEP3333](https://www.python.org/dev/peps/pep-3333/)，Python的网络服务器网关接口），这样也使得其能够运行在一系列的服务器上。

# 3 安装数据库

如果你打算使用数据库来承载内容的话，你必须确保数据库服务正在运行，Django在官方上支持PostgreSQL，MySQL，ORACLE和SQLite。如果你开发的工程较为简单，那么SQLite是足够应付的了，但是由于SQLite还是和其他数据库具有很大的差异，所以在实际环境之中，数据库还是保持统一会比较好。

对于官方版本，需要确保与数据库的链接被正确安装了：

*   <span style="font-family: 'Microsoft YaHei', 微软雅黑, Raleway, sans-serif; line-height: 22.8571px;">PostgreSQL需要使用</span><span style="font-family: 'Microsoft YaHei', 微软雅黑, Raleway, sans-serif;"><span style="line-height: 22.8571px;"> [psycopg2](http://initd.org/psycopg/) 包，在[PostgreSQL notes ](https://docs.djangoproject.com/en/1.8/ref/databases/#postgresql-notes)</span></span><span style="font-family: 'Microsoft YaHei', 微软雅黑, Raleway, sans-serif;"><span style="line-height: 22.8571px;">之中也能得到详尽的帮助</span></span>
*   MySQL需要一个数据库API驱动器，比如mysqlclient，在[notes for MySQL backend](https://docs.djangoproject.com/en/1.8/ref/databases/#mysql-notes)里可以获得详细信息
*   SQLite可以在[SQLite backend notes](https://docs.djangoproject.com/en/1.8/ref/databases/#sqlite-notes)里得到帮助
*   Oracle需要一份cx_Oracle的备份，但是还是需要在[notes for the Oracle backend ](https://docs.djangoproject.com/en/1.8/ref/databases/#oracle-notes)获得对cx_Oracle和Oracle支持版本的信息

而对于官方并不支持的数据库，第三方应用也是可以使用的，比如：

*   <span style="line-height: 1.42857;">SAP SQL Anywhere</span>
*   <span style="line-height: 1.42857;">IBM DB2</span>
*   <span style="line-height: 1.42857;">Microsoft SQL Server</span>
*   <span style="line-height: 1.42857;">Firebird</span>
*   <span style="line-height: 1.42857;">ODBC</span>

这些数据库django版本和ORM特征差异较大，对于这些非官方的后台的具体功能以及任何支持查询，应直接使用第三方项目提供支持的渠道获得帮助。

Django的命令`manage.py migrate`可以自动创建数据库之中的表格，但是需要确保具有访问和修改数据库的权限，如果需要手动进行的话，也需要给予的`SELECT, INSERT, UPDATE 和 DELETE`权限。当选用Django的测试框架去测试查询Django的时候，需要确保Django有创建test数据库的权限。

# 4 移除老版本的Django

当升级Django的版本的时候，首先需要卸载老版本的Django的。

如果你具有easy_install或者pip的话，更新Django的时候会自动执行卸载的过程的。

如果是没有以上两种工具，那么就需要手工在site-packages中删除django库的，可以通过以下命令在**Shell**命令行来取得其地址：
<pre class="lang:ps decode:true ">$ python -c "import sys; sys.path = sys.path[1:]; import django; print(django.__path__)"</pre>

# 5 安装Django代码

安装Django的方法与你所选择的Django有差异。

### pip安装官方发行版：

1.  <span style="line-height: 1.1;">安装pip。最简单的办法就是安装[独立的pip安装器 ](http://www.pip-installer.org/en/latest/installing.html#install-pip)，如果你已经安装了pip，需要确保其还能跟得上时代的潮流</span>
2.  [virtualenv](http://www.virtualenv.org/)和[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)提供了一个隔离的Python环境，这样也使得不比在系统层面上安装那么多库文件，其也支持在没有管理员权限的情况下安装Django，[这里](https://docs.djangoproject.com/en/1.8/intro/contributing/)就有如何在Python3上安装Django的方法。
3.  当完成了环境的创建和激活之后，就可以使用`pip install Django`来在Shell命令行之中安装Django了

### 安装特殊发行版

在[这里](https://docs.djangoproject.com/en/1.8/misc/distributions/)检查一下你的系统是否有特殊发行版，通常特殊发行版能够自动安装依赖和更新路径，但是往往极少含有最新的Django

### 安装开发版本

安装开发版本就需要关注[开发门径](https://code.djangoproject.com/timeline)了，你需要注意[即将到来的发行版](https://docs.djangoproject.com/en/1.8/releases/#development-release-notes)。对于每个稳定版本，任何改变都会在文档中予以标识。

如果你想得到最新的Django代码以求最新的BUG修正和代码优化，需要执行以下几步：

1.  确保Git安装完成，并且能够在Shell命令行中调用`git help`
2.  检出Django的一个主要版本，例如使用这个命令：<span class="trim-code-tag:false mixed:false lang:default decode:true  crayon-inline ">$ git clone git://github.com/django/django.git</span> ，然后再本地目录里就会出现Django文件夹
3.  确保Python能够正确的加载代码，最为稳妥的办法就是使用[virtualenv](http://www.virtualenv.org/)<span style="line-height: 22.8571px;">、</span>[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)和[pip](http://www.pip-installer.org/)
4.  当安装并且激活[virtualenv](http://www.virtualenv.org/)之后需要运行命令：<span style="color: #c7254e; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 14.4px; line-height: 20.5714px; white-space: nowrap; background-color: #f9f2f4;">pip install -e Django</span>，这样也会使得django-admin被正确执行

当需要获取最新的Django的时候，运行命令<span style="color: #c7254e; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 14.4px; line-height: 20.5714px; white-space: nowrap; background-color: #f9f2f4;">git pull</span><span style="line-height: 1.42857;"> 即可，git会自动完成各种更新的。</span>

# windows环境下的BUG

*   如果django-admin只显示帮助文本而不接受参数的话，这样很有可能是文件和Windows的关联出了问题，检查是否有多个script在环境变量之中，这往往是多个版本的Python安装所导致的
*   在使用代理采用pip或者easy_install安装的时候，需要在命令行之中配置代理，例如：<pre class="lang:ps decode:true">set http_proxy=http://username:password@proxyserver:proxyport
set https_proxy=https://username:password@proxyserver:proxyport</pre>