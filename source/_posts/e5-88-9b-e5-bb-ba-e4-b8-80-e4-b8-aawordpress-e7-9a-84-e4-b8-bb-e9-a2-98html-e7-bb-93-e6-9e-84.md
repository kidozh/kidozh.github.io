---
title: 创建一个WordPress的主题HTML结构
tags:
  - wordpress
  - 网页
id: 1389
categories:
  - 网页
date: 2016-10-30 01:09:47
---

# 前言

现在我们着手进入到WordPress的真正开发阶段：开始编写HTML结构

# 建立HTML结构的目的

当我们编写一个网站的时候，你一定会有两个目标：使代码精简并且有意义。这样就是说，尽可能使用少的标记（也就是HTML的标签）并且保证使用类和ID名称使得标记有意义。举个例子，对于小工具栏，你应该使用`class=”widget-area”` 而不是 `class=”sidebar-left”`。

现在当我们编写一个WordPress的主题（或者任何针对内容管理系统的模板）的时候，我们需要找到一种介于精简代码和我们称之为[冗余](http://www.456bereastreet.com/lab/web_development_mistakes/)的东西。代码里包含了很多不必要的`div`元素。换句话说，有很多冗余结构。你可能在浏览网页或者WordPress的主题的源代码时候见过div。你可以把他们作为HTML代码的一个容器 - 这个容器对于使用CSS来操作HTML代码来说很方便。当然我们也会有一些，但是我们不会想要太多的以及没有意义的标签。

有一些诸如`header`、`nav`和`footer`的标签，HTML5已经使得我们对于有意义的布局的请求变得更为简单。这些信的主题和div标签很相似，并且这些标签能够作为HTML代码的容器。同样的，他们也能够允许我们创造一个更能描述HTML大纲的框架。

所以我们已经有很好的框架了，使用在HTML5新的标签，这样我们能够针对我们的博客和站点布局来进行代码复用。

# 针对WordPress主题的HTML结构

让我们看一看我们将会使用在WordPress主题主体的HTML结构。

<pre class="lang:xhtml decode:true ">&lt;div id="page" class="hfeed site"&gt;
     &lt;header id="masthead" class="site-header" role="banner"&gt;
          &lt;hgroup&gt;&lt;/hgroup&gt;
          &lt;nav role="navigation" class="site-navigation main-navigation"&gt;&lt;/nav&gt;&lt;!-- .site-navigation .main-navigation --&gt;
     &lt;/header&gt;&lt;!-- #masthead .site-header --&gt;
     &lt;div id="main" class="site-main"&gt;
          &lt;div id="primary" class="content-area"&gt;
               &lt;div id="content" class="site-content"&gt;
               &lt;/div&gt;&lt;!-- #content .site-content --&gt;&lt;/div&gt;
          &lt;!-- #primary .content-area --&gt;
          &lt;div id="secondary" class="widget-area"&gt;
          &lt;/div&gt;&lt;!-- #secondary .widget-area --&gt;
          &lt;div id="tertiary" class="widget-area"&gt;
          &lt;/div&gt;&lt;!-- #tertiary .widget-area --&gt;&lt;/div&gt;
     &lt;!-- #main .site-main --&gt;
     &lt;footer id="colophon" class="site-footer" role="contentinfo"&gt;
          &lt;div class="site-info"&gt;
          &lt;/div&gt;&lt;!-- .site-info --&gt;
     &lt;/footer&gt;&lt;!-- #colophon .site-footer --&gt;
&lt;/div&gt; &lt;!-- #page .hfeed .site --&gt;</pre>

事实上，这个HTML组成了_s的脊梁。继续把这个粘到你的文本编辑器并且把他存到一个顺手的地方，当我们勾践文件结构的时候，我们将会稍后使用到它。但是在这之前，我们还是要看一些事情。

# WordPress主题HTML快速的预览

[caption id="attachment_1390" align="aligncenter" width="768"]![一个HTML的样例，点击获得大尺寸图片](http://kidozh.com/wp-content/uploads/2016/10/html-visual1.png) 一个HTML的样例，点击获得大尺寸图片[/caption]

看一下上面的HTML结构。块的颜色越深，也就代表其布局也越深。这些块的布局是由CSS所大致决定的，这些内容我们在后面会提到。

你也可以编辑HTML结构来满足你的需要。举个例子，你可以把导航（navigation）块移出`header`块或者把小工具（widget）块放进页脚（footer）块。根据这个指南的入门，我们将会使用CSS来安排我们的内容和小工具界面。

那么现在我们就开始写一点代码吧。

首先，在内容页的类，`hfeed`，`hfeed`是hatom Microformat schema的一部分。用简单的英语来说，就是告诉计算机来阅读这个内容（比如搜索引擎的爬虫或者其他服务都会通过这个来访问）。

看下文件结构中的`header`和`footer`的，你可能已经注意到了HTML5的新特征`header`和`footer`。这些标签描述了文件的广义小节。通过借用这些类名称，我将会向标记中添加更多的信息。

你将会发现了在HTML标签中的`ARIA`  `role`这个属性。这个role属性能够帮助一些残障辅助工具也来浏览你的站点。你可以在这里获得更多这一点的信息。

在我们HTML的主要区域中，注意一下我们的小工具块是在内容块之后的。你也许发现了我们的内容是在一个容器div（类名为‘content-area ’）这就是关键。它不仅让我们的主要内容在搜索引擎优先发现，而且使用CSS的时候也能精简CSS代码。

这个HTML的结构将会是你WordPress的未来框架，并且也会告诉你怎么使用CSS和这个强大的功能所搭配。