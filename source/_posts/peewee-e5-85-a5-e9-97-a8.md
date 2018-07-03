---
title: peewee入门
tags:
  - orm
  - peewee
  - Python
id: 1427
categories:
  - Python
  - 网页
date: 2016-12-15 18:37:46
---

# 前言

折腾了几天SQLAlchemy，实在是折腾不动了，所以我决定开一个peewee的坑。

那么，迁移必然是有原因的，我来简单的说一下迁移代码的原因。

*   peewee的写法很像Django自带的orm，对于我这种Django支持者很好
*   其自带的类型比起SQLAlchemy来说，验证起来要简单许多
*   peewee轻量级，很方便

# 安装

## PIP

最简单的还是通过`PIP`来安装：
```default
pip install peewee
```

peewee包含了两个C的扩展：

*   Speedup ： 其包含了一些可以用C来重写的函数，当Cython已经安装的话，这个模块将会被自动安装。
*   Sqlite扩展 ： 其包含了一些用C操纵的SQLite的函数， REGEXP运算符以及全文搜索排序算法，这个模块应该使用`build_sqlite_ext`命令来安装
安装SQLite扩展的方法：
```default
python setup.py build_sqlite_ext
python setup.py install
```


## Git

这个工程托管于[https://github.com/coleifer/peewee](https://github.com/coleifer/peewee)并且可以使用git来安装。
```default
git clone https://github.com/coleifer/peewee.git
cd peewee
python setup.py install
```

如果你想构建SQLite扩展，你可以这样：

 
```default
# Build the sqlite extension and place the shared library alongside the other modules.
python setup.py build_sqlite_ext -i
```

在有些系统上，你需要使用`sudo`来提权

# 运行测试样例

运行命令
```default
python setup.py test

# Or use the test runner:
python runtests.py
```

你也可以使用`runtests.py`测试指定的特征，默认情况下会使用SQLite数据库，并且playhouse的扩展并不会被测试，你也可以使用下面的命令来查看命令的选项：
```default
python runtests.py --help
```


# 可选的依赖

> 因为大多数的Python发行版都包含SQLite的支持，你并不需要任何区别于标准库的依赖。你可以在命令行中运行import sqlite3来检测，如果你想运行于其他数据库的话，你可以分别使用满足 DB-API 2.0-compatible的驱动，比如针对MySQL的`pymysql` 或者针对Postgres的`psycopg2`

*   [Cython](http://cython.org/) ： 通常用于加速。如果你是用SQLite的话，那么速度提升就会变得很明显
*   [apsw](https://github.com/rogerbinns/apsw) ： 一个可选的SQLite的第三方库，其提供了更好的性能。你可以通过[`AESEncryptedField`](http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#AESEncryptedField "AESEncryptedField")来使用它。
*   [pycrypto](http://pythonhosted.org/pycrypto/) ： 一个为了AES加密的库，作用于[`AESEncryptedField`](http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#AESEncryptedField "AESEncryptedField")
*   bcrypt ： bcrypt加密手段，作用于[`PasswordField`](http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#PasswordField "PasswordField")
*   [gevent](http://www.gevent.org/) ：为了SqliteQueueDatabase的一个可选的依赖（其和`threading`这个库运行的很好）
*   [BerkeleyDB](http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/downloads/index.html) ：可以使用SQLite前端编译，它与Peewee一起工作。
如果你使用过django和flask框架，那会对你了解peewee非常有用。