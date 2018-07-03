---
title: SQLAlchemy查询
tags:
  - Python
  - sqlalchemy
id: 1400
categories:
  - Python
date: 2016-11-05 04:15:08
---

# 前言

和Django一样，我们orm也要知道如何查询数据。

# Query

`Session`的`query`函数会返回一个`Query`对象。`query`函数可以接受多种参数类型。可以是类，或者是类的instrumented **descriptor**。下面的这个例子取出了所有的`User`记录。

```python
>>> for instance in session.query(User).order_by(User.id):
...     print(instance.name, instance.fullname)
ed Ed Jones
wendy Wendy Williams
mary Mary Contrary
fred Fred Flinstone
```


`Query`也接受ORM-instrumented descriptors作为参数。当多个参数传入时，返回结果为以同样顺序排列的tuples

```python
>>> for name, fullname in session.query(User.name, User.fullname):
...     print(name, fullname)
ed Ed Jones
wendy Wendy Williams
mary Mary Contrary
fred Fred Flinstone
```


`Query`返回的tuples由`KeyedTuple`这个类提供，其成员除了用下标访问意外，还可以视为实例变量来获取。对应的变量的名称与被查询的类变量名称一样，如下例：

```python
>>> for row in session.query(User, User.name).all():
...    print(row.User, row.name)
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')> ed
<User(name='wendy', fullname='Wendy Williams', password='foobar')> wendy
<User(name='mary', fullname='Mary Contrary', password='xxg527')> mary
<User(name='fred', fullname='Fred Flinstone', password='blah')> fred
```


你可以通过`label()`来制定descriptor对应实例变量的名称

```python
>>> for row in session.query(User.name.label('name_label')).all():
...    print(row.name_label)
ed
wendy
mary
fred
```


而对于类参数而言，要实现同样的定制需要使用`aliased`

```python
>>> from sqlalchemy.orm import aliased
>>> user_alias = aliased(User, name='user_alias')

SQL>>> for row in session.query(user_alias, user_alias.name).all():
...    print(row.user_alias)
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
<User(name='wendy', fullname='Wendy Williams', password='foobar')>
<User(name='mary', fullname='Mary Contrary', password='xxg527')>
<User(name='fred', fullname='Fred Flinstone', password='blah')>
```


基本的查询操作除了上面这些之外，还包括OFFSET和LIMIT，这个可以通过Python的array slice来完成。

```python
>>> for u in session.query(User).order_by(User.id)[1:3]:
...    print(u)
<User(name='wendy', fullname='Wendy Williams', password='foobar')>
<User(name='mary', fullname='Mary Contrary', password='xxg527')>
```


上述过程实际上只涉及了整体取出的操作，而没有进行筛选，筛选常用的函数是`filter_by`和`filter`。其中后者比起前者要更灵活一些，你可以在后者的参数中使用python的运算符。

```python
>>> for name, in session.query(User.name).\
...             filter_by(fullname='Ed Jones'):
...    print(name)
ed
>>> for name, in session.query(User.name).\
...             filter(User.fullname=='Ed Jones'):
...    print(name)
ed
```


注意`Query`对象是**generative**的，这意味你可以把他们串接起来调用，如下：

```python
>>> for user in session.query(User).\
...          filter(User.name=='ed').\
...          filter(User.fullname=='Ed Jones'):
...    print(user)
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
```


串接的`filter`之间是**与**的关系。

# 常用的filter操作符

下面的这些操作符可以应用在`filter`函数中

*   `equals`:

    query.filter(User.name == 'ed')`
```

*   `not equals`:

    
```
`query.filter(User.name != 'ed')`
```

*   `LIKE`:

    
```
`query.filter(User.name.like('%ed%'))`
```

*   `IN`:
    
```
`query.filter(User.name.in_(['ed', 'wendy', 'jack']))

    # works with query objects too:
    query.filter(User.name.in_(
            session.query(User.name).filter(User.name.like('%ed%'))
    ))`
```


*   `NOT IN`:
    
```
`query.filter(~User.name.in_(['ed', 'wendy', 'jack']))`
```


*   `IS NULL`:
    
```
`query.filter(User.name == None)

    # alternatively, if pep8/linters are a concern
    query.filter(User.name.is_(None))`
```


*   `IS NOT NULL`:
    
```
`query.filter(User.name != None)

    # alternatively, if pep8/linters are a concern
    query.filter(User.name.isnot(None))`
```


