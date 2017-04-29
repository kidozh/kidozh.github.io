---
title: 使你的主题更加安全
tags:
  - wordpress
  - 网页
  - 网页安全
id: 1448
categories:
  - 网页
date: 2016-12-30 05:40:24
---

# 前言

我们正准备要开始创建我们主题的模板文件了。在我们做这之前，快速了解数据验证对于WordPress的重要性是非常必要的。

# 为什么主题的安全性很重要？

下面来自WordPress Codex的话很好的回答了这个问题：
> Untrusted data comes from many sources (users, third party sites, your own database!, …) and all of it needs to be validated both on input and output.> 
> 
> “来自许多不可信的来源（例如用户、第三方站点甚至是你自己的数据库）的输入和输出都应该被验证”
我们这里需要假设所有在你WordPress数据库中输入和输出的数据都是不安全的，并且需要根据适用的环境来对数据和内容进行认证。例如，我们不希望在设置页面上的文本框中输入的HTML代码，作为主题文件中的作为HTML运行，因为这可能会破坏我们的布局。 更糟糕的是，如果动态内容的代码是JavaScript或SQL查询，那么您的站点可能会面临[跨站点脚本攻击](http://en.wikipedia.org/wiki/Cross-site_scripting)（XSS）攻击或[SQL注入](http://en.wikipedia.org/wiki/SQL_injection)的风险。

WordPress提供了一系列的函数，这些函数能让我们使得我们的数据变得安全，这些函数能帮助你：

1.  转义一些诸如单双引号、&amp;、大小于符号特殊字符到他们等价的符号(&amp;quot;, &amp;lt;, &amp;gt;, etc)，所以他们不可能作为代码运行。这也被成为输出验证以及转义
2.  确保你输入到数据库之中的内容和你所想的一致（举个例子，检查文字框包含了不含有HTML标签的安全文字）这也被称为输入验证。
在这个指南之中，我们将会关注第一个，转义数据。

第二项也是对于主题搜集来自用户的数据来说非常重要，比如主题选项页面，主题设置。当然这一部分已经超出了这本章的所述范围了。

# 输出转义以及无害化

我们的首要无害化代码的武器就是[esc_attr()](http://codex.wordpress.org/Function_Reference/esc_attr)和[esc_attr_e()](http://codex.wordpress.org/Function_Reference/esc_attr_e) 这两个函数，我们将会在此后使用多次，到时候用的时候我会告诉你们他们究竟是什么。

当我们输出HTML内置的属性的时候，这两个函数都会转义我们上面说的字符（这些字符可能会被错误的解析为代码）。[esc_attr()](http://codex.wordpress.org/Function_Reference/esc_attr)是用于在PHP内部转义代码而[esc_attr_e()](http://codex.wordpress.org/Function_Reference/esc_attr_e)则会在屏幕上显示我们正在转义的代码。

这里就有一个活生生的例子，这个代码我们将会在之后索引页的教程之中使用到这些函数。
<pre class="lang:php decode:true ">&lt;h1 class="entry-title"&gt;&lt;a href="&lt;?php the_permalink(); ?&gt;" title="&lt;?php echo esc_attr( sprintf( __( 'Permalink to %s', 'shape' ), the_title_attribute( 'echo=0' ) ) ); ?&gt;" rel="bookmark"&gt;&lt;?php the_title(); ?&gt;&lt;/a&gt;&lt;/h1&gt;</pre>
这个代码就会显示博文的标题。即使你不知道现在做的是什么，注意一下，我们在`&lt;a&gt;`标签之中，包括了title的标签以及title里面的值esc_attr()。所有包含在HTML属性标签都被认为是不安全的。所以`&lt;?php echo esc_attr( sprintf( __( 'Permalink to %s', 'book' ), the_title_attribute( 'echo=0' ) ) ); ?&gt;`也能包含所有的事情，当然也包含了隐含不安全字符的的内容。

深入这个教程，我们将会看到更多的例子。当然，如果你还想深入了解数据无害化以及验证的话，你也可以查阅Stephen Harris的[Data Validation and Sanitization With WordPress](http://wp.tutsplus.com/tutorials/creative-coding/data-sanitization-and-validation-with-wordpress/) 。

&nbsp;