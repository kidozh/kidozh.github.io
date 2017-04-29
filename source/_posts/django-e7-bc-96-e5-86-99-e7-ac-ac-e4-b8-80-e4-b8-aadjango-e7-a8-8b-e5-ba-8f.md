---
title: '[Django]编写第一个Django程序'
tags:
  - Django
  - Python
  - 网页
id: 827
categories:
  - Python
  - 网页
date: 2016-01-13 15:57:24
---

# 1 前言

那么就从实例出发，开始编写我们的第一个Django程序。

这个Django程序主要由两部分组成：

*   一个公开的站点供人们投票以及观察投票结果
*   一个管理员站点能够自由的增加、删减或者改变投票的结果

注意了，由于本文参考的来自Django 1.8文档，所以其他版本的可能存在较大的偏差，需要谨慎看待。查看Django版本的办法：`$ python -c "import django; print(django.get_version())"`。同样的，Python版本也是2.7的，故对于Python3.x系列可能需要按照文本做出轻微的调整

# 2 创建一个工程

首先打开Shell命令行，进入一个需要创建Django工程的文件夹，使用以下命令：
<pre class="lang:sh decode:true">$ django-admin startproject mysite</pre>

 这样在正常安装的情况下就能够创建一个名为mysite的工程。

_需要注意的是，该工程不能和现有的Django以及测试工程重名，比如django或者test。而对于Django文件夹所在的位置，一般最好不要和网络服务器文件夹的根目录重合，因为这样有可能导致代码泄露。例如在Linux系统下就是`/var/www/`而在Windows下，就有比如`htdocs`这样的网关文件夹。_

Django命令创建的文件目录树如下：
<pre class="lang:default decode:true">mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py</pre>

 这些文件的功能有以下关系：

