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

<pre class="lang:python decode:true">&gt;&gt;&gt; for instance in session.query(User).order_by(User.id):
...     print(instance.name, instance.fullname)
ed Ed Jones
wendy Wendy Williams
mary Mary Contrary
fred Fred Flinstone</pre>

`Query`也接受ORM-instrumented descriptors作为参数。当多个参数传入时，返回结果为以同样顺序排列的tuples

<pre class="lang:python decode:true">&gt;&gt;&gt; for name, fullname in session.query(User.name, User.fullname):
...     print(name, fullname)
ed Ed Jones
wendy Wendy Williams
mary Mary Contrary
fred Fred Flinstone</pre>

`Query`返回的tuples由`KeyedTuple`这个类提供，其成员除了用下标访问意外，还可以视为实例变量来获取。对应的变量的名称与被查询的类变量名称一样，如下例：

<pre class="lang:python decode:true">&gt;&gt;&gt; for row in session.query(User, User.name).all():
...    print(row.User, row.name)
&lt;User(name='ed', fullname='Ed Jones', password='f8s7ccs')&gt; ed
&lt;User(name='wendy', fullname='Wendy Williams', password='foobar')&gt; wendy
&lt;User(name='mary', fullname='Mary Contrary', password='xxg527')&gt; mary
&lt;User(name='fred', fullname='Fred Flinstone', password='blah')&gt; fred</pre>

你可以通过`label()`来制定descriptor对应实例变量的名称

<pre class="lang:python decode:true">&gt;&gt;&gt; for row in session.query(User.name.label('name_label')).all():
...    print(row.name_label)
ed
wendy
mary
fred</pre>

而对于类参数而言，要实现同样的定制需要使用`aliased`

<pre class="lang:python decode:true">&gt;&gt;&gt; from sqlalchemy.orm import aliased
&gt;&gt;&gt; user_alias = aliased(User, name='user_alias')

SQL&gt;&gt;&gt; for row in session.query(user_alias, user_alias.name).all():
...    print(row.user_alias)
&lt;User(name='ed', fullname='Ed Jones', password='f8s7ccs')&gt;
&lt;User(name='wendy', fullname='Wendy Williams', password='foobar')&gt;
&lt;User(name='mary', fullname='Mary Contrary', password='xxg527')&gt;
&lt;User(name='fred', fullname='Fred Flinstone', password='blah')&gt;</pre>

基本的查询操作除了上面这些之外，还包括OFFSET和LIMIT，这个可以通过Python的array slice来完成。

<pre class="lang:python decode:true">&gt;&gt;&gt; for u in session.query(User).order_by(User.id)[1:3]:
...    print(u)
&lt;User(name='wendy', fullname='Wendy Williams', password='foobar')&gt;
&lt;User(name='mary', fullname='Mary Contrary', password='xxg527')&gt;</pre>

上述过程实际上只涉及了整体取出的操作，而没有进行筛选，筛选常用的函数是`filter_by`和`filter`。其中后者比起前者要更灵活一些，你可以在后者的参数中使用python的运算符。

<pre class="lang:python decode:true">&gt;&gt;&gt; for name, in session.query(User.name).\
...             filter_by(fullname='Ed Jones'):
...    print(name)
ed
&gt;&gt;&gt; for name, in session.query(User.name).\
...             filter(User.fullname=='Ed Jones'):
...    print(name)
ed</pre>

注意`Query`对象是**generative**的，这意味你可以把他们串接起来调用，如下：

<pre class="lang:python decode:true">&gt;&gt;&gt; for user in session.query(User).\
...          filter(User.name=='ed').\
...          filter(User.fullname=='Ed Jones'):
...    print(user)
&lt;User(name='ed', fullname='Ed Jones', password='f8s7ccs')&gt;</pre>

串接的`filter`之间是**与**的关系。

# 常用的filter操作符

下面的这些操作符可以应用在`filter`函数中

