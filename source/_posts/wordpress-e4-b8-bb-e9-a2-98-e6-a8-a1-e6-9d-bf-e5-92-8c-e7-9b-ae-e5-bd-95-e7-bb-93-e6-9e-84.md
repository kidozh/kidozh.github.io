---
title: WordPress主题模板和目录结构
tags:
  - wordpress
  - 网页
id: 1393
categories:
  - 网页
date: 2016-11-03 07:29:30
---

# 前言

对于WordPress而言，WordPress主题可能只需要一个`index.php`模板和一个`style.css`的文件。但是大多数的WordPress主题还是需要一些更为坚实的东西。

# 开始

让我们创建一些文件和目录来装饰我们基于`_s`的主题，shape。

在wp-content/themes/目录下创建你的主题，在这个指南中，我们称之为shape。当然，这也可以是你想要的任何文件，接下来我们将会创建下面的空白文件和文件夹。

*   inc (folder)
*   js (folder)
*   languages (folder)
*   layouts (folder)
*   404.php
*   archive.php
*   comments.php
*   content.php
*   content-aside.php
*   content-page.php
*   content-single.php
*   footer.php
*   functions.php
*   header.php
*   index.php
*   no-results.php
*   page.php
*   search.php
*   searchform.php
*   sidebar.php
*   single.php
*   license.txt
*   rtl.css
*   style.css

现在让我们在文本编辑器里打开我们创建的最后的文件`style.css`。我们需要做的第一件事情就是在CSS文件的头几行内加入CSS注释（以`/* */`开头和结尾）。在这里，我们将会把一些信息写入CSS文件中，这些信息将会告知WordPress你的主题。没有这个，你的主题将不会在主题栏之中显示。

我将会使用Shape作为主题名称，但是你想用啥名字都无所谓。同时，你需要填入author（作者），URLs（地址栏）和你的主题的说明信息。

```css
/*
Theme Name: Shape
Theme URI: https://themeshaper.com/
Author: ThemeShaper
Author URI: https://themeshaper.com/
Description: The Shape theme is a simple, minimalist theme based on Underscores and the original Shape Theme by Ian Stewart. It was created especially as a learning theme for The ThemeShaper WordPress Theme Tutorial: 2nd Edition.
Version: 2.0
License: GNU General Public License
License URI: license.txt
Tags: light, white, one-column, two-columns, left-sidebar, right-sidebar, flexible-width, custom-backgroud, custom-header, custom-menu, featured-images, flexible-header, microformats, post-formats, rtl-language-support, threaded-comments, translation-ready
This theme, like WordPress, is licensed under the GPL.
Use it to make something cool, have fun, and share what you've learned with others.
*/
```


让我们挨个看这些元素，这样你就会知道他们在说什么了。

*   Theme Name - 你的主题名称
*   Theme URL - 你主题主页在网络中的地址。这可以是你网站的某一部分。举个例子，许多的主题作者都可能使用类似于这样的地址：[http://yourgroovydomain.com/your-theme/&#8221](http://yourgroovydomain.com/your-theme/&#8221)
*   Author - 自我说明，当然也就是你的名字咯
*   Author URL - 连接到你的网站
*   Description - 提供一个你主题的简短而清晰的说明，你可以用几句话总结你创建主题的目的以及主题的特性。当用户搜索主题的时候，这个说明将会出现在用户的仪表盘（Dashboard）之中，当然也有可能出现在WordPress.org免费主题库之中
*   Version - 你主题的版本号。这取决于你是如何对你的版本进行编号，倘若主题是全新的，你也可以从1.0开始命名主题版本号。如果你已经释出了更新，你就能够相应的更改版本号。
*   License - 你的主题协议。如果你想发布你的主题，你就必须要使用GPL协议了，这也正是WordPress使用的。
*   License URL - 提供一个用户能找到协议文本的链接。我们的主题将会包含一个`license.txt`文件，这个文件我们将会在如何分发WordPress主题那一节上提到
*   Tags - 这些文字（标签）将会描述你主题的特性，颜色和主题。如果你想分发你的主题的话，他们就是必要的。这些标签允许人们去按照颜色主题等来检索主题。[这里是一些支持的标签](http://wordpress.org/extend/themes/about/)。

需要注意的事情：这些东西很多都是可选的。事实上，你只需要主题名称就够了。但是一旦你计划要发布你的主题或者你想为某个人做一个自定义的注意的话，你就需要包含上面的东西了。最后，我希望你不要对这些琐事感到一头雾水。

一旦你做到这些之后，你就可以激活你的注意并且访问你的测试站点了。我们已经完成了我们的空主题了。事情将会开始变得有趣。

# 构建你的HTML结构

现在我们将会从前面的教程中使用我们的HTML结构。但是让我们还是学一点关于WordPress和模板的东西吧。

WordPress真的只需要一个模板文件，`index.php`。我们能够并且将会针对一些特殊的场合使用一系列模板文件（单个文章，归档，页面等）而不是`index.php`。但是在最开始，`index.php`才是我们所需要的。

现在，`index.php`和所有相关的文件都构成了我们在浏览器看到的种种。他们是由一些HTML和PHP渲染而成的。

让我们想想一些类似小说的网页，其包含了开头中间和结尾。当我们写入我们的index.php文件的时候（接下来就是我们的`single.php`，`category.php`等文件），我们将只会留心与中间的部分。但是我们将会直接引用开头和结尾的那一部分。我们可能需要复写我们的中间部分因为我们只想一次性的搞定开头和结尾的网页页面。

## Header.php和Footer.php

在我们之前的创建的HTML结构查看并且把所有的代码粘贴到这里并且在`header.php`之中应该包含`<div id="main">`。它看起来应该像这样：

```xhtml
<div id="page" class="hfeed site">
     <header id="masthead" class="site-header" role="banner">
         <hgroup></hgroup>
         <nav role="navigation" class="site-navigation main-navigation"></nav><!-- .site-navigation .main-navigation -->
     </header><!-- #masthead .site-header -->
<div id="main" class="site-main">
```


现在在后面复制所有事情，包含</div><!– #main –>在`footer.php`之中，它看起来可能是这样：

```xhtml
</div><!-- #main .site-main -->
     <footer id="colophon" class="site-footer" role="contentinfo">
          <div class="site-info"></div><!-- .site-info -->
     </footer><!-- #colophon .site-footer -->
</div><!-- #page .hfeed .site -->
```


## sidebar.php

把下面的代码复制到`sidebar.php`之中：

```xhtml
<div id="secondary" class="widget-area">
</div><!-- #secondary .widget-area -->

<div id="tertiary" class="widget-area">
</div><!-- #tertiary .widget-area -->
```


## index.php

我猜你们已经知道我们要做什么了。把下面的代码复制到#main div 之中而在#primary 闭合之前，那么差不多看成这样：

```xhtml
<div id="primary" class="content-area">
    <div id="content" class="site-content" role="main">
    </div><!-- #content .site-content -->
</div><!-- #primary .content-area -->
```


只需要两个很小几部，我们就会有一个完美的WordPress主题。我们需要在`header`，`sidebar`和`footer`之中调用这些函数。

在`index.php`的页首，我们需要添加模板标签：

```php
<?php get_header(); ?>
```


很好！那么在页尾，我们需要添加

```php
<?php get_sidebar(); ?>
<?php get_footer(); ?>
```


是的，现在我们就能够看到WordPress的主要文件index.php了。其有在页首调用了开始页，而在页尾也会调用函数。

重新加载页面并且检出代码，这样就是你的代码了！