*   <span style="line-height: 1.42857;">根目录mysite只是一个承载Django工程的文件夹，这个名字对于Django来说并不重要，你可以任意对其重命名</span>
*   manage.py主要用于与Django工程发生交互，在[这里](https://docs.djangoproject.com/en/1.8/ref/django-admin/)也能看到Django和admin之间的关系
*   在mysite工程内的文件夹的mysite，其命名空间就是需要引入的python的包，比如mysite.urls
*   mysite/__init__.py:告诉Python解释器这是一个Python的一个库
*   mysite/setting.py：配置Django的各种选项
*   mysite/urls.py：对于URL的一个声明
*   mysite/wsgi.py：一个为WSGI兼容的网络服务器提供的一个入口

# 3 设定选项

打开setting.py，这是一个正常的Python模块显示Django的设定项。

对于只想调试的人，SQLite这种轻量级的数据库是非常优秀的，你不需要安装任何东西就能使用了。但是在实际应用之中，更为稳定的PostgreSQL，也是非常合适的。

如果需要安装其他的数据库的话，首先需要安装数据库的一个链接，然后修改DATABASES中的default去设定数据库连接。

*   ENGINE：对于数据库连接后台，在上篇文章里就介绍了：'django.db.backends.sqlite3', 'django.db.backends.postgresql_psycopg2', 'django.db.backends.mysql',和'django.db.backends.oracle'都是可以得，其他数据库需要点击[这里](https://docs.djangoproject.com/en/1.8/ref/databases/#third-party-notes)
*   NAME：数据库的名称，当时用SQLite的时候是安装到里面的文件，这个时候NAME就必须使用绝对路径来指明地点，默认值是 `os.path.join(BASE_DIR, 'db.sqlite3')`，将会当必要的时候SQLite就会存储在工程文件夹里。
*   当不使用SQLite的时候，账号（USER），密码（PASSWORD），端口（HOST）必须被添加，同时也必须创建一个数据库，可以使用<span class="lang:plsql decode:true crayon-inline">CREATE DATABASE database_name;</span>来创建一个数据库

当设定setting.py的时候，也需要设定时区`TIME_ZONE`到目前计算机的时区。同时需要注意的是`INSTALLED_APP`指示了Django中所有活动的实例，应用可以在多个库中或者其他文件中进行调用。

同时也介绍一下其他的默认的应用：

*   django.contrib.admin – 管理员站点
*   django.contrib.auth – 认证系统
*   django.contrib.contenttypes – 目录类型的一个框架
*   django.contrib.sessions – 回话控制
*   django.contrib.messages – 信息框架
*   django.contrib.staticfiles –静态文件管理框架

由于这些应用都会创建数据库，所以需要使用以下命令来自动创建数据库：
<pre class="lang:sh decode:true">$ python manage.py migrate</pre>

 migrate命令会按照setting.py中的设定创建一些必要的数据库，你可以键入<span class="lang:plsql decode:true  crayon-inline "> \dt (PostgreSQL)</span> ,

<span class="lang:plsql decode:true crayon-inline">SHOW TABLES;</span>(MySQL), <span class="lang:scheme decode:true  crayon-inline ">.schema</span>  (SQLite), 或者<span class="lang:plsql decode:true crayon-inline crayon-selected">SELECT TABLE_NAME FROM USER_TABLES;</span>(Oracle)来显示Django所创建的表。

# 4 服务器开发

cd到外层的mysite文件夹（工程文件根目录），就可以<span class="lang:default decode:true  crayon-inline ">$ python manage.py runserver</span> 使用来启动django的服务器了。

在命令行里面就会输出信息：
<pre class="lang:default decode:true">Performing system checks...

0 errors found
January 12, 2016 - 15:50:53
Django version 1.8, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.</pre>

 这样就启动了一个纯粹由Python编写的轻量级服务器了，除非是真的需要部署到生产环境之中，否则我们在不使用Apache的情况下是可以直接调试我们的Django程序的。在生产环境之中还是乖乖使用Apache服务器吧，否则带不起来的。

注意到输出信息里已经给出了网址http://127.0.0.1:8000/，我们只要访问就可以看到我们的Django网页了，在没有部署任何应用的情况下，你应该会看到一个淡蓝色的欢迎页，这样就调试成功了。

如果你需要改变端口号的话，还是通过命令后加一个端口的参数<span class="lang:ps decode:true  crayon-inline ">$ python manage.py runserver 8080</span> 来实现，这样就能开启8080，如果你同样需要改变IPv4的IP地址的话，也是同样的道理，补全即可。<span class="lang:ps decode:true  crayon-inline ">$ python manage.py runserver 0.0.0.0:8000</span> ，更为详尽的改变的办法请参考官方文档：[https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-runserver](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-runserver)

# 5 创建模型

每个Django之中的应用是由多个python库组成的，而且可以保存在任何一个地方，但是保存在工程文件下在引用的时候是非常优雅的，当然，你可以使用命令<span class="lang:sh decode:true  crayon-inline ">$ python manage.py startapp polls</span> 来创建一个新的应用。

这样他的文件的布局就是这样了
<pre class="lang:default decode:true">polls/
    __init__.py
    admin.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py</pre>

 在开始一个带有数据库的Django应用的第一步就是创建模型（主要是数据布局和元数据构成）。一个好的模型应该是唯一且精准的数据来源，其必须包含数据形式和操作行为。

在我们的这个应用之中，我们会创建两个模型：问题和选择。问题模型包含问题和一个时间。而选择模型包含选择内容和一个单位，每个选择都和一个问题相关联。

所以在polls/models.py中应该这样写模型：
<pre class="lang:python decode:true" title="polls/models.py">from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)</pre>

 每个模型都是由django.db.models.Model这个子类所代表，每个模型都有一系列的变量，其代表着模型中所对应的数据库的字段。

每个字段都由Django中的一个实例组成，比如CharField是针对字符串类型的，而DateTimeField是针对日期时间类型，而每一个字段的名字就是他们在数据库之中的名字，在Python之中其作为变量名，而在数据库之中其又作为字段名。

而一些字段名是需要特定的参数的，比如CharField就需要最大字符数。这个参数不仅被用于数据库中的语法，而且也能被用于验证模块之中。当然，字段也具有各种各样的参数，例如我们就设定了votes的默认值是0.

最后，对于关系型数据库，当时用ForeignKey的时候，这也意味这关系被确立，即一种选择对应一个问题，Django支持所有的常用的数据库关系：多对一，多对多和一对一。

# 6 激活模型

使用很少的代码就能让Django具备以下的特性：

*   为应用创建一个表
*   为应用创建一个Python的数据库应用接口来获取数据

继续编辑setting.py文件夹，在INSTALLED_APP中加入polls，所以会变成这样：
<pre class="lang:python decode:true" title="mysite/settings.py">INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
)</pre>

 这样Django就加入polls到应用之中了，所以在使用migrate命令的时候，Django就会为其创建对应的表了。