*   `equals`:

    query.filter(User.name == <span class="hljs-string">'ed'</span>)`</pre>
*   `not equals`:

    <pre class="hljs bash">`query.filter(User.name != <span class="hljs-string">'ed'</span>)`</pre>
*   `LIKE`:

    <pre class="hljs bash">`query.filter(User.name.like(<span class="hljs-string">'%ed%'</span>))`</pre>
*   `IN`:
    <pre class="hljs bash">`query.filter(User.name.in_([<span class="hljs-string">'ed'</span>, <span class="hljs-string">'wendy'</span>, <span class="hljs-string">'jack'</span>]))

    <span class="hljs-comment"># works with query objects too:</span>
    query.filter(User.name.in_(
            session.query(User.name).filter(User.name.like(<span class="hljs-string">'%ed%'</span>))
    ))`</pre>

*   `NOT IN`:
    <pre class="hljs bash">`query.filter(~User.name.in_([<span class="hljs-string">'ed'</span>, <span class="hljs-string">'wendy'</span>, <span class="hljs-string">'jack'</span>]))`</pre>

*   `IS NULL`:
    <pre class="hljs bash">`query.filter(User.name == None)

    <span class="hljs-comment"># alternatively, if pep8/linters are a concern</span>
    query.filter(User.name.is_(None))`</pre>

*   `IS NOT NULL`:
    <pre class="hljs bash">`query.filter(User.name != None)

    <span class="hljs-comment"># alternatively, if pep8/linters are a concern</span>
    query.filter(User.name.isnot(None))`</pre>

*   `AND`:
    <pre class="hljs bash">`<span class="hljs-comment"># use and_()</span>
    from sqlalchemy import and_
    query.filter(and_(User.name == <span class="hljs-string">'ed'</span>, User.fullname == <span class="hljs-string">'Ed Jones'</span>))

    <span class="hljs-comment"># or send multiple expressions to .filter()</span>
    query.filter(User.name == <span class="hljs-string">'ed'</span>, User.fullname == <span class="hljs-string">'Ed Jones'</span>)

    <span class="hljs-comment"># or chain multiple filter()/filter_by() calls</span>
    query.filter(User.name == <span class="hljs-string">'ed'</span>).filter(User.fullname == <span class="hljs-string">'Ed Jones'</span>)`</pre>

*   `OR`:
    <pre class="hljs bash">`from sqlalchemy import or_
    query.filter(or_(User.name == <span class="hljs-string">'ed'</span>, User.name == <span class="hljs-string">'wendy'</span>))`</pre>

*   `MATCH`:
    <pre class="hljs bash">`query.filter(User.name.match(<span class="hljs-string">'wendy'</span>))`</pre>

    # 返回列表(List)和单项(Scalar)

    很多`Query`的方法执行了SQL命令并返回了取出的数据库结果。

*   `all()`返回一个列表:

    <pre class="hljs bash">`&gt;&gt;&gt; query = session.query(User).filter(User.name.like(<span class="hljs-string">'%ed'</span>)).order_by(User.id)
    SQL&gt;&gt;&gt; query.all()
    [&lt;User(name=<span class="hljs-string">'ed'</span>, fullname=<span class="hljs-string">'Ed Jones'</span>, password=<span class="hljs-string">'f8s7ccs'</span>)&gt;,
        &lt;User(name=<span class="hljs-string">'fred'</span>, fullname=<span class="hljs-string">'Fred Flinstone'</span>, password=<span class="hljs-string">'blah'</span>)&gt;]`</pre>
*   `first()`返回至多一个结果，而且以单项形式，而不是只有一个元素的tuple形式返回这个结果.
    <pre class="hljs bash">`&gt;&gt;&gt; query.first()
    &lt;User(name=<span class="hljs-string">'ed'</span>, fullname=<span class="hljs-string">'Ed Jones'</span>, password=<span class="hljs-string">'f8s7ccs'</span>)&gt;`</pre>

*   `one()`返回且仅返回一个查询结果。当结果的数量不足一个或者多于一个时会报错。
    <pre class="lang:python decode:true">&gt;&gt;&gt; user = query.one()
    Traceback (most recent call last):
    ...
    MultipleResultsFound: Multiple rows were found for one()</pre>

    没有查找到结果时：

    <pre class="lang:python decode:true">&gt;&gt;&gt; user = query.filter(User.id == 99).one()
    Traceback (most recent call last):
    ...
    NoResultFound: No row was found for one()</pre>

*   `one_or_none()`：从名称可以看出，当结果数量为0时返回`None`， 多于1个时报错

*   `scalar()`和`one()`类似，但是返回单项而不是tuple

    # 嵌入使用SQL

    你可以在`Query`中通过`text()`使用SQL语句。例如：

    <pre class="lang:python decode:true">&gt;&gt;&gt; from sqlalchemy import text
    &gt;&gt;&gt; for user in session.query(User).\
    ...             filter(text("id&lt;224")).\
    ...             order_by(text("id")).all():
    ...     print(user.name)
    ed
    wendy
    mary
    fred</pre>

    除了上面这种直接将参数写进字符串的方式外，你还可以通过`params()`方法来传递参数

    <pre class="lang:python decode:true">&gt;&gt;&gt; session.query(User).filter(text("id&lt;:value and name=:name")).\
    ...     params(value=224, name='fred').order_by(User.id).one()
    &lt;User(name='fred', fullname='Fred Flinstone', password='blah')&gt;</pre>

    并且，你可以直接使用完整的SQL语句，但是要注意将表名和列明写正确。

    <pre class="hljs bash">`&gt;&gt;&gt; session.query(User).from_statement(
    ...                     text(<span class="hljs-string">"SELECT * FROM users where name=:name"</span>)).\
    ...                     params(name=<span class="hljs-string">'ed'</span>).all()
    [&lt;User(name=<span class="hljs-string">'ed'</span>, fullname=<span class="hljs-string">'Ed Jones'</span>, password=<span class="hljs-string">'f8s7ccs'</span>)&gt;]`</pre>

    # 计数

    `Query`定义了一个很方便的计数函数`count()`

    <pre class="hljs bash">`&gt;&gt;&gt; session.query(User).filter(User.name.like(<span class="hljs-string">'%ed'</span>)).count()
    SELECT count(*) AS count_1
    FROM (SELECT users.id AS users_id,
                    users.name AS users_name,
                    users.fullname AS users_fullname,
                    users.password AS users_password
    FROM users
    WHERE users.name LIKE ?) AS anon_1
    (<span class="hljs-string">'%ed'</span>,)
    <span class="hljs-number">2</span>`</pre>

    注意上面我们同时列出了实际的SQL指令。在SQLAlchemy中，我们总是将被计数的查询打包成一个子查询，然后对这个子查询进行计数。即便是最简单的`SELECT count(*) FROM table`，也会如此处理。为了更精细的控制计数过程，我们可以采用`func.count()`这个函数。

    <pre class="hljs bash">`&gt;&gt;&gt; from sqlalchemy import func
    SQL&gt;&gt;&gt; session.query(func.count(User.name), User.name).group_by(User.name).all()
    SELECT count(users.name) AS count_1, users.name AS users_name
    FROM users GROUP BY users.name
    ()
    [(<span class="hljs-number">1</span>, u<span class="hljs-string">'ed'</span>), (<span class="hljs-number">1</span>, u<span class="hljs-string">'fred'</span>), (<span class="hljs-number">1</span>, u<span class="hljs-string">'mary'</span>), (<span class="hljs-number">1</span>, u<span class="hljs-string">'wendy'</span>)]`</pre>

    为了实现最简单的`SELECT count(*) FROM table`，我们可以如下调用

    <pre class="hljs bash">`&gt;&gt;&gt; session.query(func.count(<span class="hljs-string">'*'</span>)).select_from(User).scalar()
    SELECT count(?) AS count_1
    FROM users
    (<span class="hljs-string">'*'</span>,)
    <span class="hljs-number">4</span>`</pre>

    如果我们对`User`的主键进行计数，那么`select_from`也可以省略。

    <pre class="hljs bash">`&gt;&gt;&gt; session.query(func.count(User.id)).scalar()
    SELECT count(users.id) AS count_1
    FROM users
    ()
    <span class="hljs-number">4</span>

在下一篇教程里面我们将会介绍SQLAlchemy对于『关系』的处理方式，以及针对关系的更加复杂的查询。