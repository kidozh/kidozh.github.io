---
title: '[Django]模型字段参考'
tags:
  - Django
  - Python
  - 网页
id: 933
categories:
  - Python
date: 2016-02-01 17:30:09
---

# 前言

本文档包含了Django提供的全部模型字段的字段选项 和 字段类型的API参考。

如果内建的字段不能满足你的需要，你可以尝试对特定国家和文化有效的包含配套代码的 [django-localflavor](https://django-localflavor.readthedocs.org/)。当然，你也可以很容易的编写你自定义的字段。

严格意义上来讲， model 是定义在`django.db.models.fields`里面，但为了使用方便，它们被导入到 `django.db.models`中；标准上，我们导入from django.db import models ，然后使用 `models.<Foo>Field`的形式使用字段。

# 字段选项

下列参数是全部字段类型都可用的，都是可选的。

## null

`Field.null`

如果为`True`，Django 将空值以`NULL` 存储到数据库中。默认值是 `False`。

字符串字段例如`CharField` 和`TextField` 要避免使用`null`，因为空字符串值将始终储存为空字符串而不是`NULL`。如果字符串字段的`null=True`，那意味着对于“无数据”有两个可能的值：`NULL` 和空字符串。在大多数情况下，对于“无数据”声明两个值是赘余的，Django 的惯例是使用空字符串而不是`NULL`。

无论是字符串字段还是非字符串字段，如果你希望在表单中允许空值，你将还需要设置`blank=True`，因为null 仅仅影响数据库存储（参见[blank](http://python.usyiyi.cn/django_182/ref/models/fields.html#django.db.models.Field.blank)）。

注意：

在使用Oracle 数据库时，数据库将存储`NULL` 来表示空字符串，而与这个属性无关。

如果你希望`BooleanField` 接受null 值，请用 `NullBooleanField` 代替。

## blank

`Field.blank`

如果为`True`，则该字段允许为空白。 默认值是 `False`。

注意它与`null`不同。`null` 纯粹是数据库范畴的概念，而`blank` 是数据验证范畴的。如果字段设置`blank=True`，表单验证时将允许输入空值。如果字段设置`blank=False`，则该字段为必填。

## choices

`Field.choices`

它是一个可迭代的结构(比如，列表或是元组)，由可迭代的二元组组成(比如[(A, B), (A, B) ...] )，用来给这个字段提供选择项。如果设置了 `choices` ，默认表格样式就会显示选择框，而不是标准的文本框，而且这个选择框的选项就是 `choices` 中的元组。

每个元组中的第一个元素，是存储在数据库中的值；第二个元素是该选项更易理解的描述。 比如:
```python
YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
)
```


 一般来说，最好在模型类内部定义`choices`，然后再给每个值定义一个合适名字的常量。
```python
from django.db import models

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(max_length=2,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=FRESHMAN)

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)
```


 尽管你可以在模型类的外部定义choices然后引用它，在模型类中定义choices和其每个`choice`的name可以保存所有的关于应用到此信息的类的信息， 也使得choices更容易被应用（例如， `Student.SOPHOMORE` 可以在任何引入Student 模型的位置生效)。

你也可以归类可选的`choices`到已命名的组中用来达成组织整理的目的:
```python
MEDIA_CHOICES = (
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
)
```


 每个元组的第一个元素是组的名字。第二个元素是一组可迭代的二元元组，每一个二元元组包含一个值和一个给人看的名字构成一个选项。分组的选项可能会和未分组的选项合在同一个`list`中。 （就像例中的`unknown`选项）。

对于每个有choices set的模型字段, Django 将会加入一个通过该字段现在的值取回给人看的名字的方法。参见数据库API文档中的`get_FOO_display()`。

请注意`choices`可以是任何可迭代的对象 – 不是必须是列表或者元组。这一点使你可以动态的构建`choices`。但是如果你发现你自己搞不定动态的`choices`，你最好还是使用`ForeignKey`来构建一个合适的数据库表。`choices`意味着那些变动不多的静态数据，如果有的（变动）话。

除非字段中默认了`blank=False`，那么`---------`就会在选择框中被渲染出来。你也可以向元祖中添加一个包含`None`的`choices`来覆盖这个行为（比如：`(None, 'Your String For Display')`）。

## db_column

`Field.db_column`

数据库中用来表征该字段的名称。如果未指定，那么Django将会使用`Field`名作为字段名.

如果你的数据库列名为SQL语句的保留字，或者是包含不能作为Python 变量名的字符，很明显地如连字符，仍然可以的。Django 会在后台给列名和表名加上双引号。

## db_index

`Field.db_index`

若值为 `True`, 则 `django-admin sqlindexes` 将会为此字段输出 `CREATE INDEX` 语句。（译注：为此字段创建索引）

## db_tablespace

`Field.db_tablespace`

如果该字段有索引的话，`database tablespace`的名称用作该字段的索引。 如果`DEFAULT_INDEX_TABLESPACE` 已经设置，则默认值是由`DEFAULT_INDEX_TABLESPACE`指定, 如果没有设置则由 `db_tablespace` 指定。如果后台数据库不支持表空间，或者索引，则该选项被忽略。

## default

`Field.default`

该字段的默认值. 它可以是一个值或者一个可调用对象. 如果是一个可调用对象，那么在每一次创建新对象的时候，它将会调用一次.

这个默认值不可以是一个可变对象（如字典，列表，等等）,因为对于所有模型的一个新的实例来说，它们指向同一个引用。或者，把他们包装为一个可调用的对象。例如，你有一个自定义的`JSONField`，并且想指定一个特定的字典值，可以如下使用：
```python
def contact_default():
    return {"email": "to1@example.com"}

contact_info = JSONField("ContactInfo", default=contact_default)
```


 请注意`lambdas` 函数不可作为如 `default` 这类可选参数的值.因为它们无法被 `migrations`命令序列化. 请参见文档其他部分。

默认值会在新实例创建并且没有给该字段提供值时使用。如果字段为主键，默认值也会在设置为<!--more-->`None`时使用。

`Changed in Django 1.8:`

之前的版本不会使用`None`作为主键 

## editable

`Field.editable`

如果为`False`, 这个字段将不会出现在` admin `或者其他 `ModelForm`. 他们也会跳过 模型验证. 默认是`True`.

## error_messages

`Field.error_messages`

`error_messages` 参数能够让你重写默认抛出的错误信息。通过指定` key `来确认你要重写的错误信息。

`error_messages` 的 `key` 值包括 `null`, `blank`, `invalid`, `invalid_choice`, `unique`, 和 `unique_for_date`. 其余的 `error_messages` 的 `keys` 是不一样的在不同的章节下 `Field types` 。

`New in Django 1.7.`

这个 `unique_for_date` 的 `error_messages` 的`key` 是在 1.7 中加的。

## help_text

`Field.help_text`

额外的 ‘`help`' 文本被显示在表单控件中  `form`。如果你没有字表单字段中使用，它对文档事件很有帮助。

注意这 不 会自动添加 `HTML` 标签。需要你在 `help_text` 包含自己需要的格式。例如:
```python
help_text="Please use the following format: <em>YYYY-MM-DD</em>."
```


另外, 你可以使用简单文本和`django.utils.html.escape()`以避免任何HTML特定的字符。为了防止CSRF攻击，需要保证来自不可信用户的所有的帮助文本能够被编码。

## primary_key

`Field.primary_key`

若为 <!--more-->`True`, 则该字段会成为模型的主键字段。

如果你没有在模型的任何字段上指定 `primary_key=True`, Django会自动添加一个 `AutoField` 字段来充当主键。 所以除非你想要覆盖默认的主键行为，否则不需要在任何字段上设定`primary_key=True` 。更多内容 请参考[Automatic primary key fields](http://python.usyiyi.cn/django_182/topics/db/models.html#automatic-primary-key-fields).

`primary_key=True` 暗含着`null=False` 和`unique=True`. 一个对象上只能拥有一个主键.

主键字段是只读的。如果你改变了一个已存在对象上的主键并且保存的话，会创建一个新的对象，而不是覆盖旧的.

## unique

`Field.unique`

如果为 `True`, 这个字段在表中必须有唯一值.

这是一个在数据库级别的强制性动作,并且通过模型来验证。如果你试图用一个重复的值来保存`unique` 字段，那么一个`django.db.IntegrityError`就会通过模型的`save()` 函数抛出来。

除了`ManyToManyField`、`OneToOneField`和`FileField` 以外的其他字段类型都可以使用这个设置。

注意当设置`unique` 为`True` 时，你不需要再指定 `db_index`，因为`unique` 本身就意味着一个索引的创建。

## unique_for_date

`Field.unique_for_date`

当设置它为`DateField` 和`DateTimeField` 字段的名称时，表示要求该字段对于相应的日期字段值是唯一的。

例如，你有一个title 字段设置`unique_for_date="pub_date"`，那么Django 将不允许两个记录具有相同的`title` 和`pub_date`。

注意，如果你将它设置为`DateTimeField`，只会考虑其日期部分。此外，如果`USE_TZ` 为`True`，检查将以对象保存时的当前的时区 进行。

这是在模型验证期间通过`Model.validate_unique()` 强制执行的，而不是在数据库层级进行验证。如果`unique_for_date` 约束涉及的字段不是`ModelForm`（例如，exclude中列出的字段或者设置了`editable=False`），`Model.validate_unique()` 将忽略该特殊的约束。

## unique_for_month

`Field.unique_for_month`

类似`unique_for_date`，只是要求字段对于月份是唯一的。

## unique_for_year

`Field.unique_for_year`

类似`unique_for_date` 和 `unique_for_month`。

## verbose_name

`Field.verbose_name`

一个字段的可读性更高的名称。如果用户没有设定冗余名称字段，Django会自动将该字段属性名中的下划线转换为空格，并用它来创建冗余名称。可以参照 [Verbose field names](http://python.usyiyi.cn/django_182/topics/db/models.html#verbose-field-names).

## validators

`Field.validators`

该字段将要运行的一个`Validator` 的列表。更多信息参见`Validators` 的文档。

## 注册和获取查询

`Field` 实现了查询注册API。该API 可以用于自定义一个字段类型的可用的查询，以及如何从一个字段获取查询。

# 字段类型（Field Type）

## 自增字段

`class AutoField(**options)`

一个`IntegerField` 根据实际ID自动增长. 你通常不需要直接使用;如果不指定,一个主键字段将自动添加到你创建的模型中.详细查看[ 主键字段](http://python.usyiyi.cn/django_182/topics/db/models.html#automatic-primary-key-fields).

## BigIntegerField

`class BigIntegerField([**options])`

一个64位整数, 类似于一个 `IntegerField` ,它的值的范围是 -9223372036854775808 到9223372036854775807之间. 这个字段默认的表单组件是一个`TextInput`.

## BinaryField

`class BinaryField([**options])`

这是一个用来存储原始二进制码的`Field`. 只支持`bytes` 声明，注意这个Field只有很**有限**的功能。例如，不大可能在一个`BinaryField` 值的数据上进行查询

滥用 `BinaryField`

尽管你可能想使用数据库来存储你的文件，但是99%的情况下这都是不好的设计。这个字段不是合理操作静态文件的替代（XAE上可以使用storage替代）.

## CharField

`class CharField(max_length=None[, **options])`

一个用来存储从小到很大各种长度的字符串的地方

如果是巨大的文本类型, 可以用 `TextField`.

这个字段默认的表单样式是 `TextInput`.

`CharField`接收一个额外的必须参数。

`CharField.max_length`

字段的最大字符长度.max_length将在数据库层和Django表单验证中起作用, 用来限定字段的长度. 

需要注意的是：

如果你在写一个需要导出到多个不同数据库后端的应用，你需要注意某些后端对`max_length`有一些限制，[查看数据库后端](http://python.usyiyi.cn/django_182/ref/databases.html)注意事项来获取更多的细节

如果你是用了MySQLdb 1.2.2并且采用utf8_bin核对（并不是默认选项），这里就需要注意了，在[MySQL database notes](http://python.usyiyi.cn/django_182/ref/databases.html#mysql-collation)中有说明。

## CommaSeparatedIntegerField

`class CommaSeparatedIntegerField(max_length=None[, **options])`

一个逗号分隔的整数字段。像 `CharField`一样， 需要一个`max_length` 参数， 同时数据库移植时也需要注意。

## DateField

`class DateField([auto_now=False, auto_now_add=False, **options])`

这是一个使用Python的`datetime.date`实例表示的日期. 有几个额外的设置参数:

### DateField.auto_now

每次保存对象时，自动设置该字段为当前时间。用于"最后一次修改"的时间戳. 注意,它总是always使用当前日期; 它不仅是一个默认值，您可以重写。

### DateField.auto_now_add

当对象第一次被创建时自动设置当前时间。用于创建时间的时间戳. 它总是使用当前日期（第一次被创建时的时间？）; 它不仅是一个默认值，您可以重写。

该字段默认对应的表单控件是一个`TextInput`. 在管理员站点添加了一个JavaScript写的日历控件，和一个“Today"的快捷按钮.包含了一个额外的`invalid_date`错误消息键.

`auto_now_add`, `auto_now`, 和 `default` 这些设置是相互排斥的. 他们之间的任何组合将会发生错误的结果.

需要注意的是：

在目前的实现中，设置`auto_now`或者`auto_now_add`为`True`将为让这个字段同时得到`editable=False`和`blank=True`这两个设置.

注意：

`auto_now`和`auto_now_add`这两个设置会在对象创建或更新的时刻,总是使用`default timezone`(默认时区)的日期. 如果你不想这样，你可以考虑一下简单地使用你自己的默认调用或者重写`save()`(在`save()`函数里自己添加保存时间的机制.译者注)而不是使用`auto_now` 或者 `auto_now_add`; 或者使用`DateTimeField`字段类来替换`DateField` 并且在给用户呈现时间的时候,决定如何处理从`datetime`到`date`的转换.

## DateTimeField

`class DateTimeField([auto_now=False, auto_now_add=False, **options])`

它是通过Pythondatetime.datetime实例表示的日期和时间. 携带了跟DateField一样的额外参数.

该字段默认对应的表单控件是一个单个的`TextInput`(单文本输入框). 管理员系统使用两个单独Javascript的`TextInput`控件来完成输入。

## DecimalField

`class DecimalField(max_digits=None, decimal_places=None[, **options])`

十进制浮点数,表示python中 `Decimal` 的一个实例. 有两个 必须的参数:

### DecimalField.max_digits

位数总数，包括小数点后的位数。该值必须大于等于`decimal_places`.

### DecimalField.decimal_places

小数点后的数字数量。

举个例子，为了存储一个最大到999且含有两位数字的数字，你可以这样使用：
```python
models.DecimalField(..., max_digits=5, decimal_places=2)
```


 你要是想存储一个十亿的具有10位小数的数字，你可以使用这个：
```python
models.DecimalField(..., max_digits=19, decimal_places=10)
```


这个字段默认表单中的控件是`TextInput`。

注意的是：

关于`FloatField`和`DecimalField`的区别，你可以点击[这里](http://python.usyiyi.cn/django_182/ref/models/fields.html#floatfield-vs-decimalfield)。

## DurationField

**New in Django 1.8.**

`class DurationField([**options])`

用作存储一段时间的字段类型 - 类似Python中的`timedelta`. 当使用PostgreSQL的时候，使用的数据类型是`interval`，而在Oracle里就是 `INTERVAL DAY(9) TO SECOND(6)`.其他的就是一个微秒的`bigint`

**需要注意的是：**

在大多数情况下，`DurationField`能够正常工作。然而除了PostgreSQL以外，在DateTimeField计算`DurationField`的值的时候将有可能不如预期的工作。

## EmailField

`class EmailField([max_length=254, **options])`

是一个会检查有效的邮件地址的`CharField`，其会使用`EmailValidator`来[验证](http://python.usyiyi.cn/django_182/ref/validators.html#django.core.validators.EmailValidator)这个输入。

**Changed in Django 1.8:**

max_length的默认值为了与`RFC3696/5321`所兼容，会从75到254的长度间所兼容。

## FileField

`class FileField([upload_to=None, max_length=100, **options])`

一个上传文件的字段。

注意

如果使用`primary_key` 和`unique`参数会生成 `TypeError`错误

有两个可选参数：

`FileField.upload_to`

Changed in Django 1.7:

在旧版本Django中，`upload_to` 属性是必须要有的;

将会添加一个本地文件系统路径到 `MEDIA_ROOT` 设置中，来明确 url 属性的值。

这个路径可能会包含一个 `strftime()` 格式串,并且会在文件上传时被替换为 实际的`date/time`作为文件路径 (这样上传的文件就不会塞满你指定的文件夹了).

这也可以是一个可调用对象，如函数。可以调用它来获取上传路径，包括文件名。它必须接受两个参数，并且返回一个Unix-style的路径(带有/)给存储系统。这被传递的两个参数为:
<table style="width: 805px; box-sizing: border-box; height: 220px;" border="0" width="439" cellspacing="0" cellpadding="0"><colgroup> <col style="mso-width-source: userset; mso-width-alt: 4096; width: 96pt; box-sizing: border-box;" width="128" /> <col style="mso-width-source: userset; mso-width-alt: 9952; width: 233pt; box-sizing: border-box;" width="311" /> </colgroup><tbody><tr style="height: 15.0pt; box-sizing: border-box;"><td class="xl63" style="height: 15.0pt; width: 96pt;" width="128" height="20">Argument</td><td class="xl63" style="width: 233pt;" width="311">Description</td></tr><tr style="height: 85.5pt; box-sizing: border-box;"><td class="xl67" style="height: 85.5pt; border-top: none; width: 96pt; box-sizing: border-box;" width="128" height="114">instance</td><td class="xl64" style="width: 233pt; box-sizing: border-box;" width="311">FileField 被定义时的一个实例. 更准确地说，这是一个包含当前文件的特殊实例。在大多数情况下, this object will not have been saved to the database yet, so if it uses the default AutoField, it might not yet have a value for its primary key field.</td></tr><tr style="height: 43.5pt; box-sizing: border-box;"><td class="xl66" style="height: 43.5pt; width: 96pt; box-sizing: border-box;" width="128" height="58">filename</td><td class="xl65" style="width: 233pt; box-sizing: border-box;" width="311">The filename that was originally given to the file. This may or may not be taken into account when determining the final destination path.</td></tr></tbody></table>

## FileField.storage

一个storage对象，用于你的文件的存取。参见[Managing files](http://python.usyiyi.cn/django_182/topics/files.html)获取这个对象的细节。

这个字段在表格里的默认组件是 `ClearableFileInput`.

在模型中使用`FileField`或者`ImageField`需要进行以下几步：

1.  在你的设置文件之中，你需要作为定义`MEDIA_ROOT`作为完整地址为Django上传的地址（举个例子，为了高性能，这些文件最好不要存储于数据库之中）
2.  向模型中添加`FileField`或者`ImageField`，你就可以定义`upload_to`来指定`MEDIA_ROOT`下的子文件作为上传的文档
3.  所有存储到数据库中的文件都将以相对路径的形式存储到数据库之中，你可以使用Django提供的简便的url属性来指明其地址。举个例子，如果你的`ImageField`被`mug_shot`所捕获了，你就能在模板中使用`{{ object.mug_shot.url }}`来取得到图像的绝对路径。

例如，如果你的 `MEDIA_ROOT`设定为 '`/home/media`'，并且 upload_to设定为 'photos/%Y/%m/%d'。 `upload_to`的'`%Y/%m/%d`'被`strftime()`所格式化；'%Y' is the four-digit year, '%m' is the two-digit month and '%d' is the two-digit day. If you upload a file on Jan. 15, 2007, it will be saved in the directory `/home/media/photos/2007/01/15`.

如果你想获得上传文件的存盘文件名，或者是文件大小，你可以分别使用 `name` 和 `size`属性； for more information on the available attributes and methods, see the [File](http://python.usyiyi.cn/django_182/ref/files/file.html#django.core.files.File) class reference and the [Managing files](http://python.usyiyi.cn/django_182/topics/files.html) topic guide.

Note

保存的文件作为模型存储在数据库中的一部分，所以在磁盘上使用的实际的文件名在模型保存完毕之前是不可靠的。

上传的文件对应的URL可以通过使用 url 属性获得. 在内部，它会调用  Storage 类下的`url()`方法.

值得注意的是，无论你在任何时候处理上传文件的需求，你都应该密切关注你的文件将被上传到哪里，上传的文件类型，以避免安全漏洞。认证所有上传文件 以确保那些上传的文件是你所认为的文件。例如，如果你盲目的允许其他人在无需认证的情况下上传文件至你的web服务器的root目录中，那么别人可以上传一个CGI或者PHP脚本然后通过访问一个你网站的URL来执行这个脚本。所以，不要允许这个发生。

甚至是上传HTML文件也值得注意，它可以通过浏览器（虽然不是服务器）执行，也可以引发相当于是XSS或者CSRF攻击的安全威胁。

`FileField` 实例将会在你的数据库中创建一个默认最大长度为100字符的`varchar` 列。就像其他的`fields`一样, 你可以用 `max_length` 参数改变最大长度的值。

### FileField和FieldFile

`class FieldFile[source]`

当你在模型之中访问`FileField`，你就能够使用使用代理模型来访问潜在的文件。这样也能从`django.core.files.File`中继承类，这个类也有几个函数能够和文件数据进行交互：

### FieldFile.url

一个通过`url()`方式只读文件`Storage`类的相对路径的属性。

### FieldFile.open(mode='rb')

能像标准Python函数的`open()`那样打开在这个模式下在指定模型实例所关联的文件。

### FieldFile.close()

能像标准Python函数的close()那样打开在这个模式下在指定模型实例所关联的文件。

### FieldFile.save(name, content, save=True)

这个方式会获取文件名以及文件内容并且把他传递到字段的存储类之中，然后模型字段会和储存文件关联。如果你想手动在模型实例使用`FileField`关联文件的话，`save()`这个函数就能够保存文件数据。

其会使用两个必选参数：文件名称和一个包含文件内容的对象。可选参数就是一个控制在关联字段的文件发生变更的时候模型实例是否会被保存。默认是`True`。

需要注意的是，内容参数应该是`django.core.files.File`的一个实例而不是Python的内建对象，你能够这样从一个现有的Python文件对象之中构建这个文件：
```python
from django.core.files import File
# Open an existing file using Python's built-in open()
f = open('/tmp/hello.world')
myfile = File(f)
```


或者你可以这样构造Python的字符串：
```python
from django.core.files.base import ContentFile
myfile = ContentFile("hello world")
```


更多的信息，你可以查看[Managing files](http://python.usyiyi.cn/django_182/topics/files.html).

### FieldFile.delete(save=True)

删除与实例相关的文件并且关闭字段中所有的属性。需要注意的是，这个方式当`delete()`被调用的时候会关闭文件。

可选`save`项会控制在关联字段的文件发生删除的时候模型实例是否会被保存。默认是`True`。

注意，model删除的时候，与之关联的文件并不会被删除。如果你要把文件也清理掉，你需要自己处理。

## FilePathField

`class FilePathField(path=None[, match=None, recursive=False, max_length=100, **options])`

一个 `CharField` ，内容只限于文件系统内特定目录下的文件名。有三个参数, 其中第一个是 必需的:

### FilePathField.path

必选项。文件系统`FilePathField`需要获得的选项的绝对路径。

举个例子： "`/home/images`".

### FilePathField.match

可选项。`FilePathField`用于过滤文件名的一个正则表达式。需要注意的是，正则表达式会被应用于基本文件夹而不是绝对路径。

举个例子：`foo.*.txt$`"会匹配名为foo23.txt而不会匹配`bar.txt`或者`foo23.png`。

### FilePathField.recursive

可选项。布尔值，默认值为False。指定所有子文件夹的是否应该被包括。

### FilePathField.allow_files

可选项。布尔值，默认为True。在指定位置下的文件是否应该被包括。这个或者`allow_folders`有一个必须为True。

### FilePathField.allow_folders

可选项，布尔值，默认为False。在指定位置下的文件夹是否应该被包括。这个或者`allow_files`有一个必须为True。

当然，这些参数能够一起使用

有一点需要提醒的是 match只匹配基本文件名（base filename）, 而不是整个文件路径（full path）. So, this example:
```python
FilePathField(path="/home/images", match="foo.*", recursive=True)
```


 会匹配`/home/images/foo.png`但是并不会匹配`/home/images/bar.png`，因为这个前者的匹配会应用于`foo.png`和`bar.png`。

`FilePathField`实例会以最大长度为100个字符的`varchar`的行在数据库中储存。和别的字段一样，你也能通过使用max_length的参数来改变最大长度。

## FloatField

`class FloatField([**options])`

一个浮点数会由Python的一个浮点数实例所代表。

默认表格的控件是`TextInput`。

`FloatField` vs. `DecimalField`

`FloatField`会和`DecimalField`类会混淆。尽管他们都能表示实数，但是他们表示的方式却很不相同。`FloatField`会使用Python的内建的浮点类型而`DecimalField`会使用Python的小数类型。在[这里](https://docs.python.org/3/library/decimal.html#module-decimal)有关于`decimal`模组的更多信息。

## ImageField

`class ImageField([upload_to=None, height_field=None, width_field=None, max_length=100, **options])`

继承了 `FileField`的所有属性和方法, 但还对上传的对象进行校验，确保它是个有效的image.

除了从`FileField`继承来的属性外，ImageField 还有宽和 高属性。

为了辅助查询这些属性，`ImageField`有两个额外的参数：

### ImageField.height_field

每当模组实例保存的时候，会被自动存储的图片高度的模型字段的名称。

### ImageField.width_field

每当模组实例保存的时候，会被自动存储的图片宽度的模型字段的名称。

ImageField字段需要调用[Pillow](http://pillow.readthedocs.org/en/latest/) 库.

`ImageField` 实例将会在你的数据库中创建一个默认最大长度为100字符的`varchar` 列。就像其他的fields一样, 你可以用 `max_length` 参数改变最大长度的值。

这个字段的默认的表单控件是`ClearableFileInput`。

## IntegerField

`class IntegerField([**options])`

一个整数。在Django所支持的所有数据库中，从 -2147483648 到 2147483647 范围内的值是合法的。默认的表单输入工具是`TextInput`.

## GenericIPAddressField

`class GenericIPAddressField([protocol=both, unpack_ipv4=False, **options])`

一个IPv4或者一个IPv6的地址（比如`192.0.2.30`或者`2a02:42fe::4`），默认的表单控件式`TextInput`。

IPv6的地址格式化会遵循`RFC 4291`的标准，包含IPv4推荐的格式，例如`::ffff:192.0.2.0`。举个例子，`2001:0::0:01`会被格式化为`2001::1`，`::ffff:0a0a:0a0a`会被转换成`::ffff:10.10.10.10`，所有的字符都会转换成小写。

### GenericIPAddressField.protocol

可以限制指定的套接字，IPv4或者IPv6都是可以的，这里大小写敏感。

### GenericIPAddressField.unpack_ipv4

把IPv4展开成类似于`::ffff:192.0.2.1`的地址，当这个选项可用的时候，地址就会被转换成`192.0.2.1`.默认是禁用的，当套接字被设置为`both`的时候才能被使用。

如果你允许空值，因为空值会以`null`来存储，你必须允许空值的通行。

## NullBooleanField

`class NullBooleanField([**options])`

和`BooleanField`一样，但是能够允许`NULL`作为其中的一个选项。需要使用这个而不是一个`null=True`的`BooleanField`。默认的表单控件是`NullBooleanSelect`。

## PositiveIntegerField

`class PositiveIntegerField([**options])`

从0-2147483647的值在Django所支持的数据库中都支持，0的支持与否是根据后台兼容所决定的。

## PositiveSmallIntegerField

`class PositiveSmallIntegerField([**options])`

该模型字段类似 `PositiveIntegerField`, 但是只允许小于某一特定值（依据数据库类型而定）。从0 到 32767 这个区间，对于Django所支持的所有数据库而言都是安全的。

## SlugField

`class SlugField([max_length=50, **options])`

Slug 是一个新闻术语（通常叫做短标题）。一个slug只能包含字母、数字、下划线或者是连字符，通常用来作为短标签。通常它们是用来放在URL里的。

和`CharField`一样，你能够指定最大长度，如果并没有指定，Django会使用50作为其的值。

指定`setting Field.db_index`为`True`。

自动创建`SlugField`会基于其他值。你能够在管理员网页中使用`prepopulated_fields`所自动使用它。

## SmallIntegerField

`class SmallIntegerField([**options])`

和`IntegerField`一样，但是只会允许基于数据库的值，从-32768到32767在所有Django能够支持的数据库之中的数据都是安全的。

## TextField

`class TextField([**options])`

长文本的字段，默认表单控件是`Textarea`。

**Changed in Django 1.7:**

如果你指定了`max_length`的属性，其会在自动生成的表单字段中的控件所响应，然而在模型和数据库的层面上并不会强制要求这个属性。你可以使用`CharField`来解决这个问题。

MySQL users

如果你正在使用`MySQLdb 1.2.1p2`并且`utf8_bin`的核对方法的话这里就需要注意一些问题了，在[MySQL database notes](http://python.usyiyi.cn/django_182/ref/databases.html#mysql-collation)中就可以获得详情。

## TimeField

`class TimeField([auto_now=False, auto_now_add=False, **options])`

这个字段会被Python中的`datetime.time`实例所代表，其也接受一个同样自动创建的和`DateField`一样的选项。

默认的表单控件是`TextInput`，管理员站点会使用JavaScript的一个快捷方式。

## URLField

`class URLField([max_length=200, **options])`

一个为URL所涉及的`CharField`。

默认的表单控件是`TextInput`。

和所有的`CharField`的子类一样，`URLField`会使用`max_length`参数作为可选项。如果你并没有指定`max_length`的值，默认会使用200作为其值。

## UUIDField

**New in Django 1.8.**

`class UUIDField([**options])`

一个为了存储[通用唯一识别码](http://baike.baidu.com/link?url=hwOmlIib6lr_lkrd-Ea3-DW8NaJtN7aV6ZQ_aUTesW_nLcbtAaV49zx7ByqY52NDF4sWvLC6a7QV-6ARGI0vKa "UUID")的字段，使用Python的`UUID`这个类，当使用PostgreSQL的时候，其会以`uuid`的数据类型储存而不是`char(32)`的格式。

[通用唯一识别码](http://baike.baidu.com/link?url=hwOmlIib6lr_lkrd-Ea3-DW8NaJtN7aV6ZQ_aUTesW_nLcbtAaV49zx7ByqY52NDF4sWvLC6a7QV-6ARGI0vKa "UUID")是一个能够替代`primary_key`的一个`AutoField`，数据库并不会自动生成`UUID`，所以使用默认类型还是比较好的。
```python
import uuid
from django.db import models

class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # other fields
```


 需要注意的是一个`callable`会被传递给`default`，而不是[UUID](http://baike.baidu.com/link?url=hwOmlIib6lr_lkrd-Ea3-DW8NaJtN7aV6ZQ_aUTesW_nLcbtAaV49zx7ByqY52NDF4sWvLC6a7QV-6ARGI0vKa)的实例。

# 关系字段

Django 同样定义了一系列的字段来描述数据库之间的关联。

## ForeignKey

`class ForeignKey(othermodel[, **options])`

多对一关系。需要一个位置参数：与该模型关联的类。

若要创建一个递归的关联 —— 对象与自己具有多对一的关系 —— 请使用`models.ForeignKey('self')`。

如果你需要关联到一个还没有定义的模型，你可以使用模型的名字而不用模型对象本身：
```python
from django.db import models

class Car(models.Model):
    manufacturer = models.ForeignKey('Manufacturer')
    # ...

class Manufacturer(models.Model):
    # ...
    pass
```


 若要引用在其它应用中定义的模型，你可以用带有完整标签名的模型来显式指定。例如，如果上面提到的Manufacturer 模型是在一个名为production 的应用中定义的，你应该这样使用它：
```python
class Car(models.Model):
    manufacturer = models.ForeignKey('production.Manufacturer')
```


 在解析两个应用之间具有相互依赖的导入时，这种引用将会很有帮助。

`ForeignKey` 会自动创建数据库索引。你可以通过设置`db_index` 为`False` 来取消。如果你创建外键是为了一致性而不是用来Join，或者如果你将创建其它索引例如部分或多列索引，你也许想要避免索引的开销。

警告

不建议从一个没有迁移的应用中创建一个`ForeignKey` 到一个具有迁移的应用。更多细节参见[依赖性文档](http://python.usyiyi.cn/django_182/topics/migrations.html#unmigrated-dependencies)。

### 数据库中的表示

在幕后，Django 会在字段名上添加"`_id`" 来创建数据库中的列名。在上面的例子中，Car 模型的数据库表将会拥有一个manufacturer_id 列。（你可以通过显式指定`db_column` 改变它）。但是，你的代码永远不应该处理数据库中的列名称，除非你需要编写自定义的SQL。你应该永远只处理你的模型对象中的字段名称。

### 参数

`ForeignKey` 接受额外的参数集 —— 全都是可选的 —— 它们定义关联关系如何工作的细节。

#### ForeignKey.limit_choices_to

当这个字段使用模型表单或者`Admin` 渲染时（默认情况下，查询集中的所有对象都可以使用），为这个字段设置一个可用的选项。它可以是一个字典、一个Q 对象或者一个返回字典或Q对象的可调用对象。

例如：
```python
staff_member = models.ForeignKey(User, limit_choices_to={'is_staff': True})
```


 将使得模型表单 中对应的字段只列出`is_staff=True` 的`Users`。 这在Django 的`Admin` 中也可能有用处。

可调用对象的形式同样非常有用，比如与Python 的`datetime`模块一起使用来限制选择的时间范围。例如：
```python
def limit_pub_date_choices():
    return {'pub_date__lte': datetime.date.utcnow()}

limit_choices_to = limit_pub_date_choices
```


 如果`limit_choices_to` 自己本身是或者返回一个用于复杂查询的Q 对象，当字段没有在模型的`ModelAdmin`中的`raw_id_fields` 列出时，它将只会影响`Admin`中的可用的选项。

**Changed in Django 1.7:**

以前的Django 版本不允许传递一个可调用的对象给`limit_choices_to`。

_注_

如果`limit_choices_to` 使用可调用对象，这个可调用对象将在每次创建一个新表单的时候都调用。它还可能在一个模型校验的时候调用，例如被管理命令或者`Admin`。`Admin` 多次构造查询集来验证表单在各种边缘情况下的输入，所以你的可调用对象可能调用多次。

#### ForeignKey.related_name

这个名称用于让关联的对象反查到源对象。它还是`related_query_name` 的默认值（关联的模型进行反向过滤时使用的名称）。完整的解释和示例参见关联对象的文档。注意，当你为抽象模型定义关联关系的时，必须设置这个参数的值；而且当你这么做的时候需要用到一些特殊语法。

如果你不想让Django 创建一个反向关联，请设置`related_name` 为 '+' 或者以'+' 结尾。 例如，下面这行将确定User 模型将不会有到这个模型的返回关联：
```python
user = models.ForeignKey(User, related_name='+')
```


#### ForeignKey.related_query_name

这个名称用于目标模型的反向过滤。如果设置了`related_name`，则默认为它的值，否则默认值为模型的名称：
```python
# Declare the ForeignKey with related_query_name
class Tag(models.Model):
    article = models.ForeignKey(Article, related_name="tags", related_query_name="tag")
    name = models.CharField(max_length=255)

# That's now the name of the reverse filter
Article.objects.filter(tag__name="important")
```


#### ForeignKey.to_field

关联到的关联对象的字段名称。默认地，Django 使用关联对象的主键。

#### ForeignKey.db_constraint

控制是否在数据库中为这个外键创建约束。默认值为`True`，而且这几乎一定是你想要的效果；设置成`False` 对数据的完整性来说是很糟糕的。即便如此，有一些场景你也许想要这么设置：

*   你有遗留的无效数据。
*   你正在对数据库缩容。

如果被设置成`False`，访问一个不存在的关联对象将抛出 `DoesNotExist` 异常。

#### ForeignKey.on_delete

当一个`ForeignKey` 引用的对象被删除时，Django 默认模拟`SQL` 的`ON DELETE CASCADE` 的约束行为，并且删除包含该`ForeignKey`的对象。这种行为可以通过设置`on_delete` 参数来改变。例如，如果你有一个可以为空的`ForeignKey`，在其引用的对象被删除的时你想把这个`ForeignKey` 设置为空：
```python
user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
```


 `on_delete` 在`django.db.models`中可以找到的值有：

#### CASCADE

级联删除；默认值。

#### PROTECT

抛出`ProtectedError` 以阻止被引用对象的删除，它是`django.db.IntegrityError` 的一个子类。

#### SET_NULL

把`ForeignKey` 设置为`null`； `null` 参数为`True` 时才可以这样做。

#### SET_DEFAULT

`ForeignKey` 值设置成它的默认值；此时必须设置`ForeignKey` 的default 参数。

#### SET()

设置`ForeignKey` 为传递给`SET()` 的值，如果传递的是一个可调用对象，则为调用后的结果。在大部分情形下，传递一个可调用对象用于避免`models.py` 在导入时执行查询：
```python
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class MyModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET(get_sentinel_user))
```


#### DO_NOTHING

不采取任何动作。如果你的数据库后端强制引用完整性，它将引发一个`IntegrityError` ，除非你手动添加一个`ON DELETE` 约束给数据库自动（可能要用到初始化的SQL）。

### ForeignKey.swappable

**New in Django 1.7.**

控制迁移框架的的重复行为如果该`ForeignKey` 指向一个可切换的模型。如果它是默认值True，那么如果ForeignKey 指向的模型与`settings.AUTH_USER_MODEL` 匹配（或其它可切换的模型），则保存在迁移中的关联关系将使用对setting 中引用而不是直接对模型的引用。

只有当你确定你的模型将永远指向切换后的模型 —— 例如如果它是专门为你的自定义用户模型设计的模型时，你才会想将它设置成`False`。

设置为`False` 并不表示你可以引用可切换的模型即使在它被切换出去之后 —— `False` 只是表示生成的迁移中`ForeignKey` 将始终引用你指定的准确模型（所以，如果用户试图允许一个你不支持的User 模型时将会失败）。

如果有疑问，请保留它的默认值`True`。

### ForeignKey.allow_unsaved_instance_assignment

**New in Django 1.8:**

添加这个标志是为了向后兼容，因为老版本的Django 始终允许赋值未保存的模型实例。

Django 阻止未保存的模型实例被分配给一个`ForeignKey` 字段以防止意味的数据丢失（当保存一个模型实例时，未保存的外键将默默忽略）。

如果你需要允许赋值未保存的实例且不关心数据的丢失（例如你不会保存对象到数据库），你可以通过创建这个字段的子类并设置其`allow_unsaved_instance_assignment` 属性为`True` 来关闭这个检查。例如：
```python
class UnsavedForeignKey(models.ForeignKey):
    # A ForeignKey which can point to an unsaved object
    allow_unsaved_instance_assignment = True

class Book(models.Model):
    author = UnsavedForeignKey(Author)
```


## ManyToManyField

`class ManyToManyField(othermodel[, **options])`

一个多对多关联。要求一个关键字参数：与该模型关联的类，与ForeignKey 的工作方式完全一样，包括[递归关系](http://python.usyiyi.cn/django_182/ref/models/fields.html#recursive-relationships) 和[惰性关系](http://python.usyiyi.cn/django_182/ref/models/fields.html#lazy-relationships)。

关联的对象可以通过字段的`RelatedManager `添加、删除和创建。

警告

不建议从一个没有迁移的应用中创建一个ForeignKey 到一个具有迁移的应用。 更多细节参见依赖性文档。

### 数据库中的表示

在幕后，Django 创建一个中间表来表示多对多关系。默认情况下，这张中间表的名称使用多对多字段的名称和包含这张表的模型的名称生成。因为某些数据库支持的表的名字的长度有限制，这些标的名称将自动截短到64 个字符并加上一个唯一性的哈希值。这意味着，你看的表的名称可能类似 `author_books_9cdf4`；这再正常不过了。你可以使用`db_table` 选项手工提供中间表的名称。

### 参数

`ManyToManyField` 接收一个参数集来控制关联关系的功能 —— 它们都是可选的。

#### ManyToManyField.related_name

与`ForeignKey.related_name` 相同。

#### ManyToManyField.related_query_name

与`ForeignKey.related_query_name` 相同。

#### ManyToManyField.limit_choices_to

与`ForeignKey.limit_choices_to` 相同。

`limit_choices_to` 对于使用`through` 参数自定义中间表的`ManyToManyField` 不生效。

#### ManyToManyField.symmetrical

只用于与自身进行关联的`ManyToManyField`。例如下面的模型：
```python
from django.db import models

class Person(models.Model):
    friends = models.ManyToManyField("self")
```


 当Django 处理这个模型的时候，它定义该模型具有一个与自身具有多对多关联的`ManyToManyField`，因此它不会向Person 类添加`person_set` 属性。Django 将假定这个`ManyToManyField` 字段是对称的 —— 如果我是你的朋友，那么你也是我的朋友。

如果你希望与self 进行多对多关联的关系不具有对称性，可以设置`symmetrical` 为`False`。这会强制让Django 添加一个描述器给反向的关联关系，以使得`ManyToManyField` 的关联关系不是对称的。

#### ManyToManyField.through

Django 会自动创建一个表来管理多对多关系。不过，如果你希望手动指定中介表，可以使用`through` 选项来指定Django 模型来表示你想要使用的中介表。

这个选项最常见的使用场景是当你想要关联额外的数据到多对多关联关系的时候。

如果你没有显式指定`through` 的模型，仍然会有一个隐式的`through` 模型类，你可以用它来直接访问对应的表示关联关系的数据库表。它由三个字段来链接模型。

如果源模型和目标不同，则生成以下字段：

*   `id`：关系的主键。
*   `<containing_model>_id`：声明`ManyToManyField` 字段的模型的`id`。
*   `<other_model>_id`：`ManyToManyField` 字段指向的模型的`id`。

如果ManyToManyField 的源模型和目标模型相同，则生成以下字段：

*   id：关系的主键。
*   `from_<model>_id`：源模型实例的`id`<!--more--><!--more-->。
*   `to_<model>_id`：目标模型实例的`id`。

这个类可以让一个给定的模型像普通的模型那样查询与之相关联的记录。

#### ManyToManyField.through_fields

**New in Django 1.7.**

只能在指定了自定义中间模型的时候使用。 Django 一般情况会自动决定使用中间模型的哪些字段来建立多对多关联。但是，考虑如下模型：
```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership', through_fields=('group', 'person'))

class Membership(models.Model):
    group = models.ForeignKey(Group)
    person = models.ForeignKey(Person)
    inviter = models.ForeignKey(Person, related_name="membership_invites")
    invite_reason = models.CharField(max_length=64)
```


 Membership 有两个 外键指向Person （person 和inviter），这使得关联关系含混不清并让Django 不知道使用哪一个。在这种情况下，你必须使用`through_fields` 明确指定Django 应该使用哪些外键，就像上面例子一样。

`through_fields` 接收一个二元组('field1', 'field2')，其中field1 为指向定义`ManyToManyField` 字段的模型的外键名称（本例中为group），field2 为指向目标模型的外键的名称（本例中为person）。

当中间模型具有多个外键指向多对多关联关系模型中的任何一个（或两个），你必须 指定`through_fields`。这通用适用于递归的关联关系，当用到中间模型而有多个外键指向该模型时，或当你想显式指定Django 应该用到的两个字段时。

递归的关联关系使用的中间模型始终定义为非对称的，也就是`symmetrical=False` —— 所以具有源和目标的概念。这种情况下，'field1' 将作为管理关系的源，而'field2' 作为目标。

#### ManyToManyField.db_table

为存储多对多数据而创建的表的名称。如果没有提供，Django 将基于定义关联关系的模型和字段假设一个默认的名称。

#### ManyToManyField.db_constraint

控制中间表中的外键是否创建约束。默认为`True`，而且这是几乎就是你想要的；设置为`False` 对数据完整性将非常糟糕。下面是你可能需要这样设置的一些场景：

你具有不合法的遗留数据。

*   你正在对数据库缩容。
*   不可以同时传递`db_constraint` 和 `through`。

#### ManyToManyField.swappable

**New in Django 1.7.**

控制`ManyToManyField` 指向一个可切换的模型时迁移框架的行为。如果它是默认值True，那么如果`ManyToManyField` 指向的模型与`settings.AUTH_USER_MODEL` 匹配（或其它可切换的模型），则保存在迁移中的关联关系将使用对`setting` 中引用而不是直接对模型的引用。

只有当你确定你的模型将永远指向切换后的模型 —— 例如如果它是专门为你的自定义用户模型设计的模型时，你才会想将它设置成`False`。

如果不确定，请将它保留为`True`。

#### ManyToManyField.allow_unsaved_instance_assignment

New in Django 1.8.

与`ForeignKey.allow_unsaved_instance_assignment` 的工作方式类似。

`ManyToManyField` 不支持`validators`。

`null` 不生效，因为无法在数据库层次要求关联关系。

## OneToOneField

`class OneToOneField(othermodel[, parent_link=False, **options])`

一对一关联关系。概念上将，这个字段很像是`ForeignKey` 设置了`unique=True`，不同的是它会直接返回关系另一边的单个对象。

它最主要的用途是作为扩展自另外一个模型的主键；例如，多表继承就是通过对子模型添加一个隐式的一对一关联关系到父模型实现的。

需要一个位置参数：与该模型关联的类。 它的工作方式与`ForeignKey` 完全一致，包括所有与递归关系和惰性关系相关的选项。

如果你没有指定`OneToOneField` 的`related_name` 参数，Django 将使用当前模型的小写的名称作为默认值。

例如下面的例子：
```python
from django.conf import settings
from django.db import models

class MySpecialUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    supervisor = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='supervisor_of')
```


 你将使得User 模型具有以下属性：
```default
>>> user = User.objects.get(pk=1)
>>> hasattr(user, 'myspecialuser')
True
>>> hasattr(user, 'supervisor_of')
True
```


 当反向访问关联关系时，如果关联的对象不存在对应的实例，则抛出`DoesNotExist` 异常。例如，如果一个User 没有`MySpecialUser` 指定的`supervisor`：
```default
>>> user.supervisor_of
Traceback (most recent call last):
    ...
DoesNotExist: User matching query does not exist.
```


 另外，`OneToOneField` 除了接收`ForeignKey` 接收的所有额外的参数之外，还有另外一个参数：

### OneToOneField.parent_link

当它为True 并在继承自另一个具体模型 的模型中使用时，表示该字段应该用于反查的父类的链接，而不是在子类化时隐式创建的`OneToOneField`。

`OneToOneField` 的使用示例参见`One-to-one` [关联关系](http://python.usyiyi.cn/django_182/topics/db/examples/one_to_one.html)。

 