<pre class="lang:sh decode:true">$ python manage.py makemigrations polls</pre>

 那么输出信息中就可以看到有关这次表新建的内容了。
<pre class="lang:default decode:true">Migrations for 'polls':
  0001_initial.py:
    - Create model Question
    - Create model Choice
    - Add field question to choice</pre>

 通过makemigrations就可以让Django检测模型的改变并且这些改变就能被作为一个migrate储存了。

迁徙（migration）就是Django如何去变更你的模型的在硬盘上的文件。当你创建一个新的模型的时候，你可以随心所欲的观察迁徙，他们会被储存在比如<span style="color: #0c4b33; font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-size: 14px; font-weight: bold; line-height: 21px;">polls/migrations/0001_initial.py</span><span style="line-height: 1.42857;">这样的文件之中，但是我们也不必每次都花费时间去观察。</span>

当然了，migrate这个命令是更常见的被用于自动更新数据库的命令了，但是也许我们还是先看一下migrate的原理吧。使用<span style="color: #0c3c26; font-family: Roboto, Corbel, Avenir, 'Lucida Grande', 'Lucida Sans', sans-serif; font-size: 14px; line-height: 21px;"> </span><tt class="xref std std-djadmin docutils literal" style="color: #0c4b33; -webkit-tap-highlight-color: transparent; border-bottom-width: 1px; border-bottom-style: dotted; border-color: #971414; font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-size: 1em; line-height: 21px; font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed; font-weight: bold; background-color: #ffffff;"><span class="pre" style="font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed;">[sqlmigrate](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-sqlmigrate)</span></tt><span style="line-height: 1.42857;">命令就能执行迁徙这个操作并且返回执行的SQL语句。</span>
<pre class="lang:plsql decode:true">BEGIN;
CREATE TABLE "polls_choice" (
    "id" serial NOT NULL PRIMARY KEY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL
);
CREATE TABLE "polls_question" (
    "id" serial NOT NULL PRIMARY KEY,
    "question_text" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
);
ALTER TABLE "polls_choice" ADD COLUMN "question_id" integer NOT NULL;
ALTER TABLE "polls_choice" ALTER COLUMN "question_id" DROP DEFAULT;
CREATE INDEX "polls_choice_7aa0f6ee" ON "polls_choice" ("question_id");
ALTER TABLE "polls_choice"
  ADD CONSTRAINT "polls_choice_question_id_246c99a640fbbd72_fk_polls_question_id"
    FOREIGN KEY ("question_id")
    REFERENCES "polls_question" ("id")
    DEFERRABLE INITIALLY DEFERRED;

COMMIT;</pre>

 但是我必须在这里说明一些事情：

