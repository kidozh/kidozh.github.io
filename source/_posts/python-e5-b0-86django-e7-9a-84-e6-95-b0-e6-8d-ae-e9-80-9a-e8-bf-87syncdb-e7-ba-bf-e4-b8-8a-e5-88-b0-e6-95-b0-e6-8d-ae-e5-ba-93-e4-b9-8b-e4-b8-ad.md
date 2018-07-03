---
title: '[Python]将Django的数据通过syncdb线上到数据库之中'
tags:
  - Django
  - Python
  - SAE
id: 813
categories:
  - Python
date: 2016-01-12 00:51:39
---

> 本文来自：[http://www.tuicool.com/articles/JRrQvu3](http://www.tuicool.com/articles/JRrQvu3)

# 如何syncdb线上到SAE的MySQL数据库中？

在本地开发环境中，如下配置数据库，即可执行 python manage.py syncdb 直接syncdb到线上数据库。
```python
# 线上数据库的配置
MYSQL_HOST = 'w.rdc.sae.sina.com.cn'
MYSQL_PORT = '3307'
MYSQL_USER = 'ACCESSKEY'
MYSQL_PASS = 'SECRETKEY'
MYSQL_DB   = 'app_APP_NAME'

from sae._restful_mysql import monkey
monkey.patch()

DATABASES = {
  'default': {
    'ENGINE':   'django.db.backends.mysql',
    'NAME':	 MYSQL_DB,
    'USER':	 MYSQL_USER,
    'PASSWORD': MYSQL_PASS,
    'HOST':	 MYSQL_HOST,
    'PORT':	 MYSQL_PORT,
  }
}
```


 需要注意的是：使用上述方法需要首先安装SAE的Python本地开发环境，Github项目地址：[https://github.com/sinacloud/sae-python-dev-guide](https://github.com/sinacloud/sae-python-dev-guide)

另外，上述功能还比较"buggy"，所以更加稳妥的数据库同步方案为：在本地执行数据库同步，将数据库变更以SQL的形式导出，然后使用SAE提供的phpmyadmin等工具进行导入。