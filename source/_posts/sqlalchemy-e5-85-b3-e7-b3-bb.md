---
title: SQLAlchemy关系
tags:
  - Python
  - sqlalchemy
id: 1403
categories:
  - Python
date: 2016-11-05 04:20:42
---

# 前言

『关系』是关系型数据库的一大特色，也是我们在建模过程中的一个重要的抽象过程。在前面的两个教程中，我们分别回顾了使用SQLAlchemy在数据库中进行[创建](http://www.jianshu.com/p/0d234e14b5d3)和[简单查询](http://www.jianshu.com/p/8d085e2f2657)的方法，今天我们来深入到更为复杂和抽象部分。

# 建立关系

之前我们已经建立了一个用户(User)表，现在我们来考虑增加一个与用户关联的新的表。在我们的系统里面，用户可以存储多个与之相关的email地址。这是一种基本的一对多的关系。我们把这个新增加的存储email地址的表称为`addresses`。应用Declarative，我们按照如下方式定义这个新表：

    &gt;&gt;&gt; from sqlalchemy import ForeignKey
    &gt;&gt;&gt; from sqlalchemy.orm import relationship

    &gt;&gt;&gt; class Address(Base):
    ...     __tablename__ = <span class="hljs-string">'addresses'</span>
    ...     id = Column(Integer, primary_key=True)
    ...     email_address = Column(String, nullable=False)
    ...     user_id = Column(Integer, ForeignKey(<span class="hljs-string">'users.id'</span>))
    ...
    ...     user = relationship(<span class="hljs-string">"User"</span>, back_populates=<span class="hljs-string">"addresses"</span>)
    ...
    ...     def __repr__(self):
    ...         <span class="hljs-built_in">return</span> <span class="hljs-string">"&lt;Address(email_address='%s')&gt;"</span> % self.email_address

    &gt;&gt;&gt; User.addresses = relationship(
    ...     <span class="hljs-string">"Address"</span>, order_by=Address.id, back_populates=<span class="hljs-string">"user"</span>)`</pre>

    上面的代码中我们使用了一个新的名为`ForeignKey`的构造。其含义为，其所在的列的值域应当被限制在另一个表的指定列的取值范围之类。这一特性是关系型数据库的核心特性之一。就上例而言，`addresses.user_id`这一列的取值范围，应当包含在`users.id`的取值范围之内。

    除了`ForeignKey`之外，我们还引入了一个`relationship`，来告诉ORM，`Address`类需要被连接到`User`类。`relationship`和`ForeignKey`这个两个属性决定了表之间关系的属性，决定了这个关系是多对一的。

    在完成对`Address`类的声明之后，我们还定义另一个`relationship`，将其赋值给了`User.addresses`。在两个`relationship`中，我们都有传入了一个`relationship.back_populates`的属性来为反向关系所对应的属性进行命名。（作者：到这里为止，看来SQLAlchemy中定义关系要比Django的ORM要麻烦许多。Django中只需要一行就可以了。而且这里的两个`relationship`的定义明显是冗余的）

    多对一的关系的反向永远都是一对多的关系。关于更多的`relationship()`的配置方法，可以参见这个链接[Basic Relationship Patterns](http://docs.sqlalchemy.org/en/rel_1_0/orm/basic_relationships.html#relationship-patterns)。

    上述我们定义的两个互补的关系`Address.user`和`User.addresses`被称为双向关系([bidirectional relationship](http://docs.sqlalchemy.org/en/rel_1_0/glossary.html#term-bidirectional-relationship))，这是SQLAlchemy的核心特性这一。

    `relationship()`的参数配置中指向被连接的类的字符串，可以指向工程中任何位置所定义的，基于`declarative base`的类，而无先后之分。Declarative会在完成所有的映射以后的将这些字符串转换为适当的、实际使用的参数形式。

    # 使用关联对象

    现在，当我们创建一个`User`实例的时候，会同时创建一个空的`addresses`的collection。这个collection可能是多种类型，如list, set, 或是dictionary。默认情况下，其应当为一个Python列表。

    <pre class="hljs bash">`&gt;&gt;&gt; jack = User(name=<span class="hljs-string">'jack'</span>, fullname=<span class="hljs-string">'Jack Bean'</span>, password=<span class="hljs-string">'gjffdd'</span>)
    &gt;&gt;&gt; jack.addresses
    []`</pre>

    此时你可以自由的向这个列表里面插入`User`对象。

    <pre class="hljs bash">`&gt;&gt;&gt; jack.addresses = [
    ...                 Address(email_address=<span class="hljs-string">'jack@google.com'</span>),
    ...                 Address(email_address=<span class="hljs-string">'j25@yahoo.com'</span>)]`</pre>

    当使用bidirectional relationship时，通过其中一个方向的关系（如上例）会自动出现在另一个方向的关系上。

    <pre class="hljs bash">`&gt;&gt;&gt; jack.addresses[<span class="hljs-number">1</span>]
    &lt;Address(email_address=<span class="hljs-string">'j25@yahoo.com'</span>)&gt;

    &gt;&gt;&gt; jack.addresses[<span class="hljs-number">1</span>].user
    &lt;User(name=<span class="hljs-string">'jack'</span>, fullname=<span class="hljs-string">'Jack Bean'</span>, password=<span class="hljs-string">'gjffdd'</span>)&gt;`</pre>

    让我们把jack添加进入`Session`。

    <pre class="hljs bash">`&gt;&gt;&gt; session.add(jack)
    &gt;&gt;&gt; session.commit()
    INSERT INTO users (name, fullname, password) VALUES (?, ?, ?)
    (<span class="hljs-string">'jack'</span>, <span class="hljs-string">'Jack Bean'</span>, <span class="hljs-string">'gjffdd'</span>)
    INSERT INTO addresses (email_address, user_id) VALUES (?, ?)
    (<span class="hljs-string">'jack@google.com'</span>, <span class="hljs-number">5</span>)
    INSERT INTO addresses (email_address, user_id) VALUES (?, ?)
    (<span class="hljs-string">'j25@yahoo.com'</span>, <span class="hljs-number">5</span>)
    COMMIT`</pre>

    可以发现上面执行了三个`INSERT`命令，也就是说与jack关联的两个`Address`对象也被提交了。现在我们通过查询来取出jack。

    <pre class="hljs php">`&gt;&gt;&gt; jack = session.query(User).\
    ... filter_by(name=<span class="hljs-string">'jack'</span>).one()
    BEGIN (implicit)
    SELECT users.id <span class="hljs-keyword">AS</span> users_id,
            users.name <span class="hljs-keyword">AS</span> users_name,
            users.fullname <span class="hljs-keyword">AS</span> users_fullname,
            users.password <span class="hljs-keyword">AS</span> users_password
    FROM users
    WHERE users.name = ?
    (<span class="hljs-string">'jack'</span>,)

    &gt;&gt;&gt; jack
    &lt;User(name=<span class="hljs-string">'jack'</span>, fullname=<span class="hljs-string">'Jack Bean'</span>, password=<span class="hljs-string">'gjffdd'</span>)&gt;`</pre>

    可以发现目前只有针对`User`表的查询，而没有对`Address`表的查询。此时访问`addresses`属性，相关的SQL才会执行

    <pre class="hljs php">`&gt;&gt;&gt; jack.addresses
    SELECT addresses.id <span class="hljs-keyword">AS</span> addresses_id,
            addresses.email_address <span class="hljs-keyword">AS</span>
            addresses_email_address,
            addresses.user_id <span class="hljs-keyword">AS</span> addresses_user_id
    FROM addresses
    WHERE ? = addresses.user_id ORDER BY addresses.id
    (<span class="hljs-number">5</span>,)
    [&lt;Address(email_address=<span class="hljs-string">'jack@google.com'</span>)&gt;, &lt;Address(email_address=<span class="hljs-string">'j25@yahoo.com'</span>)&gt;]`</pre>

    上面这种方式我们称之为[lazy loading](http://docs.sqlalchemy.org/en/rel_1_0/glossary.html#term-lazy-loading)。

    # 使用join进行查询

    现在我们有了两会在那个彼此关联的数据表了，相比与上一篇教程中的简单查询情况，此时试图对这两张表进行联合查询就更加复杂一些了。关于join技术，读者可以自行阅读[我的前一篇文章](http://www.jianshu.com/p/9e1d3793cba6)。

    为了在`User`和`Address`之间构造一个简单的join，我们可以通过`Query.filter()`来连接其相关列（本质是隐式写法的JOIN）。下面是一个简单的例子：

    <pre class="hljs bash">`&gt;&gt;&gt; <span class="hljs-keyword">for</span> u, a <span class="hljs-keyword">in</span> session.query(User, Address).\
    ...                     filter(User.id==Address.user_id).\
    ...                     filter(Address.email_address==<span class="hljs-string">'jack@google.com'</span>).\
    ...                     all():
    ...     <span class="hljs-built_in">print</span>(u)
    ...     <span class="hljs-built_in">print</span>(a)
    &lt;User(name=<span class="hljs-string">'jack'</span>, fullname=<span class="hljs-string">'Jack Bean'</span>, password=<span class="hljs-string">'gjffdd'</span>)&gt;
    &lt;Address(email_address=<span class="hljs-string">'jack@google.com'</span>)&gt;`</pre>

    而实际的SQL JOIN语法，可以通过`Query.join()`来想实现

    <pre class="hljs bash">`&gt;&gt;&gt; session.query(User).join(Address).\
    ...         filter(Address.email_address==<span class="hljs-string">'jack@google.com'</span>).\
    ...         all()
    users.id AS users_id,
            users.name AS users_name,
            users.fullname AS users_fullname,
            users.password AS users_password
    FROM users JOIN addresses ON users.id = addresses.user_id
    WHERE addresses.email_address = ?
    (<span class="hljs-string">'jack@google.com'</span>,)
    [&lt;User(name=<span class="hljs-string">'jack'</span>, fullname=<span class="hljs-string">'Jack Bean'</span>, password=<span class="hljs-string">'gjffdd'</span>)&gt;]`</pre>

    在上面的例子中由于只存在一个ForeignKey，`Query.join`知道如何选取合适的列进行JOIN。如果没有定义ForeignKey，或者存在多个，此时你需要手动指明你参与JOIN的列。`Query.join()`以如下方式进行：

    <pre class="hljs bash">`query.join(Address, User.id==Address.user_id)    <span class="hljs-comment"># explicit condition</span>
    query.join(User.addresses)                       <span class="hljs-comment"># specify relationship from left to right</span>
    query.join(Address, User.addresses)              <span class="hljs-comment"># same, with explicit target</span>
    query.join(<span class="hljs-string">'addresses'</span>)`</pre>

    对于OUTER JOIN，只需要使用`Query.outerjoin()`就可以了。

    <pre class="hljs bash">`query.outerjoin(User.addresses)   <span class="hljs-comment"># LEFT OUTER JOIN</span>`</pre>

    关于`join()`更为详细的用法，还是请参考官方的文档[join](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html#sqlalchemy.orm.query.Query.join)

    ## 使用Aliases

    当你的查询涉及多个表，而其中同一个表出现了多次时，你需要的为重复的表aliase一个新的名字来避免冲突。这个功能其实我们在上一篇文章里面也提到过，下面是关于`aliased`的一个例子：

    <pre class="hljs bash">`&gt;&gt;&gt; from sqlalchemy.orm import aliased
    &gt;&gt;&gt; adalias1 = aliased(Address)
    &gt;&gt;&gt; adalias2 = aliased(Address)
    &gt;&gt;&gt; <span class="hljs-keyword">for</span> username, email1, email2 <span class="hljs-keyword">in</span> \
    ...     session.query(User.name, adalias1.email_address, adalias2.email_address).\
    ...     join(adalias1, User.addresses).\
    ...     join(adalias2, User.addresses).\
    ...     filter(adalias1.email_address==<span class="hljs-string">'jack@google.com'</span>).\
    ...     filter(adalias2.email_address==<span class="hljs-string">'j25@yahoo.com'</span>):
    ...     <span class="hljs-built_in">print</span>(username, email1, email2)
    SELECT users.name AS users_name,
            addresses_1.email_address AS addresses_1_email_address,
            addresses_2.email_address AS addresses_2_email_address
    FROM users JOIN addresses AS addresses_1
            ON users.id = addresses_1.user_id
    JOIN addresses AS addresses_2
            ON users.id = addresses_2.user_id
    WHERE addresses_1.email_address = ?
            AND addresses_2.email_address = ?
    (<span class="hljs-string">'jack@google.com'</span>, <span class="hljs-string">'j25@yahoo.com'</span>)
    jack jack@google.com j25@yahoo.com`</pre>

    ## 使用子查询(Subqueries)

    `Query`适合于用来构造子查询。假如我们想要取出`User`记录，并且同时计算各个用户的`Address`的数量。产生这种功能的SQL指令最好的办法是按照user的id分组统计地址的数量，然后join到外层查询。此时我们需要LEFT JOIN，这样可以使得没有地址的用户也会出现在查询结果中（地址数量为0）。 我们期望的SQL命令是这样的：

    <pre class="hljs sql">`<span class="hljs-operator">SELECT <span class="hljs-keyword">users</span>.*, adr_count.address_count <span class="hljs-keyword">FROM</span> <span class="hljs-keyword">users</span> <span class="hljs-keyword">LEFT</span> <span class="hljs-keyword">OUTER</span> <span class="hljs-keyword">JOIN</span>
        (SELECT user_id, <span class="hljs-keyword">count</span>(*) <span class="hljs-keyword">AS</span> address_count
            <span class="hljs-keyword">FROM</span> addresses <span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> user_id) <span class="hljs-keyword">AS</span> adr_count
        <span class="hljs-keyword">ON</span> <span class="hljs-keyword">users</span>.<span class="hljs-keyword">id</span>=adr_count.user_id</span>`</pre>

    使用`Query`，我们可以从内到外来构造上面的语句。

    <pre class="hljs bash">`&gt;&gt;&gt; from sqlalchemy.sql import func
    &gt;&gt;&gt; stmt = session.query(Address.user_id, func.count(<span class="hljs-string">'*'</span>).\
    ...         label(<span class="hljs-string">'address_count'</span>)).\
    ...         group_by(Address.user_id).subquery()`</pre>

    `func`我们已经在之前的教程中认识过了。`subquery()`可以产生一个内嵌了alias（是一个`query.statement.alias()`）的查询(SELECT)语句的表达。

    当我们生成了statement之后，其完全可以视为一个`Table`来使用。你可以通过`c`来访问它的属性。

    <pre class="hljs bash">`&gt;&gt;&gt; <span class="hljs-keyword">for</span> u, count <span class="hljs-keyword">in</span> session.query(User, stmt.c.address_count).\
    ...     outerjoin(stmt, User.id==stmt.c.user_id).order_by(User.id):
    ...     <span class="hljs-built_in">print</span>(u, count)
    SELECT users.id AS users_id,
            users.name AS users_name,
            users.fullname AS users_fullname,
            users.password AS users_password,
            anon_1.address_count AS anon_1_address_count
    FROM users LEFT OUTER JOIN
        (SELECT addresses.user_id AS user_id, count(?) AS address_count
        FROM addresses GROUP BY addresses.user_id) AS anon_1
        ON users.id = anon_1.user_id
    ORDER BY users.id
    (<span class="hljs-string">'*'</span>,)
    &lt;User(name=<span class="hljs-string">'ed'</span>, fullname=<span class="hljs-string">'Ed Jones'</span>, password=<span class="hljs-string">'f8s7ccs'</span>)&gt; None
    &lt;User(name=<span class="hljs-string">'wendy'</span>, fullname=<span class="hljs-string">'Wendy Williams'</span>, password=<span class="hljs-string">'foobar'</span>)&gt; None
    &lt;User(name=<span class="hljs-string">'mary'</span>, fullname=<span class="hljs-string">'Mary Contrary'</span>, password=<span class="hljs-string">'xxg527'</span>)&gt; None
    &lt;User(name=<span class="hljs-string">'fred'</span>, fullname=<span class="hljs-string">'Fred Flinstone'</span>, password=<span class="hljs-string">'blah'</span>)&gt; None
    &lt;User(name=<span class="hljs-string">'jack'</span>, fullname=<span class="hljs-string">'Jack Bean'</span>, password=<span class="hljs-string">'gjffdd'</span>)&gt; <span class="hljs-number">2</span>`</pre>

    ## 从子查询中取出Entity

    在前一个例子中，我们从子查询活着的是一个临时性的JOIN后的表，但是这个表并未定义我们在ORM中定义的Entity。如果我们想将这个临时表映射到ORM中的类呢？此时我们可以使用`aliased`这个函数来完成这个映射。

    <pre class="hljs bash">`&gt;&gt;&gt; stmt = session.query(Address).\
    ...                 filter(Address.email_address != <span class="hljs-string">'j25@yahoo.com'</span>).\
    ...                 subquery()
    &gt;&gt;&gt; adalias = aliased(Address, stmt)
    &gt;&gt;&gt; <span class="hljs-keyword">for</span> user, address <span class="hljs-keyword">in</span> session.query(User, adalias).\
    ...         join(adalias, User.addresses):
    ...     <span class="hljs-built_in">print</span>(user)
    ...     <span class="hljs-built_in">print</span>(address)
    SELECT users.id AS users_id,
                users.name AS users_name,
                users.fullname AS users_fullname,
                users.password AS users_password,
                anon_1.id AS anon_1_id,
                anon_1.email_address AS anon_1_email_address,
                anon_1.user_id AS anon_1_user_id
    FROM users JOIN
        (SELECT addresses.id AS id,
                addresses.email_address AS email_address,
                addresses.user_id AS user_id
        FROM addresses
        WHERE addresses.email_address != ?) AS anon_1
        ON users.id = anon_1.user_id
    (<span class="hljs-string">'j25@yahoo.com'</span>,)
    &lt;User(name=<span class="hljs-string">'jack'</span>, fullname=<span class="hljs-string">'Jack Bean'</span>, password=<span class="hljs-string">'gjffdd'</span>)&gt;
    &lt;Address(email_address=<span class="hljs-string">'jack@google.com'</span>)&gt;`</pre>

    # 使用EXISTS

    EXISTS关键字是一个BOOL型操作符。当查询结果存在至少一行时返回True。EXISTS可以常常和JOIN搭配使用。

    下面是一个显式的EXISTS构造方法：

    <pre class="hljs bash">`&gt;&gt;&gt; from sqlalchemy.sql import exists
    &gt;&gt;&gt; stmt = exists().where(Address.user_id==User.id)
    &gt;&gt;&gt; <span class="hljs-keyword">for</span> name, <span class="hljs-keyword">in</span> session.query(User.name).filter(stmt):
    ...     <span class="hljs-built_in">print</span>(name)
    SELECT users.name AS users_name
    FROM users
    WHERE EXISTS (SELECT *
    FROM addresses
    WHERE addresses.user_id = users.id)
    ()
    jack`</pre>

    `Query`还定义了若干个自动使用了EXISTS的操作。上面的例子可以用`any()`来完成：

    <pre class="hljs bash">`&gt;&gt;&gt; <span class="hljs-keyword">for</span> name, <span class="hljs-keyword">in</span> session.query(User.name).\
    ...         filter(User.addresses.any()):
    ...     <span class="hljs-built_in">print</span>(name)
    SELECT users.name AS users_name
    FROM users
    WHERE EXISTS (SELECT <span class="hljs-number">1</span>
    FROM addresses
    WHERE users.id = addresses.user_id)
    ()
    jack`</pre>

    `any()`也接受筛选条件来限制匹配的行：

    <pre class="hljs bash">`&gt;&gt;&gt; <span class="hljs-keyword">for</span> name, <span class="hljs-keyword">in</span> session.query(User.name).\
    ...     filter(User.addresses.any(Address.email_address.like(<span class="hljs-string">'%google%'</span>))):
    ...     <span class="hljs-built_in">print</span>(name)
    jack`</pre>

    `has()`对于的many-to-one的关系，起到的是和`any()`同样的作用（注意这里`~`表示NOT）：

    <pre class="hljs bash">`&gt;&gt;&gt; session.query(Address).\
    ...         filter(~Address.user.has(User.name==<span class="hljs-string">'jack'</span>)).all()
    []`</pre>

    ## 常用的关系操作

    下面只是简单的列出了一些常用的操作。想要更为详细的了解这些功能，还是推荐去官网的相关文档。

*   **eq**() (many-to-one “equals” comparison):
    <pre class="hljs swift">`query.<span class="hljs-built_in">filter</span>(<span class="hljs-type">Address</span>.user == someuser)`</pre>

*   **ne**() (many-to-one “not equals” comparison):
    <pre class="hljs swift">`query.<span class="hljs-built_in">filter</span>(<span class="hljs-type">Address</span>.user != someuser)`</pre>

*   IS NULL (many-to-one comparison, also uses **eq**()):
    <pre class="hljs python">`query.filter(Address.user == <span class="hljs-keyword">None</span>)`</pre>

*   contains() (used for one-to-many collections):
    <pre class="hljs css">`<span class="hljs-tag">query</span><span class="hljs-class">.filter</span>(<span class="hljs-tag">User</span><span class="hljs-class">.addresses</span><span class="hljs-class">.contains</span>(<span class="hljs-tag">someaddress</span>))`</pre>

*   any() (used for collections):
    <pre class="hljs bash">`query.filter(User.addresses.any(Address.email_address == <span class="hljs-string">'bar'</span>))

    <span class="hljs-comment"># also takes keyword arguments:</span>
    query.filter(User.addresses.any(email_address=<span class="hljs-string">'bar'</span>))`</pre>

*   has() (used for scalar references):
    <pre class="hljs bash">`query.filter(Address.user.has(name=<span class="hljs-string">'ed'</span>))`</pre>

*   Query.with_parent() (used for any relationship):
    <pre class="hljs bash">`session.query(Address).with_parent(someuser, <span class="hljs-string">'addresses'</span>)`</pre>

    ## Eager Loading（找不到合适的翻译）

    前面的教程中我们有提及到lazing loading的机制。当我们通过查询取出用户时，与之关联的地址并没有取出来。当我们试图获取`User.addresses`时，相关的针对地址的SQL查询才起作用。如果你想要减少query的次数的话，就需要使用Eager Loading了。SQLAlchemy提供了三种Eager Loading的方式，其中两种是自动的，而第三种涉及到自定义的筛选条件。所有的这三种Eager Loading方式都会通过调用`Query.options()`来影响查询的过程，促使`Query`生成需要的额外配置来取出期望的内容。

    # Subquery Loading

    在上面的例子中，我们希望在 取出用户的时候就同步取出对应的地址。此时你们可以此采用`orm.subqueryload()`。这个函数可以发起第二个SELECT查询来取出与结果相关的另一个表的信息。这里取名为"subquery"的原因是，此处的`Query`在发起第二个查询时作为子查询而被复用了。详细过程参加下面的程序：

    <pre class="hljs bash">`&gt;&gt;&gt; from sqlalchemy.orm import subqueryload
    &gt;&gt;&gt; jack = session.query(User).\
    ...                 options(subqueryload(User.addresses)).\
    ...                 filter_by(name=<span class="hljs-string">'jack'</span>).one()
    SELECT users.id AS users_id,
            users.name AS users_name,
            users.fullname AS users_fullname,
            users.password AS users_password
    FROM users
    WHERE users.name = ?
    (<span class="hljs-string">'jack'</span>,)
    SELECT addresses.id AS addresses_id,
            addresses.email_address AS addresses_email_address,
            addresses.user_id AS addresses_user_id,
            anon_1.users_id AS anon_1_users_id
    FROM (SELECT users.id AS users_id
        FROM users WHERE users.name = ?) AS anon_1
    JOIN addresses ON anon_1.users_id = addresses.user_id
    ORDER BY anon_1.users_id, addresses.id
    (<span class="hljs-string">'jack'</span>,)
    &gt;&gt;&gt; jack
    &lt;User(name=<span class="hljs-string">'jack'</span>, fullname=<span class="hljs-string">'Jack Bean'</span>, password=<span class="hljs-string">'gjffdd'</span>)&gt;

    &gt;&gt;&gt; jack.addresses
    [&lt;Address(email_address=<span class="hljs-string">'jack@google.com'</span>)&gt;, &lt;Address(email_address=<span class="hljs-string">'j25@yahoo.com'</span>)&gt;]`</pre>

    **注意**：当`subqueryload()`和涉及limiting的函数一起使用的时候（如`Query.first()`, `Query.limit()`, Query.offset()`等），应当加上一个以Unique的行作为参数的`Query.order_by()`来确保结果的正确性。详情参见[The importance of Ordering](http://docs.sqlalchemy.org/en/rel_1_0/orm/loading_relationships.html#subqueryload-ordering)

    # Joined Load

    这种自动Eager Loading的方式要更为常用一些。Joined Loading发起了一个JOIN（默认是LEFT OUTER JOIN），故而查询结果和制定的与之关联的行可以被同时取出。我们这里以和上面的Subquery Loading中同样的查询目的为例。

    <pre class="hljs bash">`&gt;&gt;&gt; from sqlalchemy.orm import joinedload

    &gt;&gt;&gt; jack = session.query(User).\
    ...                        options(joinedload(User.addresses)).\
    ...                        filter_by(name=<span class="hljs-string">'jack'</span>).one()
    SELECT users.id AS users_id,
            users.name AS users_name,
            users.fullname AS users_fullname,
            users.password AS users_password,
            addresses_1.id AS addresses_1_id,
            addresses_1.email_address AS addresses_1_email_address,
            addresses_1.user_id AS addresses_1_user_id
    FROM users
        LEFT OUTER JOIN addresses AS addresses_1 ON users.id = addresses_1.user_id
    WHERE users.name = ? ORDER BY addresses_1.id
    (<span class="hljs-string">'jack'</span>,)

    &gt;&gt;&gt; jack
    &lt;User(name=<span class="hljs-string">'jack'</span>, fullname=<span class="hljs-string">'Jack Bean'</span>, password=<span class="hljs-string">'gjffdd'</span>)&gt;

    &gt;&gt;&gt; jack.addresses
    [&lt;Address(email_address=<span class="hljs-string">'jack@google.com'</span>)&gt;, &lt;Address(email_address=<span class="hljs-string">'j25@yahoo.com'</span>)&gt;]`</pre>

    注意到，如果你是在命令行运行了前一个Subquery Loading的例子的话，在这里jack的addresses实际上已经填充了的，但是这里的Joined Load仍然是会发起JOIN。另外，LEFT OUTER JOIN指令实际上有可能导致重复的User出现，但是在结果中实际得到的User却不会重复。这是因为`Query`实际上是基于Object Identity采用了一种"uniquing"的策略。

    历史上来看`joinedload()`出现的更早一些。`joinedloading()`更加适合于处理Many-to-one的关系。

    # 显式的Join + EagerLoad

    第三种方式我们是我们自己显式的调用join来定位JOIN连接主键，并接着关联表的信息填充到查询结果中对应对象或者列表中。这个特性需要使用到`orm.contains_eager()`函数。这个机制最典型的用途是pre-loading many-to-one关系，同时添加对这个关系的筛选。我们用下面的这个例子来阐述说明上面这些比较绕的话。假设我们需要筛选出用户的名字为jack的邮件地址，进行这个查询的方法如下：

    <pre class="hljs bash">`&gt;&gt;&gt; from sqlalchemy.orm import contains_eager
    &gt;&gt;&gt; jacks_addresses = session.query(Address).\
    ...                             join(Address.user).\
    ...                             filter(User.name==<span class="hljs-string">'jack'</span>).\
    ...                             options(contains_eager(Address.user)).\
    ...                             all()
    SELECT users.id AS users_id,
            users.name AS users_name,
            users.fullname AS users_fullname,
            users.password AS users_password,
            addresses.id AS addresses_id,
            addresses.email_address AS addresses_email_address,
            addresses.user_id AS addresses_user_id
    FROM addresses JOIN users ON users.id = addresses.user_id
    WHERE users.name = ?
    (<span class="hljs-string">'jack'</span>,)

    &gt;&gt;&gt; jacks_addresses
    [&lt;Address(email_address=<span class="hljs-string">'jack@google.com'</span>)&gt;, &lt;Address(email_address=<span class="hljs-string">'j25@yahoo.com'</span>)&gt;]

    &gt;&gt;&gt; jacks_addresses[<span class="hljs-number">0</span>].user
    &lt;User(name=<span class="hljs-string">'jack'</span>, fullname=<span class="hljs-string">'Jack Bean'</span>, password=<span class="hljs-string">'gjffdd'</span>)&gt;`</pre>

    ## 关系中的删除问题

    沃恩尝试删除jack，来看结果：

    <pre class="hljs bash">`&gt;&gt;&gt; session.delete(jack)
    &gt;&gt;&gt; session.query(User).filter_by(name=<span class="hljs-string">'jack'</span>).count()
    UPDATE addresses SET user_id=? WHERE addresses.id = ?
    ((None, <span class="hljs-number">1</span>), (None, <span class="hljs-number">2</span>))
    DELETE FROM users WHERE users.id = ?
    (<span class="hljs-number">5</span>,)
    SELECT count(*) AS count_1
    FROM (SELECT users.id AS users_id,
            users.name AS users_name,
            users.fullname AS users_fullname,
            users.password AS users_password
    FROM users
    WHERE users.name = ?) AS anon_1
    (<span class="hljs-string">'jack'</span>,)
    <span class="hljs-number">0</span>`</pre>

    那么与jack关联的地址呢？

    <pre class="hljs css">`&gt;&gt;&gt; <span class="hljs-tag">session</span><span class="hljs-class">.query</span>(<span class="hljs-tag">Address</span>)<span class="hljs-class">.filter</span>(
    ...     <span class="hljs-tag">Address</span><span class="hljs-class">.email_address</span><span class="hljs-class">.in_</span>(<span class="hljs-attr_selector">['jack@google.com', 'j25@yahoo.com']</span>)
    ...  )<span class="hljs-class">.count</span>()
    2`</pre>

    地址记录仍然在这里。如果我们commit的话，我们可以从上面的SQL语句中发现，相关的`Address`的`user_id`属性被设置成了NULL。这不符合我们的要求。那么我们需要自己来设置关系的删除规则。

    ## 配置delete/delete-orphan Cascade

    我们通过配置`User.addresses`关系的**cascade***选项来控制删除行为。尽管SQLAlchemy允许你在任何时候给ORM添加属性或者关系。此时我们还是需要移除现存的关系并且重新开始（作者：django的ORM包含）。让我们首先关闭当前的session

    <pre class="hljs bash">`&gt;&gt;&gt; session.close()`</pre>

    并且使用一个新的`declarative_base()`:

    <pre class="hljs bash">`&gt;&gt;&gt; Base = declarative_base()`</pre>

    下面我们重新声明`User`类，注意`addresses`中的配置：

    <pre class="hljs bash">`&gt;&gt;&gt; class User(Base):
    ...     __tablename__ = <span class="hljs-string">'users'</span>
    ...
    ...     id = Column(Integer, primary_key=True)
    ...     name = Column(String)
    ...     fullname = Column(String)
    ...     password = Column(String)
    ...
    ...     addresses = relationship(<span class="hljs-string">"Address"</span>, back_populates=<span class="hljs-string">'user'</span>,
    ...                     cascade=<span class="hljs-string">"all, delete, delete-orphan"</span>)
    ...
    ...     def __repr__(self):
    ...        <span class="hljs-built_in">return</span> <span class="hljs-string">"&lt;User(name='%s', fullname='%s', password='%s')&gt;"</span> % (
    ...                                self.name, self.fullname, self.password)`</pre>

    接下来重新声明`Address`。

    <pre class="hljs bash">`&gt;&gt;&gt; class Address(Base):
    ...     __tablename__ = <span class="hljs-string">'addresses'</span>
    ...     id = Column(Integer, primary_key=True)
    ...     email_address = Column(String, nullable=False)
    ...     user_id = Column(Integer, ForeignKey(<span class="hljs-string">'users.id'</span>))
    ...     user = relationship(<span class="hljs-string">"User"</span>, back_populates=<span class="hljs-string">"addresses"</span>)
    ...
    ...     def __repr__(self):
    ...         <span class="hljs-built_in">return</span> <span class="hljs-string">"&lt;Address(email_address='%s')&gt;"</span> % self.email_address`</pre>

    现在让我们取出jack(下面我们使用了一个之前没有提到的函数`get()`，其参数为查询目标的主键)，现在从`addresses`中删除一个地址的话，会导致这个`Address`被删除。

    <pre class="hljs bash">`<span class="hljs-comment"># load Jack by primary key</span>
    SQL&gt;&gt;&gt; jack = session.query(User).get(<span class="hljs-number">5</span>)

    <span class="hljs-comment"># remove one Address (lazy load fires off)</span>
    SQL&gt;&gt;&gt; del jack.addresses[<span class="hljs-number">1</span>]

    <span class="hljs-comment"># only one address remains</span>
    SQL&gt;&gt;&gt; session.query(Address).filter(
    ...     Address.email_address.in_([<span class="hljs-string">'jack@google.com'</span>, <span class="hljs-string">'j25@yahoo.com'</span>])
    ... ).count()
    <span class="hljs-number">1</span>`</pre>

    删除jack也会导致剩下jack以及其所有的`Address`都会被删除:

    <pre class="hljs bash">`&gt;&gt; session.delete(jack)

    SQL&gt;&gt;&gt; session.query(User).filter_by(name=<span class="hljs-string">'jack'</span>).count()
    <span class="hljs-number">0</span>

    SQL&gt;&gt;&gt; session.query(Address).filter(
    ...    Address.email_address.in_([<span class="hljs-string">'jack@google.com'</span>, <span class="hljs-string">'j25@yahoo.com'</span>])
    ... ).count()
    <span class="hljs-number">0</span>`</pre>

    关于更多的Cascade配置请参见官方文档。

    ## 建立多对多关系ManyToMany Relationship

    现在我们需要引入一个新的模型来阐述多对多的关系了。假设我们需要完成一个博客应用。在这个应用里面我们可以书写`BlogPost`，每个博客都有若干`Keyword`。

    对于一个多对多的关系，我们需要建立一个未映射的（也就是没有一个Python类与之对应的）表`Table`来作为中间联系的表。

    <pre class="hljs bash">`&gt;&gt;&gt; from sqlalchemy import Table, Text
    &gt;&gt;&gt; <span class="hljs-comment"># association table</span>
    &gt;&gt;&gt; post_keywords = Table(<span class="hljs-string">'post_keywords'</span>, Base.metadata,
    ...     Column(<span class="hljs-string">'post_id'</span>, ForeignKey(<span class="hljs-string">'posts.id'</span>), primary_key=True),
    ...     Column(<span class="hljs-string">'keyword_id'</span>, ForeignKey(<span class="hljs-string">'keywords.id'</span>), primary_key=True)
    ... )`</pre>

    不同于我们之前的典型的ORM方法，在上面的代码中我们直接声明了一个`Table`，而没有制定与之对应的Python类。`Table`是一个构造函数，其参数中的每个`Colomn`以逗号分隔。

    下面我们来定义`BlogPost`和`Keyword`。我们这里需要使用`relationship()`在这两个类中定义一对互补的关系，其中每个关系的都指向`post_keyword`这个表。

    <pre class="hljs bash">`&gt;&gt;&gt; class B<span class="hljs-built_in">log</span>Post(Base):
    ...     __tablename__ = <span class="hljs-string">'posts'</span>
    ...
    ...     id = Column(Integer, primary_key=True)
    ...     user_id = Column(Integer, ForeignKey(<span class="hljs-string">'users.id'</span>))
    ...     headline = Column(String(<span class="hljs-number">255</span>), nullable=False)
    ...     body = Column(Text)
    ...
    ...     <span class="hljs-comment"># many to many BlogPost&lt;-&gt;Keyword</span>
    ...     keywords = relationship(<span class="hljs-string">'Keyword'</span>,
    ...                             secondary=post_keywords,
    ...                             back_populates=<span class="hljs-string">'posts'</span>)
    ...
    ...     def __init__(self, headline, body, author):
    ...         self.author = author
    ...         self.headline = headline
    ...         self.body = body
    ...
    ...     def __repr__(self):
    ...         <span class="hljs-built_in">return</span> <span class="hljs-string">"BlogPost(%r, %r, %r)"</span> % (self.headline, self.body, self.author)

    &gt;&gt;&gt; class Keyword(Base):
    ...     __tablename__ = <span class="hljs-string">'keywords'</span>
    ...
    ...     id = Column(Integer, primary_key=True)
    ...     keyword = Column(String(<span class="hljs-number">50</span>), nullable=False, unique=True)
    ...     posts = relationship(<span class="hljs-string">'BlogPost'</span>,
    ...                          secondary=post_keywords,
    ...                          back_populates=<span class="hljs-string">'keywords'</span>)
    ...
    ...     def __init__(self, keyword):
    ...         self.keyword = keyword`</pre>

    在上面的定义中，我们可以发现和OneToMany关系不同，`relationship()`中多了一个`secondary`的参数，这个参数指向了中间表(原文为associated table)。这个中间表只包含了指向多对多关系两侧的表的主键的列。如果这个表包含了其他属性，甚至是自身的主键，SQLAlchemy需要你使用另一种，称为`association object`的机制来处理。

    我们还希望我们的`BlogPost`能够拥有一个`author`属性，这个属性指向我们先前定义的`User`。此时我们需要再定义一个双向关系。由于一个作者可能拥有很多文章，我们希望访问`User.posts`的时候可以加以筛选而不是载入全部的相关文章。为此我们在定义`User.posts`中的时候，设置`lazy='dynamic'`，来控制载入策略。

    <pre class="hljs bash">`&gt;&gt;&gt; B<span class="hljs-built_in">log</span>Post.author = relationship(User, back_populates=<span class="hljs-string">"posts"</span>)
    &gt;&gt;&gt; User.posts = relationship(B<span class="hljs-built_in">log</span>Post, back_populates=<span class="hljs-string">"author"</span>, lazy=<span class="hljs-string">"dynamic"</span>)`</pre>

    然后让我们来创建数据库中对应的表

    <pre class="hljs bash">`&gt;&gt;&gt; Base.metadata.create_all(engine)
    PRAGMA...
    CREATE TABLE keywords (
        id INTEGER NOT NULL,
        keyword VARCHAR(<span class="hljs-number">50</span>) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (keyword)
    )
    ()
    COMMIT
    CREATE TABLE posts (
        id INTEGER NOT NULL,
        user_id INTEGER,
        headline VARCHAR(<span class="hljs-number">255</span>) NOT NULL,
        body TEXT,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES users (id)
    )
    ()
    COMMIT
    CREATE TABLE post_keywords (
        post_id INTEGER NOT NULL,
        keyword_id INTEGER NOT NULL,
        PRIMARY KEY (post_id, keyword_id),
        FOREIGN KEY(post_id) REFERENCES posts (id),
        FOREIGN KEY(keyword_id) REFERENCES keywords (id)
    )
    ()
    COMMIT`</pre>

    多对多关系的使用方法道也没有太大的不同之处。让我们先来给windy添加博文。

    <pre class="hljs bash">`&gt;&gt;&gt; wendy = session.query(User).\
    ...                 filter_by(name=<span class="hljs-string">'wendy'</span>).\
    ...                 one()
    &gt;&gt;&gt; post = B<span class="hljs-built_in">log</span>Post(<span class="hljs-string">"Wendy's Blog Post"</span>, <span class="hljs-string">"This is a test"</span>, wendy)
    &gt;&gt;&gt; session.add(post)`</pre>

    给博文添加一些关键字。目前数据库里面还没有关键字存在，我们创建一些：

    <pre class="hljs bash">`&gt;&gt;&gt; post.keywords.append(Keyword(<span class="hljs-string">'wendy'</span>))
    &gt;&gt;&gt; post.keywords.append(Keyword(<span class="hljs-string">'firstpost'</span>))`</pre>

    我们可以开始查询了。先以'firstpost'为关键字来检索所有的博文。我们使用`any`来查询拥有关键词'firstpost'的博文：

    <pre class="hljs bash">`&gt;&gt;&gt; session.query(B<span class="hljs-built_in">log</span>Post).\
    ...             filter(B<span class="hljs-built_in">log</span>Post.keywords.any(keyword=<span class="hljs-string">'firstpost'</span>)).\
    ...             all()
    [B<span class="hljs-built_in">log</span>Post(<span class="hljs-string">"Wendy's Blog Post"</span>, <span class="hljs-string">'This is a test'</span>, &lt;User(name=<span class="hljs-string">'wendy'</span>, fullname=<span class="hljs-string">'Wendy Williams'</span>, password=<span class="hljs-string">'foobar'</span>)&gt;)]`</pre>

    如果我们希望将查询范围限制在wendy用户所拥有的博文之内，

    <pre class="hljs bash">`&gt;&gt;&gt; session.query(B<span class="hljs-built_in">log</span>Post).\
    ...             filter(B<span class="hljs-built_in">log</span>Post.author==wendy).\
    ...             filter(B<span class="hljs-built_in">log</span>Post.keywords.any(keyword=<span class="hljs-string">'firstpost'</span>)).\
    ...             all()
    SELECT posts.id AS posts_id,
            posts.user_id AS posts_user_id,
            posts.headline AS posts_headline,
            posts.body AS posts_body
    FROM posts
    WHERE ? = posts.user_id AND (EXISTS (SELECT <span class="hljs-number">1</span>
        FROM post_keywords, keywords
        WHERE posts.id = post_keywords.post_id
            AND keywords.id = post_keywords.keyword_id
            AND keywords.keyword = ?))
    (<span class="hljs-number">2</span>, <span class="hljs-string">'firstpost'</span>)
    [B<span class="hljs-built_in">log</span>Post(<span class="hljs-string">"Wendy's Blog Post"</span>, <span class="hljs-string">'This is a test'</span>, &lt;User(name=<span class="hljs-string">'wendy'</span>, fullname=<span class="hljs-string">'Wendy Williams'</span>, password=<span class="hljs-string">'foobar'</span>)&gt;)]`</pre>

    或者我们可以直接在wendy的`posts`属性上进行查询：

    <pre class="hljs bash">`&gt;&gt;&gt; wendy.posts.\
    ...         filter(B<span class="hljs-built_in">log</span>Post.keywords.any(keyword=<span class="hljs-string">'firstpost'</span>)).\
    ...         all()
    [B<span class="hljs-built_in">log</span>Post(<span class="hljs-string">"Wendy's Blog Post"</span>, <span class="hljs-string">'This is a test'</span>, &lt;User(name=<span class="hljs-string">'wendy'</span>, fullname=<span class="hljs-string">'Wendy Williams'</span>, password=<span class="hljs-string">'foobar'</span>)&gt;)]

&nbsp;