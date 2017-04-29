---
title: python ConfigParser – 配置文件解析
tags:
  - Python
id: 1352
categories:
  - Python
date: 2016-10-12 23:33:05
---

ConfigParser该模块定义了ConfigParser类，该类实现了基本的配置文件的解析，配置文件提供了类似与 WINDOWS下的INI文件结构。你可以使用该类编写最终用户很容易自定义的Python程序。

警告：该库不包括值类型前缀，该前缀应用与INI语法的扩展版本—Windows Registry中。

例如：

<pre class="lang:ini decode:true">[My Section] 
foodir: %(dir)s/whatever 
dir=frob</pre>

将会解析“`%(dir)s`”为“`dir`”的值（这里是“`frob`”）。该模块包含所以需要的扩展。

默认值可以通过他们作为字典传递给`ConfigParser`构造器来知道，另外还会默认传递给`get()`方法，它会覆盖其他所以方法。

Class RawConfigParser([defaults]) 

基本配置类，当传递defaults时，会初始化到内置字典中。该类不支持智能修复，2.3版本新特征。

Class ConfigParser([defaults])

继承之RawConfigParser类，实现了智能特性，为get(),items()方法添加了可选参数。Defaults中的值必须能填补“%()s”。注意__name__是内置的default；该值是section的名称，它会被defaults提供的任何值所覆盖。

所以的用于填补的option名称都会通过optionxform()方法传递，就像其他任何option名称一样。例如，使用optionxform()的默认实现（将option名称转化成小写），“foo %(bar)s”和“foo %(BAR)s”的值相等。

Class SafeConfigParser([defaults]) 

继承至ConfigParser，实现了更多智能特征，实现更有可预见性，新的应用更偏好这个版本，如果他们不需要对python老版本的兼容性，2.3版本。

Exception NoSectionError 

当没有发现给定section时抛出。

Exception DuplicateSectionError 

如果add_section()方法被调用时，提供的section参数的值已经存在时抛出。

Exception NoOptionError 

指定option不存在时抛出。

Exception InterpolationError 

执行字符串填补时抛出的异常的基类。

Exception InterpolationDepthError 

当填补字符串因为迭代次数超过了MAX_INTERPOLATION_DEPTH值时抛出的异常，InterpolationError的子类。

Exception InterpolationMissingOptionError 

当option引用的值不存在时抛出，该异常为InterpolationError的子类，2.3版本新加。

Exeption InterpolationSyntaxError 

当原文件格式没有遵守规定的语法时抛出的异常，继承至InterpolationError，2.3版本。

Exception MissingSectionHeaderError 

尝试解析没有section头的文件时抛出。

Exception ParsingError 

解析文件时发生错误。

MAX_INTERPOLATION_DEPTH 

get()方法当raw参数为false时，递归的对大深度。只适用与ConfigParser类。

RawConfigParser对象 

RawConfigParser实例的方法：

defaults() 

返回全部示例中所以defaults。

sections() 

返回有效的section列表，DEFAULT不包含在列表中。

add_section(section) 

为实例添加一个section，如果给定的section名已经存在，将抛出DuplicateSectionError异常。

has_section(section) 

判断给定的section名在配置文件中是否存在，DEFAULT section不包括。

options(section) 

返回给定的section下的所有可用option的列表。

has_option(section, option) 

如果section存在，并包含给定的option，返回true，放在返回false, 1.6版本新增。

read(filenames) 

尝试解析文件列表，如果解析成功返回文件列表。如果filenames是string或Unicode string，将会按单个文件来解析。如果在filenames中的文件不能打开，该文件将被忽略。这样设计的目的是，让你能指定本地有可能是配置文件的列表（例如，当前文件夹，用户的根目录，及一些全系统目录），所以在列表中存在的配置文件都会被读取。如果文件都不存在，那么ConfigParser实例会包含空数据集。一个需要从配置文件读取初始化数据的应用程序，应该使用readfp()方法来加载所需要的文件，之后可以使用read()方法来获取任何可能的文件：

<pre class="lang:python decode:true ">import ConfigParser, os

config = ConfigParser.ConfigParser() 
config.readfp(open('defaults.cfg')) 
config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')]) </pre>

&nbsp;

2.4版本之后，返回成功解析的文件列表。

readfp(fp[, filename]) 

从文件或fp（值使用该对象的readline()方法）中的似文件类读取并解析配置数据，如果filename被省略，fp有一个name属性，该属性用于获取filename；默认是“&lt;???&gt;”。

get(section, option) 

获取section下option的值。

getint(section, option) 

强制指定section下的option的值，作为Int类型返回的方便方法。

getfloat(section, option) 

强制section下的option值，作为float类型返回的方法方法。

getboolean(section, option) 

强制section下的option值，作为布尔类型返回的方法方法。注意可接受的option的true值有“1”，“yes”，“true”及“on”，可接受的false值有“0”，“no”，“false”，“off”。字符串值不检测大小写，其他值会抛出ValueError异常。

itmes(section) 

返回给定section下的所以option的（name, value）对列表。

set(section, option, value) 

如果给定的setion存在，为option设定给定的值；否则抛出NoSectionError异常。当可能使用RawConfigParser（或者ConfigParser的参数raw为true）来在内部存储非字符串值，所以功能（包括填补和输出到文件）只能使用字符串值来归档。1.6版本新增。

write(fileobject) 

将配置表示写入指定文件类，该表示以后可以通过调用read()来解析，1.6版本新增。

remove_option(section, option) 

从指定section中删除指定option，如果section不存在，抛出NoSectionError异常；如果option存在，则删除，并返回True；否则返回false。1.6版本新增。

remove_section(section) 

从配置文件中删除指定的section，如果section确实存在，返回true，否则返回false。

optionxform(option) 

将输入文件中，或客户端代码传递的option名转化成内部结构使用的形式。默认实现返回option的小写形式；子类可能重写该方法或客户端代码可能将该方法作为实例的属性，以此来影响它的行为。将此用于str()，例如，会使option名称大小写敏感。

ConfigParser对象 

ConfigParser类扩展了RawConfigParser的一些接口方法，添加了一些可选参数。

get(section, option [, raw[, vars]]) 

获取给定section下的option的值，所以“%”占位符在返回值中被填补，基于构造时传递的默认值，就像option，vars也被提供，除非raw参数为true。

items(section, [, raw[, vars]]) 

返回给定section下的所以option的（name, value）对列表。可选参数同get方法，2.3版本新增。

SafeConfigParser对象 

SafeConfigParser类实现了ConfigParser相同的接口，新增如下方法：

set(section, option, value) 

如果给定的section存在，给option赋值；否则抛出NoSectionError异常。Value值必须是字符串（str或unicode）；如果不是，抛出TypeError异常，2.4版本新增。