*   输出的格式由你所选择的数据库所决定，上面的就是PostgreSQL生成的
*   表格的名字是由应用的名字和模型中类的名字的全小写采用下划线生成
*   主键会被自动添加
*   外围的键会精确地由<span class="pre" style="font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed; color: #0c4b33; font-size: 14px; font-weight: bold; line-height: 21px;">FOREIGN</span><span style="color: #0c4b33; font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-size: 14px; font-weight: bold; line-height: 21px;"> </span><span class="pre" style="font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed; color: #0c4b33; font-size: 14px; font-weight: bold; line-height: 21px;">KEY</span>约束所确立，而对于<span style="color: #0c3c26; font-family: Roboto, Corbel, Avenir, 'Lucida Grande', 'Lucida Sans', sans-serif; font-size: 14px; line-height: 21px;"> </span><tt class="docutils literal" style="font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed; color: #0c4b33; font-size: 14px; font-weight: bold; line-height: 21px;"><span class="pre" style="font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed;">DEFERRABLE</span></tt>，不必在意，其只是告诉PostgreSQL在事物之后才执行执行外围键这个操作
*   通常为了简洁起见，Django会在外围键添加_id的后缀
*   对于不同的数据库特殊类型我们应该为其量身定做类型，比如SQL中常见的自增<span style="color: #0c4b33; font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-size: 14px; font-weight: bold; line-height: 21px;">auto_increment</span>，PostgreSQL中的<span style="color: #0c4b33; font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-size: 14px; font-weight: bold; line-height: 21px;">serial</span>和SQLite之中的<span class="pre" style="font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed; color: #0c4b33; font-size: 14px; font-weight: bold; line-height: 21px;">integer</span><span style="color: #0c4b33; font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-size: 14px; font-weight: bold; line-height: 21px;"> </span><span class="pre" style="font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed; color: #0c4b33; font-size: 14px; font-weight: bold; line-height: 21px;">primary</span><span style="color: #0c4b33; font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-size: 14px; font-weight: bold; line-height: 21px;"> </span><span class="pre" style="font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed; color: #0c4b33; font-size: 14px; font-weight: bold; line-height: 21px;">key</span><span style="color: #0c4b33; font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-size: 14px; font-weight: bold; line-height: 21px;"> </span><span class="pre" style="font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed; color: #0c4b33; font-size: 14px; font-weight: bold; line-height: 21px;">autoincrement</span>
*   <span style="color: #0c3c26; font-family: Roboto, Corbel, Avenir, 'Lucida Grande', 'Lucida Sans', sans-serif; font-size: 14px; line-height: 21px;"> </span>[<tt class="xref std std-djadmin docutils literal" style="font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed; color: #0c4b33; font-size: 1em; font-weight: bold;"><span class="pre" style="font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed;">sqlmigrate</span></tt>](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-sqlmigrate)<span style="color: #0c3c26; font-family: Roboto, Corbel, Avenir, 'Lucida Grande', 'Lucida Sans', sans-serif; font-size: 14px; line-height: 21px;"> </span>并不会真正的去运行这个迁徙，他只是会把命令显示到屏幕之上去检查SQL语句

使用 <span style="color: #0c3c26; font-family: Roboto, Corbel, Avenir, 'Lucida Grande', 'Lucida Sans', sans-serif; font-size: 14px; line-height: 21px;"> </span><tt class="xref std std-djadmin docutils literal" style="color: #1d915c; -webkit-tap-highlight-color: transparent; outline: 0px; border-bottom-width: 1px; border-bottom-style: dotted; border-color: #971414; font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-size: 1em; line-height: 21px; font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed; font-weight: bold; background-color: #f1fff7;">[<span class="pre" style="font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed;">python</span> <span class="pre" style="font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed;">manage.py</span> <span class="pre" style="font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed;">check</span>](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-check)</tt><span style="line-height: 1.42857;"> 可以在不改变数据库结构的情况下检查工程中的SQL问题。</span>

接下来，运行migrate就可以创建模型表了。
<pre class="lang:default decode:true">$ python manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, contenttypes, polls, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying &lt;migration name&gt;... OK</pre>

 migrate命令会执行对未应用的模型所有的迁徙操作。migrate是一种非常强大的工具，它能够在升级模型数据库的情况下不丢失对应的数据，这里我们给出了修改模型的三步：

