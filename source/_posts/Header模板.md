---
title: Header模板
id: 1454
date: 2017-06-30 21:43:34
categories:
  - 未分类
tags:
---

# 前言

现在让我们开始创建主题把！

构建你的`header.php`并且使用HTML Doctype验证你的主题。在这个教程里可能会有大量的PHP代码，但是这一点也不重要。我们正要准备开始针对搜索引擎做一些优化，并且向`functions.php`文件之中添加一些东西。

这个教程假设你已经向你的header.php之中添加了一些基本的元素，如果你的header.php这个文件还是空的话，情查看之前的教程，再来一遍。

# 头文件部分

现在你的空的WordPress主题在实际上来说是无用的。因为这是因为其缺失了`DocType`来指示浏览器如何编译HTML的造型。我们正要使用HTML5的`DocType`。HTML5现在能够很好的适用于我们的WordPress主题。

首先，打开`header.php`并且把下面的代码粘到里面。

```php
<?php
/**
 * The Header for our theme.
 *
 * Displays all of the <head> section and everything up till <div id="main">
 *
 * @package Shape
 * @since Shape 2.0
 */
?><!DOCTYPE html>
```


 