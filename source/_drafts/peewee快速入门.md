---
title: peewee快速入门
id: 1434
categories:
  - 未分类
tags:
---

# 前言

这个博文讲述了一个简要的peewee特征，这个概述将会包括

*   模型定义
*   数据存储
*   取回数据
我强烈建议你能打开交互式shell命令行，并且运行。这样你就能够对peewee有个大致了解。

# 模型的定义

模型类，字段以及实例都对应着数据库的结构。
<table style="border-collapse: collapse; width: 108pt;" border="0" width="144" cellspacing="0" cellpadding="0"><colgroup><col style="width: 54pt;" span="2" width="72" /> </colgroup>
<tbody>
<tr>
<td width="72" height="18">Thing</td>
<td width="72">Corresponds to...</td>
</tr>
<tr>
<td height="18">Model class</td>
<td>Database table</td>
</tr>
<tr>
<td height="18">Field instance</td>
<td>Column on a table</td>
</tr>
<tr>
<td height="18">Model instance</td>
<td>Row in a database table</td>
</tr>
</tbody>
</table>
当开始使用peewee来开发工程的时候，最好的还是定义model实例：
<pre class="lang:python decode:true ">from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.</pre>
&nbsp;