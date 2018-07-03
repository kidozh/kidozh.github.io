---
title: '[Django]Model介绍'
tags:
  - Django
  - Python
  - 网页
id: 895
categories:
  - Python
date: 2016-01-26 20:09:36
---

# 前言

模型系统是一种精准的描述你信息的来源。其包含了一些必要的数据以及其操作行为，通常来说，一个模型就是一个单独的数据库中的表。

其中模型系统最基础的是：

*   每个模型都包含了一个Python的子类`django.db.models.Model`的一个类
*   每个模型中的属性都代表着一个数据库字段
*   有着这些，Django就能够赋予你自动创建的数据库API，在[Making Queries](https://docs.djangoproject.com/en/1.9/topics/db/queries/)中可以看到

# 简单的例子

这个例子定义了一个`Person`，其具有`first_name`和`last_name`：
```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```


 `first_name`和`last_name`都是模型之中的字段，每个字段都有一个特定的类属性所确定，每个属性都和一种特定的数据库列所对应。

`Person`这个模型会创建这样的模型：
```pgsql
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```


 需要注意的是：

*   表的名字被自动分配成`myapp_person`，这个表的名字可以从一些模型的元数据中提取，在[Table names](https://docs.djangoproject.com/en/1.8/ref/models/options/#table-names)可以获得更多信息
*   id这一列是自动添加的，但是这个操作能够被重新定义，[Automatic primary key fields](https://docs.djangoproject.com/en/1.8/topics/db/models/#automatic-primary-key-fields)中就有关于自动定义主键的信息
*   `CREATE SQL`在这里面使用的SQL语句是用的PostgreSQL语法，但是还是需要指出的是Django使用的SQL语句是由你在`setting.py`中的数据库后台的设定所指定的

# 使用模型

当你已经定义好模型之后，你需要指定Django需要使用哪些模型，通过编辑你的设置文件以及向`INSTALLED_APPS`的设定中添加包含`models.py`的模组的名字。

举个例子，如果你的应用的模型在`myapp.models`之下（这个包由`manage.py startapp`这个指令所生成），`INSTALLED_APP`一个是这样的：
```python
INSTALLED_APPS = (
    #...
    'myapp',
    #...
)
```


 当你向INSTALLED_APPS之中增加了新的应用之后，一定要确保运行了manage.py migrate，当然第一次应用模型的时候需要使用`manage.py makemigrations`。

# 字段

模型中最重要的一部分就是字段了，字段同时也是模型的一个唯一的必填项，字段有类属性所确定，但是字段的名字最好不要和[模型的API](https://docs.djangoproject.com/en/1.8/ref/models/instances/)相抵触，比如`clean`，`save`或者`delete`。

举个例子：
```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```


## 字段的名字

每个在你的模型中的字段都应该包含一个正确的字段的类的实例，Django会使用字段的名字来确立下列的一些事情：

*   数据库行的类型（比如INTEGER，VARCHAR）
*   渲染表单中字段的时候默认HTML的控件样式（比如<input type="text">, <select>）
*   使用Django管理员的最小的验证需求

Django搭载了许多的内建字段类型，你能够在[模型字段参考](https://docs.djangoproject.com/en/1.8/ref/models/fields/#model-field-types)中找到完整的列表，你也可以轻松的[定义](https://docs.djangoproject.com/en/1.8/ref/models/fields/#model-field-types)你的模型字段。

## 字段的选项

每一个字段都会包含一些列特定的参数（[模型字段参考](https://docs.djangoproject.com/en/1.8/ref/models/fields/#model-field-types)就有）。举个例子`CharField`和其子类都需要一个`max_length`的参数来指定`VARCHAR`的数据字段大小。

这里也有一系列常用的字段参数，所有的都是可选的，在[模型字段参考](https://docs.djangoproject.com/en/1.8/ref/models/fields/#model-field-types)中有详细解释，但是我们还是在这里给出一个小结吧：

### null

如果被置为真值，Django会存储一个NULL的值，默认是假

### blank

如果置为真，字段能够为空。

需要注意的是，这个和null和不一样，null纯粹就是和数据库关联的，而blank却是验证相关的。如果一个字段具有`blank=True`，表单验证会允许一个空值，如果一个字段具有`blank=False`，这个字段就是必填的。

### choices

在这个字段里需要使用一个二元的可迭代的元祖，此时默认的HTML空间将会是一个选择框，并且会限制选项。

这个选择列表是这样的：
```python
YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
)
```


 每个元祖的第一个元素就是会被存储到数据库里的值，第二个会被默认表单控件所展示。当具有一个模型对象的实例的时候，对于选项字段的显示值可以被`get_FOO_display`的方法所操作：
```default
from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
>>> p = Person(name="Fred Flintstone", shirt_size="L")
>>> p.save()
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
'Large'
```


### default

字段的默认值。其可以是一个数值或者一个能够被引用的对象，如果其是一个被引用的对象，当新对象被创建的时候其就能够被调用了

### help_text

多余的帮助文档会在表单控件之中显示，对于文档来说，其非常有用。

### primary_key

如果为真，这个字段就是模型的一个主键了。

如果你没有指定primary_key=True的字段，Django会自动增加一个IntegerField的数字字段来作为主键，所以你不是一定要在某个字段之中设置primary_key=True。当然如果你需要重定义默认主键的行为的话，你就需要定义primary_key=True的字段了。关于这种行为，你可以点击[这里](https://docs.djangoproject.com/en/1.8/topics/db/models/#automatic-primary-key-fields)。

需要注意的是，主键是只读的，如果你变更了现有对象的主键的值然后保存了，这个新对象会在旧对象后创建：
```python
from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
>>> fruit = Fruit.objects.create(name='Apple')
>>> fruit.name = 'Pear'
>>> fruit.save()
>>> Fruit.objects.values_list('name', flat=True)
['Apple', 'Pear']
```


### unique

如果为真，这个字段需要是独一无二的。当然，在[这里](https://docs.djangoproject.com/en/1.8/ref/models/fields/#common-model-field-options)有详细解释。

## 自增的字段

默认的来说，Django会给每个模型这样的模型：
```python
id = models.AutoField(primary_key=True)
```


 这就是一个自增的主键了。

如果你想自定义一个主键，你只需要在你的字段中指定`primary_key=True`即可，如果Django观察到了你已经精准的定义了`Field.primary_key`之后，其就不会添加自增的列了。

每个模型的需要一个自增的字段（除非被精准的定义了或者自动增加一个主键）。

## 自述字段名

每个字段的类别，除了 `ForeignKey`, `ManyToManyField` 和 `OneToOneField`都会要求一个可选的位置参数，也就是一个自述字段名字段名，如果这个字段名没有给定的话，Django就会自动使用字段的名字来创建（字段名中的下划线会被空格所取代）。

在这个例子中，自述字段名就是person's first name：
```python
first_name = models.CharField("person's first name", max_length=30)
```


 在这个例子中，自述字段名就是first name：
```python
first_name = models.CharField(max_length=30)
```


`ForeignKey`, `ManyToManyField`和`OneToOneField`都需要一个模型类作为第一个参数，所以需要使用`verbose_name`作为一个关键字参数。
```python
poll = models.ForeignKey(Poll, verbose_name="the related poll")
sites = models.ManyToManyField(Site, verbose_name="list of sites")
place = models.OneToOneField(Place, verbose_name="related place")
```


 这种规定不会确立`verbose_name`的第一个字母。当必要时，Django会自动确定第一个字母。

## 关系

 关系型数据库的特点就是表之间具有特定的关系，这里，Django提供了三种最常见的数据库关系：多对一，多对多和一对一。

### 多对一关系

我们可以使用`django.db.models.ForeginKey`来定义多对一关系，你可以像其他字段一样，向类之中添加属性来使用这种数据库。

`ForeignKey`需要一个定位参数：一个模型相关的类。

举个例子，对于一辆车来说只有一个制造商，但是制造商可以造很多两车，车和制造商之间就构成了多对一关系。这样就可以使用这样的：
```python
from django.db import models

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    # ...
```


 你也可以创建[递归的关联关系](https://docs.djangoproject.com/en/1.8/ref/models/fields/#recursive-relationships)（recursive relationships，也就是一种对自己的多对一对象）和[关联至尚未定义关系的模型](https://docs.djangoproject.com/en/1.8/ref/models/fields/#lazy-relationships)（relationships to models not yet defined），详情可以见[模型字段参考](https://docs.djangoproject.com/en/1.8/ref/models/fields/#ref-foreignkey)。

`ForeignKey`字段（比如例子中的制造商）应该是小写的模型名称，你可以任意的调用它。
```python
class Car(models.Model):
    company_that_makes_it = models.ForeignKey(Manufacturer)
    # ...
```


同样的，`ForeignKey`字段可以接收一些额外的参数，在[模型字段参考](https://docs.djangoproject.com/en/1.8/ref/models/fields/#foreign-key-arguments)中可以获得详情。这些选项能有助于定义关系工作的方式。

对于后台相关的对象，你可以点击[这里](https://docs.djangoproject.com/en/1.8/topics/db/queries/#backwards-related-objects)。

让我们来举个例子吧！
```python
from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)
```


 下面我们就给出了通过Python API的操作实例：

创建一些记者：
```default
>>> r = Reporter(first_name='John', last_name='Smith', email='john@example.com')
>>> r.save()

>>> r2 = Reporter(first_name='Paul', last_name='Jones', email='paul@example.com')
>>> r2.save()
```


 创建一些文章：
```default
>>> from datetime import date
>>> a = Article(id=None, headline="This is a test", pub_date=date(2005, 7, 27), reporter=r)
>>> a.save()

>>> a.reporter.id
1

>>> a.reporter
<Reporter: John Smith>
```


 现在你必须在其分配一个外键之前就保存这个对象，举个例子，下面就是创建一个没有保存的记者的文章，其会引发`ValueError`：
```default
>>> r3 = Reporter(first_name='John', last_name='Smith', email='john@example.com')
>>> Article.objects.create(headline="This is a test", pub_date=date(2005, 7, 27), reporter=r3)
Traceback (most recent call last):
...
ValueError: save() prohibited to prevent data loss due to unsaved related object 'reporter'.
```


 需要注意的是在Django 1.8.4之前，保存一个没有关联的对象并不会引发异常，这样会引发数据丢失，在1.8-1.8.3之中，没有保存的模型实力不会分配到指定的字段，而且为了更简单使用模型，约束也会被移除。

文章这个对象能够这样被记者这个对象所引用：
```default
>>> r = a.reporter
```


 在Python 2里，其返回的字符是`str`而不是`unicode`的字符串。
```default
>>> r.first_name, r.last_name
('John', 'Smith')
```


通过记者对象来创建一个文章：
```default
>>> new_article = r.article_set.create(headline="John's second story", pub_date=date(2005, 7, 29))
>>> new_article
<Article: John's second story>
>>> new_article.reporter
<Reporter: John Smith>
>>> new_article.reporter.id
1
```


 创建一个文章并且把它加到文章集里：
```default
>>> new_article2 = Article(headline="Paul's story", pub_date=date(2006, 1, 17))
>>> r.article_set.add(new_article2)
>>> new_article2.reporter
<Reporter: John Smith>
>>> new_article2.reporter.id
1
>>> r.article_set.all()
[<Article: John's second story>, <Article: Paul's story>, <Article: This is a test>]
```


 向不同的文章集中增加相同的文章：
```default
>>> r2.article_set.add(new_article2)
>>> new_article2.reporter.id
2
>>> new_article2.reporter
<Reporter: Paul Jones>
```


 向一个集中添加错误的对象会引发异常：
```default
>>> r.article_set.add(r2)
Traceback (most recent call last):
...
TypeError: 'Article' instance expected

>>> r.article_set.all()
[<Article: John's second story>, <Article: This is a test>]
>>> r2.article_set.all()
[<Article: Paul's story>]

>>> r.article_set.count()
2

>>> r2.article_set.count()
1
```


 注意最后一个例子中，文章的作者已经由John变成了Paul。

相关的数据库也支持字段的查找，API会自动遵循你需要的关系，使用双下划线来区分关系，其能够在任意的层面进行工作：
```default
>>> r.article_set.filter(headline__startswith='This')
[<Article: This is a test>]

# Find all Articles for any Reporter whose first name is "John".
>>> Article.objects.filter(reporter__first_name='John')
[<Article: John's second story>, <Article: This is a test>]
```


 也支持精准匹配：
```default
>>> Article.objects.filter(reporter__first_name='John')
[<Article: John's second story>, <Article: This is a test>]
```


 也能支持相关字段的AND查询，这样会自动变成一个和情形在WHERE的语法中：
```default
>>> Article.objects.filter(reporter__first_name='John', reporter__last_name='Smith')
[<Article: John's second story>, <Article: This is a test>]
```


 从相关的查询中，你可以指定一个主键或者精准的过滤掉一些相关的对象：
```default
>>> Article.objects.filter(reporter__pk=1)
[<Article: John's second story>, <Article: This is a test>]
>>> Article.objects.filter(reporter=1)
[<Article: John's second story>, <Article: This is a test>]
>>> Article.objects.filter(reporter=r)
[<Article: John's second story>, <Article: This is a test>]

>>> Article.objects.filter(reporter__in=[1,2]).distinct()
[<Article: John's second story>, <Article: Paul's story>, <Article: This is a test>]
>>> Article.objects.filter(reporter__in=[r,r2]).distinct()
[<Article: John's second story>, <Article: Paul's story>, <Article: This is a test>]
```


 你也能够使用查询集：
```default
>>> Article.objects.filter(reporter__in=Reporter.objects.filter(first_name='John')).distinct()
[<Article: John's second story>, <Article: This is a test>]
```


 反向查询：
```default
>>> Reporter.objects.filter(article__pk=1)
[<Reporter: John Smith>]
>>> Reporter.objects.filter(article=1)
[<Reporter: John Smith>]
>>> Reporter.objects.filter(article=a)
[<Reporter: John Smith>]

>>> Reporter.objects.filter(article__headline__startswith='This')
[<Reporter: John Smith>, <Reporter: John Smith>, <Reporter: John Smith>]
>>> Reporter.objects.filter(article__headline__startswith='This').distinct()
[<Reporter: John Smith>]
```


 获得符合条件对象的个数：
```default
>>> Reporter.objects.filter(article__headline__startswith='This').count()
3
>>> Reporter.objects.filter(article__headline__startswith='This').distinct().count()
1
```


 同样也可以循环查询：
```default
>>> Reporter.objects.filter(article__reporter__first_name__startswith='John')
[<Reporter: John Smith>, <Reporter: John Smith>, <Reporter: John Smith>, <Reporter: John Smith>]
>>> Reporter.objects.filter(article__reporter__first_name__startswith='John').distinct()
[<Reporter: John Smith>]
>>> Reporter.objects.filter(article__reporter=r).distinct()
[<Reporter: John Smith>]
```


 如果你删除了记者，那么他的文章也会被删除（根据`[django.db.models.ForeignKey.on_delete](https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.ForeignKey.on_delete "django.db.models.ForeignKey.on_delete")`在`ForeignKey`中的定义）.
```default
>>> Article.objects.all()
[<Article: John's second story>, <Article: Paul's story>, <Article: This is a test>]
>>> Reporter.objects.order_by('first_name')
[<Reporter: John Smith>, <Reporter: Paul Jones>]
>>> r2.delete()
>>> Article.objects.all()
[<Article: John's second story>, <Article: This is a test>]
>>> Reporter.objects.order_by('first_name')
[<Reporter: John Smith>]
```


 你也可以使用连接的方法构造要求：
```default
>>> Reporter.objects.filter(article__headline__startswith='This').delete()
>>> Reporter.objects.all()
[]
>>> Article.objects.all()
[]
```


### 多对多关系

对于多对多关系，就可以使用`ManyToManyField`，你可以像使用其他字段一样使用它：把它包含到类里面去。

`ManyToManyField`只要一个定位参数：关联模型的类。

举个例子，Pizza有很多配料，配料也可以被用在各种不同的pizza上，所以你可以这样表示他们的关系：
```python
from django.db import models

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)
```


 和`ForeignKey`一样，你也能创建迭代关系，还是老样子，我就不安利了。

这里还是建议（并非强制要求）`ManyToManyField`的名称只是纯粹描述相关模型对象的集合。

哪一个模型包含`ManyToManyField`，并不重要但是你应该至少把它放到其中一个里。

通常来说，`ManyToManyField`实例应该深入到在表单中被编辑的对象中，在上面的例子中，配料（topping）是披萨（Pizza）的一个组成部分（并不是配料具有和pizza的多对多关系）。一旦我们创建了这个模型，Pizza的表单里就会让我们选择配料了。

那么还是看个例子吧！

在这个例子之中我们会使用文章和出版者来举例说明多对多关系。
```python
from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)
```


 下面的操作使用的是Python 的命令行，需要注意的是你现在使用的是一个即时性的多对多关系的模型，有些相关的操作方式可能被禁用了，所以一些例子可能会不使用这个模型。

创建一些Publication：
```default
>>> p1 = Publication(title='The Python Journal')
>>> p1.save()
>>> p2 = Publication(title='Science News')
>>> p2.save()
>>> p3 = Publication(title='Science Weekly')
>>> p3.save()
```


 创建一篇文章：
```default
>>> a1 = Article(headline='Django lets you build Web apps easily')
```


 在你需要关联之前，你应该提前储存这个数据（也就是文章），如果手贱没有保存的话，那么Django就会析出ValueError了：
```default
>>> a1.publications.add(p1)
Traceback (most recent call last):
...
ValueError: 'Article' instance needs to have a primary key value before a many-to-many relationship can be used.
```


 那么就保存吧！
```default
>>> a1.save()
```


 把文章和发行者关联起来：
```default
>>> a1.publications.add(p1)
```


 创建其他的文章，并且添加多个Publication：
```default
>>> a2 = Article(headline='NASA uses Python')
>>> a2.save()
>>> a2.publications.add(p1, p2)
>>> a2.publications.add(p3)
```


 重复添加也是允许的：
```default
>>> a2.publications.add(p3)
```


 而添加一个不正确的类就会析出`TypeError`：
```default
>>> a2.publications.add(a1)
Traceback (most recent call last):
...
TypeError: 'Publication' instance expected
```


 创建并且向文章中增加一个Publication。如果需要一步到位，那么可以使用`create()`函数：
```default
>>> new_publication = a2.publications.create(title='Highlights for Children')
```


文章这个对象能够访问到所有相关的Publication的对象：
```default
>>> a1.publications.all()
[<Publication: The Python Journal>]
>>> a2.publications.all()
[<Publication: Highlights for Children>, <Publication: Science News>, <Publication: Science Weekly>, <Publication: The Python Journal>]
```


 Publication对象可以访问到相关的Article对象：
```default
>>> p2.article_set.all()
[<Article: NASA uses Python>]
>>> p1.article_set.all()
[<Article: Django lets you build Web apps easily>, <Article: NASA uses Python>]
>>> Publication.objects.get(id=4).article_set.all()
[<Article: NASA uses Python>]
```


 多对多关系可以在[跨关系查询](https://docs.djangoproject.com/en/1.8/topics/db/queries/#lookups-that-span-relationships)中获得更多信息。
```default
>>> Article.objects.filter(publications__id=1)
[<Article: Django lets you build Web apps easily>, <Article: NASA uses Python>]
>>> Article.objects.filter(publications__pk=1)
[<Article: Django lets you build Web apps easily>, <Article: NASA uses Python>]
>>> Article.objects.filter(publications=1)
[<Article: Django lets you build Web apps easily>, <Article: NASA uses Python>]
>>> Article.objects.filter(publications=p1)
[<Article: Django lets you build Web apps easily>, <Article: NASA uses Python>]

>>> Article.objects.filter(publications__title__startswith="Science")
[<Article: NASA uses Python>, <Article: NASA uses Python>]

>>> Article.objects.filter(publications__title__startswith="Science").distinct()
[<Article: NASA uses Python>]
```


 `count()`这个函数也能使用`distinct()`的方法：
```default
>>> Article.objects.filter(publications__title__startswith="Science").count()
2

>>> Article.objects.filter(publications__title__startswith="Science").distinct().count()
1

>>> Article.objects.filter(publications__in=[1,2]).distinct()
[<Article: Django lets you build Web apps easily>, <Article: NASA uses Python>]
>>> Article.objects.filter(publications__in=[p1,p2]).distinct()
[<Article: Django lets you build Web apps easily>, <Article: NASA uses Python>]
```


 反向查询也是可以使用的：
```default
>>> Publication.objects.filter(id=1)
[<Publication: The Python Journal>]
>>> Publication.objects.filter(pk=1)
[<Publication: The Python Journal>]

>>> Publication.objects.filter(article__headline__startswith="NASA")
[<Publication: Highlights for Children>, <Publication: Science News>, <Publication: Science Weekly>, <Publication: The Python Journal>]

>>> Publication.objects.filter(article__id=1)
[<Publication: The Python Journal>]
>>> Publication.objects.filter(article__pk=1)
[<Publication: The Python Journal>]
>>> Publication.objects.filter(article=1)
[<Publication: The Python Journal>]
>>> Publication.objects.filter(article=a1)
[<Publication: The Python Journal>]

>>> Publication.objects.filter(article__in=[1,2]).distinct()
[<Publication: Highlights for Children>, <Publication: Science News>, <Publication: Science Weekly>, <Publication: The Python Journal>]
>>> Publication.objects.filter(article__in=[a1,a2]).distinct()
[<Publication: Highlights for Children>, <Publication: Science News>, <Publication: Science Weekly>, <Publication: The Python Journal>]
```


 排除掉一些特定的项目也可以（虽然说相关的SQL语句有一点复杂。。。）
```default
>>> Article.objects.exclude(publications=p2)
[<Article: Django lets you build Web apps easily>]
```


 当我们删除了一个Publication之后，其Article也不能访问它。
```default
>>> p1.delete()
>>> Publication.objects.all()
[<Publication: Highlights for Children>, <Publication: Science News>, <Publication: Science Weekly>]
>>> a1 = Article.objects.get(pk=1)
>>> a1.publications.all()
[]
```


 如果我们删除了Article，那么也是一样的道理：
```default
>>> a2.delete()
>>> Article.objects.all()
[<Article: Django lets you build Web apps easily>]
>>> p2.article_set.all()
[]
```


 也可以通过其他方式来使用多对多关系：
```default
>>> a4 = Article(headline='NASA finds intelligent life on Earth')
>>> a4.save()
>>> p2.article_set.add(a4)
>>> p2.article_set.all()
[<Article: NASA finds intelligent life on Earth>]
>>> a4.publications.all()
[<Publication: Science News>]
```


 也可以使用索引的方法获取某个对象：
```default
>>> new_article = p2.article_set.create(headline='Oxygen-free diet works wonders')
>>> p2.article_set.all()
[<Article: NASA finds intelligent life on Earth>, <Article: Oxygen-free diet works wonders>]
>>> a5 = p2.article_set.all()[1]
>>> a5.publications.all()
[<Publication: Science News>]
```


 从Article中移除一个Publication：
```default
>>> a4.publications.remove(p2)
>>> p2.article_set.all()
[<Article: Oxygen-free diet works wonders>]
>>> a4.publications.all()
[]
```


 另一种姿势：
```default
>>> p2.article_set.remove(a5)
>>> p2.article_set.all()
[]
>>> a5.publications.all()
[]
```


 关系集能够被重新指定，会清除所有现存的集合中的条目：
```default
>>> a4.publications.all()
[<Publication: Science News>]
>>> a4.publications = [p3]
>>> a4.publications.all()
[<Publication: Science Weekly>]
```


 关系也能够被移除：
```default
>>> p2.article_set.clear()
>>> p2.article_set.all()
[]
```


 你也可以以另一种方法移除数据：
```default
>>> p2.article_set.add(a4, a5)
>>> p2.article_set.all()
[<Article: NASA finds intelligent life on Earth>, <Article: Oxygen-free diet works wonders>]
>>> a4.publications.all()
[<Publication: Science News>, <Publication: Science Weekly>]
>>> a4.publications.clear()
>>> a4.publications.all()
[]
>>> p2.article_set.all()
[<Article: Oxygen-free diet works wonders>]
```


 你也可以重新创建关系：
```default
>>> p1 = Publication(title='The Python Journal')
>>> p1.save()
>>> a2 = Article(headline='NASA uses Python')
>>> a2.save()
>>> a2.publications.add(p1, p2, p3)
```


 批量删除Publication应该使用这样的办法：
```default
>>> Publication.objects.filter(title__startswith='Science').delete()
>>> Publication.objects.all()
[<Publication: Highlights for Children>, <Publication: The Python Journal>]
>>> Article.objects.all()
[<Article: Django lets you build Web apps easily>, <Article: NASA finds intelligent life on Earth>, <Article: NASA uses Python>, <Article: Oxygen-free diet works wonders>]
>>> a2.publications.all()
[<Publication: The Python Journal>]
```


 批量删除Article应该使用这样的方法：
```default
>>> q = Article.objects.filter(headline__startswith='Django')
>>> print(q)
[<Article: Django lets you build Web apps easily>]
>>> q.delete()
```


 当删除之后，查询集中的缓存还是要清空：
```default
>>> print(q)
[]
>>> p1.article_set.all()
[<Article: NASA uses Python>]
```


 删除也可以使用这种方法：
```default
>>> p1.article_set = []
>>> p1.article_set.all()
[]

>>> a2.publications = [p1, new_publication]
>>> a2.publications.all()
[<Publication: Highlights for Children>, <Publication: The Python Journal>]
>>> a2.publications = []
>>> a2.publications.all()
[]
```


多对多关系也支持一些额外的可选项，你可以在这里获得参数详情，这些可选项能够帮助定义关系工作的方式。

### 其他多对多关系的字段

当处理一些简单的关系的时候，标准的多对多关系完全能够胜任，然而，有些时候你还是需要在两个模型之间在数据之间确立一些关系。

举个例子，考虑到乐队和歌手的关系，当我们考虑到个人和团队的关系，那么毫无疑问，这是个多对多关系，但是如果要考虑到成员加入的时间的话，那么就需要仔细考虑了。

在这种情况下，Django允许你指定多对多关系，你可以往媒介模型之中加入额外的字段，媒介模型使用`through`的参数指明媒介来关联`ManyToManyField`，在我们的音乐家例子之中，代码应该是这样的：
```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
```


当你指明了媒介模型之后，你就可以精确地指定与多对多关系的外键了。这种精确地关系制订了两个模型之间的相关方式。

对于媒介模型，有以下的限制：

*   你的媒介模型必须有且仅有一个到源模型的外键（在这里就是Group了）。如果你有多余一个的外键或者`through_fields`没有被指定，`validation error`就会被抛出，相同的约束也会作用于目标模板的外键（这里就是person这个模型了）
*   对于通过媒介模型建立的一个具有多对多关系的模型，这里就允许一个模型具有两个外键，但是他们仍然会被当作两个不同的多对多关系。如果有多于两个的外键，你也必须指定`through_fields`，否则也会抛出`validation error`
*   当你需要定义一个从别的模型到自身的多对多关系的时候，你必须使用`symmetrical=False`（在参考里也有说明）

需要指出的是，你已经使用媒介模型（也就是Membership）来建立了你的多对多模型了，你就可以开始创建一些多对多关系了，你可以通过媒介模型来创建实例：
```default
>>> ringo = Person.objects.create(name="Ringo Starr")
>>> paul = Person.objects.create(name="Paul McCartney")
>>> beatles = Group.objects.create(name="The Beatles")
>>> m1 = Membership(person=ringo, group=beatles,
...     date_joined=date(1962, 8, 16),
...     invite_reason="Needed a new drummer.")
>>> m1.save()
>>> beatles.members.all()
[<Person: Ringo Starr>]
>>> ringo.group_set.all()
[<Group: The Beatles>]
>>> m2 = Membership.objects.create(person=paul, group=beatles,
...     date_joined=date(1960, 8, 1),
...     invite_reason="Wanted to form a band.")
>>> beatles.members.all()
[<Person: Ringo Starr>, <Person: Paul McCartney>]
```


 不同于一般的多对多关系，你不能使用`add`，`create`或者是指定的方法来创建关系：
```default
# THIS WILL NOT WORK
>>> beatles.members.add(john)
# NEITHER WILL THIS
>>> beatles.members.create(name="George Harrison")
# AND NEITHER WILL THIS
>>> beatles.members = [john, paul, ringo, george]
```


 为什么我们不能在Person和Group之间创建关系呢？因为你需要指定Membership中的关系详情，简单的`add`，`create`的办法不能提供这些额外的信息，所以他们就在这里被禁用了，那么创建这种关系的唯一方法就是创建媒介模型的实例了。

remove()这种方法也被禁用了，然而`clear()`仍然能够移除实例的所有多对多关系：
```default
>>> # Beatles have broken up
>>> beatles.members.clear()
>>> # Note that this deletes the intermediate model instances
>>> Membership.objects.all()
[]
```


 一旦你已经通过创建媒介模型的实例来建立多对多模型了，你就可以开始查询了，和一般的多对多关系一样，你可以使用查询属性的方法来查询多对多关系。
```default
# Find all the groups with a member whose name starts with 'Paul'
>>> Group.objects.filter(members__name__startswith='Paul')
[<Group: The Beatles>]
```


因为你已经使用了媒介模型，你也可以查询他的属性：
```default
# Find all the members of the Beatles that joined after 1 Jan 1961
>>> Person.objects.filter(
...     group__name='The Beatles',
...     membership__date_joined__gt=date(1961,1,1))
[<Person: Ringo Starr]
```


如果你需要访问成员的信息的话，你也可以使用这种方法：
```default
>>> ringos_membership = Membership.objects.get(group=beatles, person=ringo)
>>> ringos_membership.date_joined
datetime.date(1962, 8, 16)
>>> ringos_membership.invite_reason
'Needed a new drummer.'
```


 当然也有通过多对多反向查询的方法获取信息的例子：
```default
>>> ringos_membership = ringo.membership_set.get(group=beatles)
>>> ringos_membership.date_joined
datetime.date(1962, 8, 16)
>>> ringos_membership.invite_reason
'Needed a new drummer.'
```


###  一对一关系

为了定义对一对关系，我们可以使用`OneToOneField`，你可以像使用别的字段一样使用它。

当这个对象需要延伸到别的对象的时候，这个对象最有用的就是主键了。

`OneToOneField`只有一个位置参数：相关模型的类。

举个例子，如果你正在创建一个位置的数据库的话，你就可能需要地址，座机号等数据。然后如果你想创建一个当地的餐馆的数据库的话，为了不重复，你就可以使Restaurant具有一个到Place的`OneToOneField`的字段（因为餐馆还是一个地方，事实上，你也可以使用继承的办法来思考这个问题，实际上也是精准的说明了一对一关系）。

`OneToOneField`也接受一个特定的可选参数parent_link参数，[这里](https://docs.djangoproject.com/en/1.8/ref/models/fields/#ref-onetoone)也有详细说明。

`OneToOneField`这个类在以前会自动成为模型中的主键，但是现在就不会是事实了。现在你可以在一个域里面包含多个一对一的字段。

那么还是举个例子吧：

在这个例子里，一个Place可以有一个Restaurant：
```default
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(Place, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=50)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the waiter at %s" % (self.name, self.restaurant)
```


 现在下面就是可以使用Python命令行来演示的例子了。

创建一个地点：
```default
>>> p1 = Place(name='Demon Dogs', address='944 W. Fullerton')
>>> p1.save()
>>> p2 = Place(name='Ace Hardware', address='1013 N. Ashland')
>>> p2.save()
```


 创建一个餐厅，通过“父”对象作为这个对象的id：
```default
>>> r = Restaurant(place=p1, serves_hot_dogs=True, serves_pizza=False)
>>> r.save()
```


 通过餐厅可以访问这个地址：
```default
>>> r.place
<Place: Demon Dogs the place>
```


 p2并没有相关的餐厅的例子：
```default
>>> from django.core.exceptions import ObjectDoesNotExist
>>> try:
>>>     p2.restaurant
>>> except ObjectDoesNotExist:
>>>     print("There is no restaurant here.")
There is no restaurant here.
```


 你也可以使用`hasattr`的方法来避免抛出异常：
```default
>>> hasattr(p2, 'restaurant')
False
```


 使用`=`的方法来分配位置，由于Restaurant的主键是place，所以当保存的时候，新的餐厅就会被创建了：
```default
>>> r.place = p2
>>> r.save()
>>> p2.restaurant
<Restaurant: Ace Hardware the restaurant>
>>> r.place
<Place: Ace Hardware the place>
```


 你可以使用相反的方法来指定地点：
```default
>>> p1.restaurant = r
>>> p1.restaurant
<Restaurant: Demon Dogs the restaurant>
```


 需要注意的是，你必须在分配一对一关系之后保存对象，举个例子，创建一个没有保存地点的餐馆就会抛出`ValueError`：
```default
>>> p3 = Place(name='Demon Dogs', address='944 W. Fullerton')
>>> Restaurant.objects.create(place=p3, serves_hot_dogs=True, serves_pizza=False)
Traceback (most recent call last):
...
ValueError: save() prohibited to prevent data loss due to unsaved related object 'place'.
```


 需要指出的是，1.8-1.8.3的版本中，当上述情况发生的时候，没有保存的模型实例不会保存到相关的字段内，但是为了更简单的使用内存数据库模型这种局限性也会被移除。

Restaurant.objects.all()会返回Restaurant的对象，需要注意的是我们现在有两个餐厅（Ace Hardware the Restaurant是由r.place=p2所创建的）
```default
>>> Restaurant.objects.all()
[<Restaurant: Demon Dogs the restaurant>, <Restaurant: Ace Hardware the restaurant>]
```


 Place.objects.all()会返回所有的Places的对象，无论其是否有餐馆：
```default
>>> Place.objects.order_by('name')
[<Place: Ace Hardware the place>, <Place: Demon Dogs the place>]
```


 你也可以通过跨关系查询的方法查询模型：
```default
>>> Restaurant.objects.get(place=p1)
<Restaurant: Demon Dogs the restaurant>
>>> Restaurant.objects.get(place__pk=1)
<Restaurant: Demon Dogs the restaurant>
>>> Restaurant.objects.filter(place__name__startswith="Demon")
[<Restaurant: Demon Dogs the restaurant>]
>>> Restaurant.objects.exclude(place__address__contains="Ashland")
[<Restaurant: Demon Dogs the restaurant>]
```


 反过来查询也是可以的：
```default
>>> Place.objects.get(pk=1)
<Place: Demon Dogs the place>
>>> Place.objects.get(restaurant__place=p1)
<Place: Demon Dogs the place>
>>> Place.objects.get(restaurant=r)
<Place: Demon Dogs the place>
>>> Place.objects.get(restaurant__place__name__startswith="Demon")
<Place: Demon Dogs the place>
```


 向Restaurant中添加一个Waitor
```default
>>> w = r.waiter_set.create(name='Joe')
>>> w.save()
>>> w
<Waiter: Joe the waiter at Demon Dogs the restaurant>
```


 查询waitor：
```default
>>> Waiter.objects.filter(restaurant__place=p1)
[<Waiter: Joe the waiter at Demon Dogs the restaurant>]
>>> Waiter.objects.filter(restaurant__place__name__startswith="Demon")
[<Waiter: Joe the waiter at Demon Dogs the restaurant>]
```


## 跨文件引用模型

很简单，只要使用类似于下面的方法就可以了：
```default
from django.db import models
from geography.models import ZipCode

class Restaurant(models.Model):
    # ...
    zip_code = models.ForeignKey(ZipCode)
```


## 字段名约束

Django只会对字段名给两个约束：

1.  字段名称不能使Python的保留字段，因为这样会引发Python的语法错误：

    ```python
class Example(models.Model):
    pass = models.IntegerField() # 'pass' is a reserved word!
```

2.  因为Django查询方式，字段名不能包含多余一个的下划线。
```python
class Example(models.Model):
    foo__bar = models.IntegerField() # 'foo__bar' has two underscores!
```


因为你的字段名并不是一定会匹配到你数据库的列名称，这些限制还是能够工作的。你可以在[db_column](https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.Field.db_column)选项中获得更多信息。

SQL的保留字，比如`join`，`where`或者`select`是可以作为字段名的吗因为Django会编码所有的表的名称和列的名称，他会使用你数据库中的引用语法来工作。

## 自定义字段类型

如果现有的字段不能满足你的需求的话，你可以自定义字段。你可以点击[这里](https://docs.djangoproject.com/en/1.8/howto/custom-model-fields/)获得更多自定义字段的类型。

# 元选项

你可以使用内置的`Meta`类来描述模型的元数据。
```default
from django.db import models

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"
```


 模型的元数据可以是除了字段的任何的东西。比如排序，表名或者自述名。所有的都是不必须的，Meta这个类也是对于模型类的一个不必须的存在。

在[这里](https://docs.djangoproject.com/en/1.8/ref/models/options/)你可以获得更多元选项的详情。

# 模型属性

## objects

一个模型最重要的属性就是`Manager`了，它也是数据库查询操作的一个接口，如果没有定义`Manager`，那么默认的名称就是`objects`了，`Manager`只能通过模型类而不是模型实例来获得。

# 模型方式

你可以通过向一个模型中自定义方法来增加一个自定义的列级别的功能。当Manager的方法能够行使表级别的事情，模型方式应该对特定模型实例做出响应。
```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)
```


在这个例子之中最后的方法就是property。

[模型实例参考](https://docs.djangoproject.com/en/1.8/ref/models/instances/)中有一个完全的[列表](https://docs.djangoproject.com/en/1.8/ref/models/instances/#model-instance-methods)。你可以重写[大多数的方法](https://docs.djangoproject.com/en/1.8/topics/db/models/#overriding-predefined-model-methods)，但是这里有一些你可能经常会用到的方法：

## __str__()（Python 3）

Python 3之中你也可以使用`__unicode__()`的方法来取代

## __unicode__()（Python 2）

python 的一个奇妙的方法就是就是返回一串使用`unicode`描述对象的字符串，这也是Python和Django会使用的。在绝大多数的情况下，在管理员站点之中，当你想要描述对象的时候，这个函数就会使用了。

作为开发者你还是定义这个方法比较好一点，因为默认的方法一点也不好用。。。

## get_absolute_url()

这个函数会告诉Django如何去计算实例的URL，Django会在管理员界面之中使用这个函数。

所有具有独一无二地址的对象都需要定义这个方法。

## 复写预定义的模型方法

当然这里也有其他的方法来封装一系列你想自定义的数据行为。更有甚者，你需要频繁的变更`save()`和`delete()`函数的内容。

你可以任意的变更这种行为。

一个经典的方法就是在类之中内建方法：
```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        do_something()
        super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.
        do_something_else()
```


 你也可以防止某些情形下的保存操作：
```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        if self.name == "Yoko Ono's blog":
            return # Yoko shall never have her own blog!
        else:
            super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.
```


 记得使用超级类的方法在开发中很重要，这就是super(Blog, self).save(*args, **kwargs) 的活了，为了确保对象真正的保存到数据库之中，如果你忘记了，那么默认的保存操作并不会发生，数据库也不会被连接。

需要注意的是参数也是很重要的，Django将会延伸内建模型方法的能力，如果你需要在定义模型的时候使用`*args`和`**kwargs`，你需要保证代码会支持这些操作。

需要注意的是，当大规模的删除操作使用的时候，`delete()`的并不是一定需要调用的，为了确保自定义的操作逻辑被确立了，你可以使用`pre_delete`或者`post_delete`的方法。不幸的是，大规模创建或者更新对象的时候并没有`save()`，`pre_save`或者`post_save`被调用。

# 执行自定义的SQL

使用原生的SQL，你可以参考文件[使用原生SQL](https://docs.djangoproject.com/en/1.8/topics/db/sql/)。

# 模型的继承

在Django之中模型的继承是非常重要的，但是基本的原则仍然应该被引用。这也就是说，基础类必须具有这个`django.db.models.Model`类。

Django之中有三种继承方法：

1.  通常来说，你需要使用父类来容纳你并不想输出所有子类的信息，这个类并不会独立使用，所以基于抽象的类就是你需要使用的。
2.  如果你需要使用一个现存的子类并且想要每个模型建立自身的表，那么多表格继承是需要的。
3.  最后，如果你只需要编辑Python层面上的行为的话而不变更模型字段的话，你就可以使用[代理模型](https://docs.djangoproject.com/en/1.8/topics/db/models/#proxy-models)。

## 抽象类

抽象类在你需要把一些常用信息放置到其他模型之中是非常有用的，你可以编写你的基类并且在Meta类之中放置`abstract=True`。这个模型并不会创建任何的数据库表。然而当基类在别的类中开始受用的时候，其字段就会在子类中显示。所以，子类和抽象类中含有相同字段就会抛出异常。

举个例子吧：
```python
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
```


 学生这个模型就会有三个类name,age,home_group。由于抽象基类的存在，`CommonInfo`这个模型不会视为一般的类。其不会创建一个数据表或者分配一个manager并且也不会实例化或者直接保存。

对于许多的用途来说，模型实例的类型会被提取。其能够提供一个基于Python层面上的常规信息的代理。

### 抽象类的继承

当抽象基类被创建了，Django就会在你声明的基类的`Meta`中获取到一个信息。如果子类没有声明自己的基类，他就会继承父的元信息。如果子需要延伸父的元类，其就能够继承他：
```python
from django.db import models

class CommonInfo(models.Model):
    # ...
    class Meta:
        abstract = True
        ordering = ['name']

class Student(CommonInfo):
    # ...
    class Meta(CommonInfo.Meta):
        db_table = 'student_info'
```


 Django会对抽象类调整自己的meta类：在安装了`Meta`属性之后，他就会将`abstract`置为`False`，这也意味着抽象类的子类不会自动成为子类。当然你也可以写一个继承自其他抽象类的抽象类，这样的话你需要每次都精确的置`abstract=True`。

### 需要对related_name谨慎

如果你对`ForeignKey`或者`ManyToManyField`使用了`related_name`属性，你需要制定一个独一无二的字段保留名。这样就会引发一个一般性的错误。

为了解决这个问题，当你只在抽象基类使用`related_name`的时候，你的应用名称必须包含`'%(app_label)s'`和`'%(class)s'`

*   '%(class)s'需要有子类的小写的名称所取代
*   '%(app_label)s'会被小写的应用名称所取代。每个安装好的应用都必须独一无二，模型类名字也需要是独二无而的

举个例子，在common/models.py中分配应用：
```python
from django.db import models

class Base(models.Model):
    m2m = models.ManyToManyField(OtherModel, related_name="%(app_label)s_%(class)s_related")

    class Meta:
        abstract = True

class ChildA(Base):
    pass

class ChildB(Base):
    pass
```


 当然这里还有其他的应用：
```python
from common.models import Base

class ChildB(Base):
    pass
```


 The reverse name of the <tt>common.ChildA.m2m</tt> field will be <tt>common_childa_related</tt>, whilst the reverse name of the<tt>common.ChildB.m2m</tt> field will be <tt>common_childb_related</tt>, and finally the reverse name of the <tt>rare.ChildB.m2m</tt> field will be <tt>rare_childb_related</tt>. It is up to you how you use the <tt>'%(class)s'</tt> and <tt>'%(app_label)s</tt> portion to construct your related name, but if you forget to use it, Django will raise errors when you perform system checks (or run [<tt>migrate</tt>](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-migrate)).

If you don’t specify a [<tt>related_name</tt>](https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") attribute for a field in an abstract base class, the default reverse name will be the name of the child class followed by <tt>'_set'</tt>, just as it normally would be if you’d declared the field directly on the child class. For example, in the above code, if the [<tt>related_name</tt>](https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") attribute was omitted, the reverse name for the <tt>m2m</tt> field would be <tt>childa_set</tt> in the<tt>ChildA</tt> case and <tt>childb_set</tt> for the <tt>ChildB</tt> field.

（- -翻译不下来了。。。。）

## 多重继承

由Django支持的第二种继承模型。每个模型都对应着自己的数据库表并且能够单独的查询和创建。这种继承关系会在子模型和父模型之间建立联系（通过自动创建的`OneToOneField`），举个例子：
```python
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
```


 尽管数据能够归属于不同的数据库表，所有Place字段的仍然会被Restaurant所获取。
```default
>>> Place.objects.filter(name="Bob's Cafe")
>>> Restaurant.objects.filter(name="Bob's Cafe")
```


 如果你具有一个是Restaurant和Place，你也能够使用小写版本的模型名称来获取从Place对象到Restaurant对象。
```default
>>> p = Place.objects.get(id=12)
# If p is a Restaurant object, this will give the child class:
>>> p.restaurant
<Restaurant: ...>
```


 然而，如果在上面的p不是Restaurant的话，将会抛出一个`Restaurant.DoesNotExist`的异常。

### 元数据和多重继承

在多表格继承之中，子类继承父类的`Meta`类是没有意义的。所有的在父类之中应用的Meta选项可能与子选项发生矛盾。

所以子模型无法访问到父类的`Meta`类，然而，这里仍有一些例外：如果子类并没有指定`ordering`或者`get_latest_by`的属性的话，他就会继承父类的属性：

如果父类有一个ordering而你又不想子类有排序方式的话，你可以这样：
```python
class ChildModel(ParentModel):
    # ...
    class Meta:
        # Remove parent's ordering effect
        ordering = []
```


## 继承和保留关系

由于多表格继承都会使用`OneToOneField`来指明父子关系，所以在下面的例子中，子类和父类也是可以脱离的。然而，这也会使用默认的为外键和多对多字段的`related_name`。如果你把这些关系放在了父节点的子类中，你需要在每个字段里都要指定`related_name`，如果你忘记了这一点的话，Django也会抛出一个`Validation error`让你长记性的。

举个例子，再次使用Place这个类的时候，让我们创建另一个带有多对多字段的子类：
```python
class Supplier(Place):
    customers = models.ManyToManyField(Place)
```


 这样就会析出异常：
```default
Reverse query name for 'Supplier.customers' clashes with reverse query
name for 'Supplier.place_ptr'.

HINT: Add or change a related_name argument to the definition for
'Supplier.customers' or 'Supplier.place_ptr'.
```


 所以在自定义字段中需要使用`related_name`来解决这个问题：models.ManyToManyField(Place, related_name='provider'). 

## 指定父链接字段

上面我们提到了，Django会自动创建一个`OneToOneField`来连接子类和一个不为抽象的父模型。如果你想控制连接到父模型的属性名称的话，你也可以创建一个`OneToOneField`并且设置`parent_link=True`来指明你回溯到父类的字段。

# 代理模型

当使用多表格继承中，每个模型的子类都会创建一个数据库的表。因为子类需要存储基类中无法表达的字段，所以这常常是合理的。有的时候你还是需要更改Python的模型行为：有可能是变更默认的管理器或者新增一种方法。

这就是代理模型做的事情了：为原始的模型创建一个代理模型，你就能创建，删除或者改变代理模型的实例，但是原始模型的数据仍然是保存好了的。不同电视你可以像变更默认模型那样在代理中修改数据而并不需要变更原始数据。

代理模型的声明就和一般模型一样：你可以通过在Meta类中设置`proxy=True`来达到这个目的。

举个例子，如果你想向Person模型中添加一种方式的话，你这样使用：
```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        # ...
        pass
```


 MyPerson这个类就能像父类Person那样操作数据表。特殊的说，任何的Person实例都能通过MyPerson一样访问：
```python
>>> p = Person.objects.create(first_name="foobar")
>>> MyPerson.objects.get(first_name="foobar")
<MyPerson: foobar>
```


 你也可以使用代理模型来定义一个不同默认的排序方式的模型，你可能并不想去指明Person模型的排序方式，但是通常来说你可以在使用代理模型的时候指定他：
```python
class OrderedPerson(Person):
    class Meta:
        ordering = ["last_name"]
        proxy = True
```


 现在一般的Person查询仍然是无序的，但是`OrderedPerson`的查询将会按照`last_name`所排序。

## 基类限制

代理模型必须精准的继承于一个非抽象模型类，你不能由多个非抽象模型中继承，因为代理模型不会在不同表的行之间建立任何联系。代理模型可以继承于任意个抽象模型，因为他们并没有定义任何模型字段。

## 代理模型管理器

如果你对代理模型没有指定任何模型管理器的话，它就会从父模型之中继承管理器，如果你在代理模型之中定义了管理器，那么它就会成为一个默认的管理器，然而所有在父类之中定义的管理器仍然是使用的。

那么接下来下面的例子，你就能在查询Person这个模型的时候变更默认管理器。
```python
from django.db import models

class NewManager(models.Manager):
    # ...
    pass

class MyPerson(Person):
    objects = NewManager()

    class Meta:
        proxy = True
```


 如果你想向代理模型中新增管理器的话，你这样在自定义管理器里所讲的这样：创建一个含有NewManager的基类，然后再基类中继承就可以了：
```python
# Create an abstract class for the new manager.
class ExtraManagers(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True

class MyPerson(Person, ExtraManagers):
    class Meta:
        proxy = True
```


 你可能对这项技能不常用，但是存在即合理嘛。

## 代理继承和非托管模型的区别

代理 model 继承看上去和使用<tt>Meta</tt>类中的 [<tt>managed</tt>](http://python.usyiyi.cn/django_182/ref/models/options.html#django.db.models.Options.managed "django.db.models.Options.managed") 属性的非托管 model 非常相似。但两者并不相同，使用时选用哪种方案是一个值得考虑的问题。

一个不同之处是你可以在<tt>Meta.managed=False</tt>的 model 中定义字段(事实上，是必须指定，除非你真的想得到一个空 model )。在创建非托管 model 时要谨慎设置[<tt>Meta.db_table</tt>](http://python.usyiyi.cn/django_182/ref/models/options.html#django.db.models.Options.db_table "django.db.models.Options.db_table") ，这是因为创建的非托管 model 映射某个已存在的 model ，并且有自己的方法。因此，如果你要保证这两个 model 同步并对程序进行改动，那么就会变得繁冗而脆弱。

另一个不同之处是两者对 管理器的处理方式不同。 代理 model 要与它所代理的 model 行为相似，所以代理 model 要继承父 model 的 managers ，包括它的默认 manager 。 但在普通的多表继承中，子类不能继承父类的 manager ，这是因为在处理非基类字段时，父类的 manager 未必适用。 后一种情况在 [管理器文档](http://python.usyiyi.cn/django_182/topics/db/managers.html#custom-managers-and-inheritance)有详细介绍。

我们实现了这两种特性之后，曾尝试把两者结合到一起。 结果证明，宏观的继承关系和微观的 管理器揉在一起，不仅导致 API 复杂难用，而且还难以理解。 由于任何场合下都可能需要这两个选项，所以目前二者仍是各自独立使用的。

所以，一般规则是：

1.  如果你要借鉴一个已有的 模型或数据表，且不想涉及所有的原始数据表的列，那就令 <tt style="line-height: 1.42857;">Meta.managed=False</tt>。通常情况下，对模型数据库创建视图和表格不需要由 Django 控制时，就使用这个选项。
2.  如果你想对 model 做 Python 层级的改动，又想保留字段不变，那就令 <tt>Meta.proxy=True</tt>。因此在数据保存时，代理 model 相当于完全复制了原始 模型的存储结构。

## 多重继承

就像Python的子类那样，DJango的模型可以继承自多个父类模型。切记一般的Python名称解析规则也会适用。出现特定名称的第一个基类(比如[Meta](http://python.usyiyi.cn/django_182/topics/db/models.html#meta-options))是所使用的那个。例如，这意味着如果多个父类含有 [Meta](http://python.usyiyi.cn/django_182/topics/db/models.html#meta-options)类，只有第一个会被使用，剩下的会忽略掉。

一般来说，你并不需要继承多个父类。多重继承主要对“mix-in”类有用：向每个继承mix-in的类添加一个特定的、额外的字段或者方法。你应该尝试将你的继承关系保持得尽可能简洁和直接，这样你就不必费很大力气来弄清楚某段特定的信息来自哪里。

Django 1.7之前，继承多个含有<tt>id</tt>主键字段的模型不会抛出异常，但是会导致数据丢失。例如，考虑这些模型（由于<tt>id</tt>字段的冲突，它们不再有效）：
```python
class Article(models.Model):
    headline = models.CharField(max_length=50)
    body = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=50)

class BookReview(Book, Article):
    pass
```


 这段代码展示了如何创建子类的对象，并覆写之前创建的父类对象中的值。
```default
>>> article = Article.objects.create(headline='Some piece of news.')
>>> review = BookReview.objects.create(
...     headline='Review of Little Red Riding Hood.',
...     title='Little Red Riding Hood')
>>>
>>> assert Article.objects.get(pk=article.pk).headline == article.headline
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AssertionError
>>> # the "Some piece of news." headline has been overwritten.
>>> Article.objects.get(pk=article.pk).headline
'Review of Little Red Riding Hood.'
```


 你可以在模型基类中使用显式的[<tt>AutoField</tt>](http://python.usyiyi.cn/django_182/ref/models/fields.html#django.db.models.AutoField "django.db.models.AutoField")来合理使用多重继承：
```default
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    ...

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    ...

class BookReview(Book, Article):
    pass
```


 或者是使用一个父类来持有[<tt>AutoField</tt>](http://python.usyiyi.cn/django_182/ref/models/fields.html#django.db.models.AutoField "django.db.models.AutoField")：
```default
class Piece(models.Model):
    pass

class Article(Piece):
    ...

class Book(Piece):
    ...

class BookReview(Book, Article):
    pass
```


##  字段名hiding不被允许

普通的 Python 类继承允许子类覆盖父类的任何属性。 但在 Django 中，重写 [<tt>Field</tt>](http://python.usyiyi.cn/django_182/ref/models/fields.html#django.db.models.Field "django.db.models.Field")实例是不允许的(至少现在还不行)。如果基类中有一个 <tt>author</tt>字段，你就不能在子类中创建任何名为 <tt>author</tt>的字段。

重写父类的字段会导致很多麻烦，比如：初始化实例(指定在 <tt>Model.__init__</tt> 中被实例化的字段) 和序列化。而普通的 Python 类继承机制并不能处理好这些特性。所以 Django 的继承机制被设计成与 Python 有所不同，这样做并不是随意而为的。

这些限制仅仅针对做为属性使用的 [<tt>Field</tt>](http://python.usyiyi.cn/django_182/ref/models/fields.html#django.db.models.Field "django.db.models.Field")实例，并不是针对 Python 属性，Python 属性仍是可以被重写的。 在 Python 看来，上面的限制仅仅针对字段实例的名称：如果你手动指定了数据库的列名称，那么在多重继承中，你就可以在子类和某个祖先类当中使用同一个列名称。(因为它们使用的是两个不同数据表的字段)。

如果你在任何一个祖先类中重写了某个 model 字段，Django 都会抛出 [<tt>FieldError</tt>](http://python.usyiyi.cn/django_182/ref/exceptions.html#django.core.exceptions.FieldError "django.core.exceptions.FieldError")异常。


另见
<dl><dt>[模型参考](http://python.usyiyi.cn/django_182/ref/models/index.html)</dt><dd>涵盖模型相关的API，包括模型字段、关联对象和<tt>查询集</tt>。</dd></dl>

 