1.  在models.py文件夹之中修改模型
2.  运行 [<tt class="xref std std-djadmin docutils literal" style="font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed; color: #1d915c; font-size: 1em; font-weight: bold;"><span class="pre" style="font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed;">python</span> <span class="pre" style="font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed;">manage.py</span> <span class="pre" style="font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed;">makemigrations</span></tt>](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-makemigrations)<span style="color: #0c3c26; font-family: Roboto, Corbel, Avenir, 'Lucida Grande', 'Lucida Sans', sans-serif; font-size: 14px; line-height: 21px;"> </span> 来执行改变的迁徙行为
3.  运行 [<tt class="xref std std-djadmin docutils literal" style="font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed; color: #1d915c; font-size: 1em; font-weight: bold;"><span class="pre" style="font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed;">python</span> <span class="pre" style="font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed;">manage.py</span> <span class="pre" style="font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed;">migrate</span></tt>](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-migrate)<span style="color: #0c3c26; font-family: Roboto, Corbel, Avenir, 'Lucida Grande', 'Lucida Sans', sans-serif; font-size: 14px; line-height: 21px;"> </span> 来执行迁徙在数据库中的操作

在[这里](https://docs.djangoproject.com/en/1.8/ref/django-admin/)就能看到所有的manage.py能够做到的事情。

# 7 使用API

接着我们就开始使用Django提供的API来了，可以使用这个命令来激活Django的命令行：
<pre class="lang:default decode:true ">$ python manage.py shell</pre>

在这里我们并没有使用python，这是因为manage.py定义了DJANO_SETTING_MODULE环境变量，这样也能把mysite/setting.py引入自己的工程之中。

如果你就是不想使用manage.py的话，你可以设置<span style="line-height: 22.8571px;">DJANO_SETTING_MODULE环境变量到</span><span style="line-height: 22.8571px;">mysite/setting.py，在mysite文件夹下启动Shell命令行，输入以下命令：</span>
<pre class="lang:python decode:true ">&gt;&gt;&gt; import django
&gt;&gt;&gt; django.setup()</pre>

如果引发了一个<span style="color: #0c3c26; font-family: Roboto, Corbel, Avenir, 'Lucida Grande', 'Lucida Sans', sans-serif; font-size: 14px; line-height: 21px; background-color: #f1fff7;"> </span>[<tt class="xref py py-exc docutils literal" style="font-family: 'Fira Mono', Consolas, Menlo, Monaco, 'Courier New', Courier, monospace; font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed; color: #0c4b33; font-size: 1em; font-weight: bold;"><span class="pre" style="font-variant-ligatures: no-common-ligatures; text-rendering: optimizeSpeed;">AttributeError</span></tt>](https://docs.python.org/3/library/exceptions.html#AttributeError "(in Python v3.5)")的异常的话，那么就说明你安装的Django版本并非是1.8。

如果你想参考更多的函数的话，[这里](https://docs.djangoproject.com/en/1.8/topics/db/queries/)也有API的详情。
<pre class="lang:python decode:true ">&gt;&gt;&gt; from polls.models import Question, Choice   # Import the model classes we just wrote.

# No questions are in the system yet.
&gt;&gt;&gt; Question.objects.all()
[]

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
&gt;&gt;&gt; from django.utils import timezone
&gt;&gt;&gt; q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
&gt;&gt;&gt; q.save()

# Now it has an ID. Note that this might say "1L" instead of "1", depending
# on which database you're using. That's no biggie; it just means your
# database backend prefers to return integers as Python long integer
# objects.
&gt;&gt;&gt; q.id
1

# Access model field values via Python attributes.
&gt;&gt;&gt; q.question_text
"What's new?"
&gt;&gt;&gt; q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=&lt;UTC&gt;)

# Change values by changing the attributes, then calling save().
&gt;&gt;&gt; q.question_text = "What's up?"
&gt;&gt;&gt; q.save()

# objects.all() displays all the questions in the database.
&gt;&gt;&gt; Question.objects.all()
[&lt;Question: Question object&gt;]</pre>

 需要指出的是&lt;Question: Question object&gt; 是一种在表达上非常没有意义的表示形式，你可以在models采用<span class="lang:python decode:true  crayon-inline "> __str__() </span> 这个函数来指明此时输出的格式
<pre class="lang:python decode:true " title="polls/models.py">from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text</pre>

 增加这个函数是非常必要的，因为这不仅可以方便你以后检查代码，同时在Django的后台中得到很好的显示。

_对于Python3，使用<span class="lang:python decode:true  crayon-inline ">__str__</span> 即可，在Python 2 之中，你必须定义<span class="lang:python decode:true  crayon-inline ">__unicode__</span> 来返回一个unicode的代码，Django的<span class="lang:python decode:true  crayon-inline ">__str__</span> 会自动去调用<span class="lang:python decode:true  crayon-inline ">__unicode__</span> 这个函数。也就是说<span class="lang:python decode:true  crayon-inline ">__unicode__</span> 会返回一个unicode的字符串，而<span class="lang:python decode:true  crayon-inline ">__str__</span> 则会返回一个由UTF-8编码而成的字节码,但是Python 2 中object中的<span class="lang:python decode:true  crayon-inline ">__unicode__</span> 会调用<span class="lang:python decode:true  crayon-inline ">__str__</span> 来返回一个ASCII码的字符串，如果你觉得这很蛋疼的话，用Python 3就好。_

当然这只是一种很平淡的用法，而有的时候我们需要自定义用法来满足我们的需求：
<pre class="lang:python decode:true " title="polls/models.py">import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date &gt;= timezone.now() - datetime.timedelta(days=1)</pre>

 这里datetime的timezone和django.untils.timezone之间具有很大的差异，需要特别注意。[这里](https://docs.djangoproject.com/en/1.8/topics/i18n/timezones/)有相关的文档。
<pre class="lang:default decode:true " title="shell">&gt;&gt;&gt; from polls.models import Question, Choice

# Make sure our __str__() addition worked.
&gt;&gt;&gt; Question.objects.all()
[&lt;Question: What's up?&gt;]

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
&gt;&gt;&gt; Question.objects.filter(id=1)
[&lt;Question: What's up?&gt;]
&gt;&gt;&gt; Question.objects.filter(question_text__startswith='What')
[&lt;Question: What's up?&gt;]

# Get the question that was published this year.
&gt;&gt;&gt; from django.utils import timezone
&gt;&gt;&gt; current_year = timezone.now().year
&gt;&gt;&gt; Question.objects.get(pub_date__year=current_year)
&lt;Question: What's up?&gt;

# Request an ID that doesn't exist, this will raise an exception.
&gt;&gt;&gt; Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
&gt;&gt;&gt; Question.objects.get(pk=1)
&lt;Question: What's up?&gt;

# Make sure our custom method worked.
&gt;&gt;&gt; q = Question.objects.get(pk=1)
&gt;&gt;&gt; q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
&gt;&gt;&gt; q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
&gt;&gt;&gt; q.choice_set.all()
[]

# Create three choices.
&gt;&gt;&gt; q.choice_set.create(choice_text='Not much', votes=0)
&lt;Choice: Not much&gt;
&gt;&gt;&gt; q.choice_set.create(choice_text='The sky', votes=0)
&lt;Choice: The sky&gt;
&gt;&gt;&gt; c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
&gt;&gt;&gt; c.question
&lt;Question: What's up?&gt;

# And vice versa: Question objects get access to Choice objects.
&gt;&gt;&gt; q.choice_set.all()
[&lt;Choice: Not much&gt;, &lt;Choice: The sky&gt;, &lt;Choice: Just hacking again&gt;]
&gt;&gt;&gt; q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
&gt;&gt;&gt; Choice.objects.filter(question__pub_date__year=current_year)
[&lt;Choice: Not much&gt;, &lt;Choice: The sky&gt;, &lt;Choice: Just hacking again&gt;]

# Let's delete one of the choices. Use delete() for that.
&gt;&gt;&gt; c = q.choice_set.filter(choice_text__startswith='Just hacking')
&gt;&gt;&gt; c.delete()</pre>

#  8 后话

关于模型的关系，你可以点击[这里](https://docs.djangoproject.com/en/1.8/ref/models/relations/)。

关于数据库API的详尽内容，你可以点击[这里](https://docs.djangoproject.com/en/1.8/topics/db/queries/)。

下一章我们会介绍，如何使用管理员库来建立自己的网站。

 