---
title: 创建一个WordPress主题
tags:
  - wordpress
  - 模板
  - 网页
id: 1366
categories:
  - 网页
date: 2016-10-19 21:54:23
---

# 来源

翻译自[https://themeshaper.com/2012/10/22/the-themeshaper-wordpress-theme-tutorial-2nd-edition/](https://themeshaper.com/2012/10/22/the-themeshaper-wordpress-theme-tutorial-2nd-edition/)

# 前言

在仅仅的16个课程里，这个WordPress主题知道将会告诉你如何开始构建一个强大而与时俱进的WordPress主题。在接下来的课程之中，我会解释一些或好或坏的我对于一些特定技术的理解以及我选择某项技术的原因。更为重要的是，我会告诉你一切和WordPress主题开发相关的任何事情。

在这个入门之中，你能够随心所欲的开发WordPress了。

![theme-shaper-cloud1](http://kidozh.com/wp-content/uploads/2016/10/theme-shaper-cloud1.png)

# 下划线(_s)的开始主题的入门

如果你还没有听说过`_s`，简而言之，这是一个100%的GPL，由社区开发的开始主题。这个主题包含了一些现代化的模板，初学者的CSS和一个组织良好的文件结构。这意味着，你所需要做的就只是从头开始设计。你也可以使用`_s`作为你将来主题开发大厦的一块奠基石。如果你想了解更多`_s`背后的故事，你也可以花些时间来看看[A 1000-Hour Head Start: Introducing the _s Theme.](https://themeshaper.com/2012/02/13/introducing-the-underscores-theme/)

我们将要在这个入门里将会构建一个很简单的主题，[shape](https://themeshaper.files.wordpress.com/2014/03/shape1.zip)（这个主题在入门的第一版里被提到了，现在他会为第二版做出一些更新），这个主题也基于`_s`。如果你想看我们将来要完成的代码，那么不妨下载并且略观一二。在我们学习CSS的课程之前，显然这是比较乏力的。但是如果你想看看我们最终创建shape这个主题的设计思路的话，你就可以[点这里](https://themeshaper.files.wordpress.com/2013/10/shape-sample-style.zip)了。

## 历史的一些包袱

如果你阅读了这篇第一版的入门指南，那么我会告诉你，第一版中的代码有些已经过时了。但这还好，因为更重要的事情就是你能够理解一些很宽泛的概念，这也是为什么他们仍在这里抛头露面的原因。同样的，你也可以在这里获得一份关于[ the latest _s source code from the GitHub repository](https://github.com/automattic/_s)的复印件。

下面是一些你可能会涉及到关于主题的内容：

*   一个良好组织并且模块化的文件结构
*   一些实用的针对搜索引擎的优化
*   谷歌支持的[Microformat](http://google.com/support/webmasters/bin/answer.py?answer=146897)的语义
*   有效并且具有逻辑的语义标记结构，这个结构能够创建ANY布局
*   智能的CSS布局
*   支持本地化：支持翻译以及从右到左的层叠表
*   动态的主体，文章和评论CSS类
*   分离的回溯和评论系统
*   两个小工具区域，第一个是默认的小工具，第二个当其为空的时候就会消失
*   对于`Aside`投稿格式的支持（在这个教程节数之后，你就能够轻松的对更多博客格式给予支持）
*   一个自定义的目录，弹性的自定义头图片和一个自定义的背景
*   一个简单的响应式样式，包括一个对移动设备轻量化的导航菜单
*   还有你想获得的所有WordPress的资料

我认为对任何WordPress主题这也是重要的。

&nbsp;

&nbsp;