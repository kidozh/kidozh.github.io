---
title: '[javascript]jQuery入门'
tags:
  - javascript
  - jQuery
id: 765
categories:
  - 网页
date: 2015-12-24 00:54:00
---

# 1 jQuery简介

jQuery是一种流行且易于使用的JavaScript框架。

整个jQuery库仅仅由一个单独的javascript文件组成，其简化了javascript中的包含物。整个jQuery的语法也易于学习。他使用一个简单的命名空间和一致的功能性。和jQuery用户接口插件一起可以创建一个强大的、高度交互的web应用。

# 2 使用jQuery

jQuery可以在[http://www.jquery.com/](http://www.jquery.com/ "jQuery")获取。

## 2.1 两种jQuery下载

jQuery的主页有两种下载可供选择：产品版和开发板。

当我们使用的时候，可以使用内容分发网络（CDN）访问一种托管版本的jQuery。在国外google通过其API网站托管了jQuery和其他库。这样就意味着在建立网站的时候无需在自己的服务器本地托管jQuery。

由于知道的原因，在中国大陆境内访问Google托管的jQuery是较为困难的，所以可以使用下面的方法使用CDN的jQuery：

1\. 360网站卫士托管了google的字体和库，同时在建立网站的时候也可以使用他们的CDN来加速整个网络：

[http://libs.useso.com/](http://libs.useso.com/ "360公共库")

2\. BootCDN托管了其他众多开源库，例如bootstrap、AngularJS，速度较为理想：

[http://www.bootcdn.cn/](http://www.bootcdn.cn/ "BOOTCDN")

3\. 百度静态资源公共库，同时也可以使用百度云加速来对整个网页进行加速：

[http://cdn.code.baidu.com/](http://cdn.code.baidu.com/ "百度")

4\. 七牛云，加速整个网页：

[http://www.qiniu.com/](http://www.qiniu.com/ "七牛")

## 2.2 包含jQuery

使用&lt;script&gt;&lt;/script&gt;包含jQuery，这里使用bootcdn为例子：
<pre class="lang:xhtml decode:true">&lt;script src="//cdn.bootcss.com/jquery/3.0.0-alpha1/jquery.min.js"&gt;&lt;/script&gt;</pre>

##  2.3 基本的jQuery语法

当页面上包含jQuery库时，jQuery增加了一个名为jquery的函数，这里也可以使用jQuery的简单的方法：$()，这样仍可以访问jQuery库，同样的还有以下几种选择器：
<table style="height: 115px;" width="783"><tbody><tr><td>语法</td><td>说明</td></tr><tr><td>$("a")</td><td>文档中所有的&lt;a&gt;元素</td></tr><tr><td>$(document)</td><td>整个文档，通常用来访问ready()函数</td></tr><tr><td>$("#elementID")</td><td>由elementID标识的元素</td></tr><tr><td>$(".className")</td><td>具有className类的元素</td></tr></tbody></table>

jQuery以分号结束，同样的，可以使用单引号和双引号作为jQuery的选择器，两种方法等价。

## 2.4 将jQuery链接到load事件

使用jQuery的最常见的方式就是在界面的load或者onload事件期间连接到元素。在jQuery之中，可以通过document元素的.ready()函数使用，也就是<span class="lang:js decode:true  crayon-inline">$(document).ready()</span> 

使用<span class="lang:js decode:true  crayon-inline" style="font-size: 14px;">$(document).ready()</span><span style="line-height: 22.8571px;"> 的方法就还是按照一般的javascript方法进行：</span>
<pre class="lang:js decode:true">&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Document Ready&lt;/title&gt;
    &lt;!-- jQuery文件。务必在bootstrap.min.js 之前引入 --&gt;
    &lt;script src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;script type="text/javascript"&gt;
    $(document).ready(function(){
        alert('hi!');
    })
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</pre>

 这里jQuery和javascript函数混合在一起，使用jQuery来补充常规的javascript。

<span class="lang:js decode:true  crayon-inline" style="font-size: 14px;">$(document).ready()</span><span style="line-height: 22.8571px;"> 使得函数不惜要使用浏览器的load时间或者在load时间插入一个函数调用，有了</span><span class="lang:js decode:true  crayon-inline" style="font-size: 14px;">$(document).ready()</span><span style="line-height: 22.8571px;"> ，文档对象模型（DOM）的所有元素在.ready()函数执行前都可以使用，尽管不一定对所有的图像。同时</span><span class="lang:js decode:true  crayon-inline" style="font-size: 14px;">$(document).ready()</span><span style="line-height: 22.8571px;"> 也是大部分jQuery编程的**核心**。</span>

# 3 使用选择器

选择器常被用来识别和分组jQuery函数执行的元素，其常常用于手机具有某个标签，ID或者某个应用于他们类的所有元素，这里可以参考CSS的DOM。

## 3.1 根据ID选择元素

<span style="line-height: 22.8571px;">访问全部的就可以用下面的选择器：</span>
<pre class="lang:js decode:true">$("#elementID")</pre>

 而在Javascript中使用的是这样的：
<pre class="lang:js decode:true">getElementByid("elementID");</pre>

##  3.2 根据class选择元素

访问全部的就可以用下面的选择器：
<pre class="lang:js decode:true">$(".className")</pre>

##  3.3 根据类型选择元素

例如要访问所有的a元素的时候：
<pre class="lang:js decode:true">$('a')</pre>

##  3.4 根据层级选择元素

若要选择&lt;div&gt;元素内的所有&lt;a&gt;元素就应该使用：
<pre class="lang:js decode:true">$("div a")</pre>

 如果只想得到元素的直接后代，应该使用大于号：
<pre class="lang:js decode:true">$("div &gt; p")</pre>

 此语法生成所有&lt;div&gt;元素直接后代的&lt;p&gt;元素但是不包含选定&lt;p&gt;元素内的任何&lt;p&gt;元素

也可以使用:nth-child()选择器选择一组中的第n个孩子。例如，选择第三个：
<pre class="lang:js decode:true">$("p:nth-child(3)")</pre>

##  3.5 根据位置选择元素

例如在页面中选择第一个&lt;p&gt;元素：
<pre class="lang:js decode:true">$("p:first")</pre>

 当选择最后一个元素的时候：
<pre class="lang:js decode:true">$("p:last")</pre>

 当选择指定的索引值的元素的时候（第index个元素的时候）：
<pre class="lang:js decode:true">$("p")[index]</pre>

 需要指出的是，数组的索引值以0开头（MATLAB和Pascal这种奇葩）

另外还可以使用：
<pre class="lang:js decode:true">$("p:eq(index)")</pre>

当想使用奇数或者偶数的时候，应选择odd或者even：
<pre class="lang:js decode:true">$("p:odd")
$("p:even")</pre>

 这种方法常常用于控制表格的颜色

## 3.6 根据属性选择元素

当需要选择仅仅包含一个属性的元素或者包含一个具有特定属性的元素的时候，例如，要选择具有alt属性的图像：
<pre class="lang:js decode:true">$("img[alt]")</pre>

 仅选择alt被设置为某个值得图像：
<pre class="lang:js decode:true">$('img[alt="alternative text"]')</pre>

 当使用相同的引号的时候，需要转义内部符号，使用\"来转义

当然jQuery包含不要求属性完全匹配的通配符选择器：
<table style="height: 138px;" width="804"><tbody><tr><td>语法</td><td>说明</td></tr><tr><td>attribute*=value</td><td>选择包含该属性的元素，属性值包含指定的值作为子字符串</td></tr><tr><td><span style="line-height: 15.7143px;">attribute~=value</span></td><td>选择包含该属性的元素，属性的值包含指定的值作为由空格分隔的单词</td></tr><tr><td><span style="line-height: 15.7143px;">attribute!=value</span></td><td>

选择元素，这些元素或者不包含该属性或者该属性值不匹配指定的值
</td></tr><tr><td><span style="line-height: 15.7143px;">attribute$=value</span></td><td>选择包含指定属性的元素，属性以指定字符串结束</td></tr><tr><td><span style="line-height: 15.7143px;">attribute^=value</span></td><td><span style="line-height: 15.7143px;">选择包含指定属性的元素，属性以指定字符串开头</span></td></tr></tbody></table>

## 3.7 选择表单元素

jQuery包含与web相关的本地选择器。
<table style="height: 230px;" width="798"><tbody><tr><td>选择器</td><td>说明</td></tr><tr><td>:checkbox</td><td>选择所有复选框</td></tr><tr><td>:checked</td><td>选择所有被选中的元素</td></tr><tr><td>:input</td><td>选择页面上的所有输入元素</td></tr><tr><td>:password</td><td>选择所有密码输入</td></tr><tr><td>:radio</td><td>选择所有单选按钮输入</td></tr><tr><td>:reset</td><td>选择reset的所有输入类型</td></tr><tr><td>:selected</td><td>选择目前选定的所有元素</td></tr><tr><td>:submit</td><td>选择submit的所有输入类型</td></tr><tr><td>:text</td><td>选择text的所有输入类型</td></tr></tbody></table>

## 3.8 更多的选择器

例如所有隐藏元素或者所有不可见元素以及激活元素、禁用元素以及其他元素的选择器。

可以参考[http://api.jquery.com/catagory/selectors/](http://api.jquery.com/catagory/selectors/)可以得到一个完整的且最新的jQuery选择器列表

# 4 函数

## 4.1 遍历DOM

可以使用<span class="lang:js decode:true  crayon-inline ">.each()</span> 函数接受一个选定元素的列表并且遍历其中的每个元素，使用遍历函数的时候，需要用户自定义封装类型函数和<span class="lang:js decode:true  crayon-inline ">$(this)</span> 选择器只想当前的对象，也就可以遍历当前元素了。

在之前的我们的rating System里面，我们需要对大于某个值的数字进行特定的css样式识别，所以我加入了这一段jQuery代码：
<pre class="lang:js decode:true">$('rating').each(function(){
	if($(this).text()&gt;=2000){
		$(this).css('font-weight','bold');
	}
})</pre>

 这段代码使用了一个选择器收集所有class=rating的元素，接着使用jQuery的<span class="lang:js decode:true  crayon-inline " style="font-size: 14px;">.each()</span><span style="line-height: 22.8571px;"> 函数访问其中的每一个元素。在</span><span class="lang:js decode:true  crayon-inline" style="font-size: 14px;">.each()</span><span style="line-height: 22.8571px;"> 函数内，一个用户自定义函数执行一个条件来确定rating列中的值是否大于或者等于2000，如果是，代码调用.css()函数来为该元素添加一个font-weight属性并且将其设置为bold。</span>

在这里我们必须强调<span class="lang:js decode:true  crayon-inline ">.parent()</span> 函数的使用，其从根本上升级了DOM树已找到包含特定元素的父标签，这样就可以对父标签的元素进行修改。<span class="lang:js decode:true  crayon-inline ">.parent()</span> 函数引入了一个名为Chaining的概念，他能提供额外级别的选择以及函数的多级应用，当然，这样也可能链接到难以阅读和维护的代码。党被链接的选择器元素发生改变的时候，Chaining会生成脆弱代码。

使用jQuery操作CSS样式类的方法主要包括：
<pre class="lang:tex decode:true">.hasClass()
.addClass()
.removeClass()
.toggleClass()</pre>

## 4.2 操作属性

jQuery操作DOM属性的函数常见的有<span class="lang:tex decode:true  crayon-inline">.attr()</span> ，<span class="lang:tex decode:true  crayon-inline ">.html()</span> ，<span class="lang:tex decode:true  crayon-inline ">.val()</span> 以及其他函数，<span class="lang:tex decode:true  crayon-inline" style="font-size: 14px;">.attr()</span><span style="line-height: 22.8571px;"> 被用于获取和设定属性，例如可以使用下列的方法设置一个图像的alt属性：</span>
<pre class="lang:js decode:true">$("#elementID").attr("alt","newText")</pre>

_ 在设置元素之前获取它的值是没有意义的。_

## 4.3 修改文档和HTML

可以使用.text()和.val()这样的函数全部重写页面，但是这样并不是个好的方法。有的时候还是需要重写部分HTML或者修改文本或者值。

比如以下方法：
<pre class="lang:js decode:true">$("#elementID").html('&lt;span class="redStyle"&gt;This is red text.&lt;/span&gt;');</pre>

 这段的输出就是，由elementID表示的元素现在包含一个带有示例代码所示的新文本的&lt;span&gt;元素。

和<span class="lang:js decode:true crayon-inline">.html()</span> 函数一样，其支持选定元素对于文本的获取以及设置，与HTML不同的是<span class="lang:js decode:true  crayon-inline ">.text()</span> 函数只获取或者设置文本，因此其不可能修改选定元素的实际HTML。

## 4.4 插入元素

使用jQuery可以容易在页面中添加元素，主要采用的是<span class="lang:js decode:true  crayon-inline ">.after()</span> 和<span class="lang:js decode:true  crayon-inline ">.before()</span> 函数，正如其名由于，他们分别表示在选定元素后面或者前面添加元素。
<pre class="lang:js decode:true" style="font-size: 14px; line-height: 1.42857;">$("#elementID").after('&lt;span class="redStyle"&gt;This is red text.&lt;/span&gt;');</pre><pre class="lang:js decode:true" style="font-size: 14px; line-height: 1.42857;">$("#elementID").before('&lt;span class="redStyle"&gt;This is red text.&lt;/span&gt;');</pre>

<span class="lang:js decode:true  crayon-inline">.append()</span> 函数的工作方式基本与上面一样，但是<span class="lang:js decode:true  crayon-inline ">.append()</span> 函数在他所附加的元素**内**插入HTML代码，比如：
<pre class="lang:js decode:true">$(document).ready(function(){
    $('body').append('&lt;div id="myDiv"&gt;Adding a element&lt;/div&gt;'); 
})</pre>

与<span class="lang:js decode:true  crayon-inline ">.after()</span> 不同，采用<span class="lang:js decode:true  crayon-inline ">.append()</span> 方法的输出将在&lt;body&gt;以内，而前者则会在body之外，这显然是不理想的

# 5 更多jQuery参考资源

可以参见jQuery官网。

[http://www.jquery.com/](http://www.jquery.com/ "jQuery")

目前其可以在国内正常访问。