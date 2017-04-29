---
title: '[JavaScript]JavaScript初探'
tags:
  - javascript
  - 网页
id: 680
categories:
  - 网页
date: 2015-12-09 21:39:03
---

# 1\. JavaScript程序的构成

JavaScript程序有语句和表达式构成，而表达式由各种类别的令牌组成，包含了关键字、直接量、分隔符、操作符和标识符，他们以一种对大部分web浏览器都包含的解释器有意义的顺序放在一起。

表达式实例如下：

在这个表达式中，有一个标记或者保留字<span style="color: #00b050;">var</span>，后面跟着其他标记:一个标识符（smallNumber）、一个操作符（=）和一个直接量（4）.

# 2.使用javascript伪协议和函数

2.1首先，打开一个浏览器（Chrome和Firefox优先）。

2.2在地址栏中输入以下代码并且按下Enter键：

<span class="lang:js decode:true  crayon-inline ">javascript:alert("Hello World")</span> 

2.3 按下Enter键之后就能看出来<span style="color: #c00000;">alert</span>对话框

这里，Javascript代码包含了两项比较重要的内容：浏览器中的javascript伪协议标识符和alert函数。

# 3.JavaScript的意义

javascript也是事件驱动的，也就是说他能够对某些事情做出相应，例如鼠标的点击和表单字段的文本变动。

# 4.JavaScript在网页上的应用

javascript应放在&lt;script&gt;标签内，而<span style="line-height: 22.8571px;">&lt;script</span><span style="line-height: 22.8571px;">&gt;标签位于网页的&lt;head&gt;&lt;/head&gt;或者&lt;body&gt;&lt;/body&gt;之内。</span>

位于&lt;body&gt;标签内的JavaScript在浏览器遇到他的时候开始执行，如果需要使用JavaScript函数的write函数，就需要在body内部放置javascript的代码。

<pre class="lang:php decode:true ">&lt;html&gt;
    &lt;head&gt;
        &lt;meta name="generator"
        content="HTML Tidy for HTML5 (experimental) for Windows https://github.com/w3c/tidy-html5/tree/c63cc39" /&gt;
        &lt;title&gt;Test Page For JavaScript&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;h3 class="demo-panel-title"&gt;Input&lt;/h3&gt;
        &lt;div class="row"&gt;
            &lt;div class="col-xs-3"&gt;
                &lt;div class="form-group"&gt;
                    &lt;input type="text" value="" placeholder="Inactive" class="form-control" /&gt;
                &lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="col-xs-3"&gt;
                &lt;div class="form-group has-error"&gt;
                    &lt;input type="text" value="" placeholder="Error" class="form-control" /&gt;
                &lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="col-xs-3"&gt;
                &lt;div class="form-group has-success"&gt;
                    &lt;input type="text" value="" placeholder="Success" class="form-control" /&gt;
                &lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="col-xs-3"&gt;
                &lt;div class="form-group"&gt;
                    &lt;input type="text" value="Disabled" disabled="disabled" class="form-control" /&gt;
                &lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;
        &lt;!-- /row --&gt;
    &lt;/body&gt;

	&lt;script type="text/javascript"&gt;
		document.write("hello");
		document.write(" world");

	&lt;/script&gt;

&lt;/html&gt;
</pre>

 由于Javascript加载的阻塞输入，通常在HTML中放置javascript的最好位置是将其置于&lt;body&gt;元素的结尾而不是&lt;head&gt;内。

# 5.XHTML页上的问题

在可扩展超文本标记语言（XHTML）页面上使用Javascript的时候，小于号(&lt;)和与字符(&amp;)被解释为XML，而对于Javascript可能会引发问题，为了避免这个问题，在XHTML页面中应使用以下语法：
<pre class="lang:xhtml decode:true ">&lt;script type="text/javascript"&gt;
&lt;![CDATA[
	// JavaScript Goes Here!

]]&gt;

&lt;/script&gt;</pre>

 而对于不兼容XHTML的浏览器不能正确解释CDATA部分。可以通过将CDATA部分放置在Javascript内的一个或者几个以双斜线打头的注释内来解决这个问题。
<pre class="lang:xhtml decode:true ">&lt;script type="text/javascript"&gt;
//&lt;![CDATA[
	// JavaScript Goes Here!

//]]&gt;

&lt;/script&gt;</pre>

 而一般的文档类型声明（DOCTYPE声明），这个能告诉浏览器知道解析文档元素是应该遵循的规则，HTML 5使用更简单的DOCTYPE

&lt;!DOCTYPE html&gt;

# 6.JavaScript的作用范围

javascript可以在日常的程序客户端执行很多任务。包含了创建下拉菜单、转换页面上的文本、为页面添加动态元素、辅助表单输入等方式来为网站添加所需的交互性。

javascript不能强加于客户端，由于其以来其他界面和宿主程序来实现功能，而一些宿主程序有的时候根本不支持javascript（由于弹出广告而屏蔽javascript）。同样的，Javascript不能保证数据的安全性，我们不能相信从客户端返回的任何数据（XSS），如果你天真的相信客户端的Javascript函数已经检查了数据并且确保他是有效的，可能会发现无效的数据返回到服务器，造成无法预料并且**严重**的后果。最后Javascript不能跨域，由于浏览器的同源策略（也就是位于A网页下的javascript不能访问任何其他域内执行的Javascript），也就是javascript必须在相同位置执行或者javascript必须来自同一位置。