*   `AND`:
    
```
`# use and_()
    from sqlalchemy import and_
    query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))

    # or send multiple expressions to .filter()
    query.filter(User.name == 'ed', User.fullname == 'Ed Jones')

    # or chain multiple filter()/filter_by() calls
    query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')`
```


*   `OR`:
    
```
`from sqlalchemy import or_
    query.filter(or_(User.name == 'ed', User.name == 'wendy'))`
```


*   `MATCH`:
    
```
`query.filter(User.name.match('wendy'))`
```


    # 返回列表(List)和单项(Scalar)

    很多`Query`的方法执行了SQL命令并返回了取出的数据库结果。

*   `all()`返回一个列表:

    
```
`>>> query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
    SQL>>> query.all()
    [<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>,
        <User(name='fred', fullname='Fred Flinstone', password='blah')>]`
```

*   `first()`返回至多一个结果，而且以单项形式，而不是只有一个元素的tuple形式返回这个结果.
    
```
`>>> query.first()
    <User(name='ed', fullname='Ed Jones', password='f8s7ccs')>`
```


*   `one()`返回且仅返回一个查询结果。当结果的数量不足一个或者多于一个时会报错。
    ```python
>>> user = query.one()
    Traceback (most recent call last):
    ...
    MultipleResultsFound: Multiple rows were found for one()
```


    没有查找到结果时：

    ```python
>>> user = query.filter(User.id == 99).one()
    Traceback (most recent call last):
    ...
    NoResultFound: No row was found for one()
```


*   `one_or_none()`：从名称可以看出，当结果数量为0时返回`None`， 多于1个时报错

*   `scalar()`和`one()`类似，但是返回单项而不是tuple

    # 嵌入使用SQL

    你可以在`Query`中通过`text()`使用SQL语句。例如：

    ```python
>>> from sqlalchemy import text
    >>> for user in session.query(User).\
    ...             filter(text("id<224")).\
    ...             order_by(text("id")).all():
    ...     print(user.name)
    ed
    wendy
    mary
    fred
```


    除了上面这种直接将参数写进字符串的方式外，你还可以通过`params()`方法来传递参数

    ```python
>>> session.query(User).filter(text("id<:value and name=:name")).\
    ...     params(value=224, name='fred').order_by(User.id).one()
    <User(name='fred', fullname='Fred Flinstone', password='blah')>
```


    并且，你可以直接使用完整的SQL语句，但是要注意将表名和列明写正确。

    
```
`>>> session.query(User).from_statement(
    ...                     text("SELECT * FROM users where name=:name")).\
    ...                     params(name='ed').all()
    [<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>]`
```


    # 计数

    `Query`定义了一个很方便的计数函数`count()`

    
```
`>>> session.query(User).filter(User.name.like('%ed')).count()
    SELECT count(*) AS count_1
    FROM (SELECT users.id AS users_id,
                    users.name AS users_name,
                    users.fullname AS users_fullname,
                    users.password AS users_password
    FROM users
    WHERE users.name LIKE ?) AS anon_1
    ('%ed',)
    2`
```


    注意上面我们同时列出了实际的SQL指令。在SQLAlchemy中，我们总是将被计数的查询打包成一个子查询，然后对这个子查询进行计数。即便是最简单的`SELECT count(*) FROM table`，也会如此处理。为了更精细的控制计数过程，我们可以采用`func.count()`这个函数。

    
```
`>>> from sqlalchemy import func
    SQL>>> session.query(func.count(User.name), User.name).group_by(User.name).all()
    SELECT count(users.name) AS count_1, users.name AS users_name
    FROM users GROUP BY users.name
    ()
    [(1, u'ed'), (1, u'fred'), (1, u'mary'), (1, u'wendy')]`
```


    为了实现最简单的`SELECT count(*) FROM table`，我们可以如下调用

    
```
`>>> session.query(func.count('*')).select_from(User).scalar()
    SELECT count(?) AS count_1
    FROM users
    ('*',)
    4`
```


    如果我们对`User`的主键进行计数，那么`select_from`也可以省略。

    
```
`>>> session.query(func.count(User.id)).scalar()
    SELECT count(users.id) AS count_1
    FROM users
    ()
    4

在下一篇教程里面我们将会介绍SQLAlchemy对于『关系』的处理方式，以及针对关系的更加复杂的查询。