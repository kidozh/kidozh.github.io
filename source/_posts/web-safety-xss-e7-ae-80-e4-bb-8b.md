---
title: '[Web Safety] XSS简介'
tags:
  - 网页
  - 网页安全
id: 385
categories:
  - 安全工程
date: 2015-08-05 18:11:23
---

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">    XSS,</span><span style="color: #333333; font-family: Arial; font-size: 10pt; background-color: white;">
 </span><span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">跨站脚本攻击（Cross Site Script Attack）,一种很常见的攻击方法。</span>

1\. 一个简单的简单的XSS示例PHP示例
<pre class="lang:default decode:true ">&lt;html&gt;
&lt;head&gt;&lt;/head&gt;
&lt;?php
        $input = $_GET["param"];
        echo "&lt;div&gt;".$input."&lt;/div&gt;"
    ?&gt;
&lt;/html&gt;</pre>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">这个时候我们在本地的PHP服务器中创建了一个带有GET的网页，这种不加区分的GET方法就是一个很简单的XSS注入点。
</span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">当我们插入这样的代码：（好像拿Chrome浏览器就不会alert）
</span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">    [http://localhost/chart.php?param=%3Cscript%3Ealert(/xss/)%3C/script%3E%3C/div%3E](http://localhost/chart.php?param=%3Cscript%3Ealert(/xss/)%3C/script%3E%3C/div%3E)
</span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">也就是[http://localhost/chart.php?param=&lt;script&gt;alert(/xss/)&lt;script&gt;&lt;div](http://localhost/chart.php?param=%3cscript%3ealert(/xss/)%3cscript%3e%3cdiv)&gt;
</span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">这个时候，对话框就出现/XSS/了，意味着代码被执行了。
</span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">    ![](/wp-content/uploads/2015/08/080515_1010_WebSafetyXS1.png)
</span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">这个时候我们查看源代码就发现用户输入的内容被错误的认为是JavaScript被执行了。</span>
<pre class="lang:default decode:true ">&lt;html&gt;
    &lt;head&gt;

    &lt;/head&gt;
    &lt;body&gt;
        &lt;div&gt;
            &lt;script&gt;
				alert(/xss/)
			&lt;/script&gt;
        &lt;/div&gt;
    &lt;/body&gt;
&lt;/html&gt;</pre>

*   <div><span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">第一种类型：反射型XSS（非持久性XSS）
 </span></div>

    <span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">上面简单的例子就是一个很简单的反射型XSS，他只是一个简单的把用户输入的数据"反射"给浏览器。也就是说只有诱骗用户点击一个恶意链接的时候，才能攻击成功。
 </span>

*   <div><span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">第二种类型：储存型XSS
 </span></div>

    <span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">存储型XSS会把用户的数据储存在服务器上，在用户访问该服务器的时候将会运行该JavaScript，从而导致XSS攻击。比如，一个很常见的例子，攻击者在某论坛上发表了一个带有恶意JavaScript的博客文章，所有访问该文章的用户都会执行这段恶意的JavaScript代码。这种往往是对于标签的过滤不到位导致的。
 </span>

*   <div><span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">第三种类型：DOM Based XSS
 </span></div>

    <span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">这种XSS原理上来说也是反射性XSS，但是由于这个是因为修改DOM节点的XSS，所以被称为DOM Based XSS。同样的使用本地服务器做演示。
 </span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">PHP代码如下：
 </span><pre class="crayon-selected">[php]
&amp;amp;amp;amp;lt;html&amp;amp;amp;amp;gt;
    &amp;amp;amp;amp;lt;head&amp;amp;amp;amp;gt;&amp;amp;amp;amp;lt;/head&amp;amp;amp;amp;gt;
    &amp;amp;amp;amp;lt;script&amp;amp;amp;amp;gt;
    function test(){
        var string = document.getElementById(&quot;text&quot;).value;
        document.getElementById(&quot;t&quot;).innerHTML = &quot;&amp;amp;amp;amp;lt;a herf = '&quot;+string+&quot;'&amp;amp;amp;amp;gt;testLink&amp;amp;amp;amp;lt;/a&amp;amp;amp;amp;gt;&quot;;
    }
    &amp;amp;amp;amp;lt;/script&amp;amp;amp;amp;gt;
    &amp;amp;amp;amp;lt;div id = &quot;t&quot;&amp;amp;amp;amp;gt;&amp;amp;amp;amp;lt;/div&amp;amp;amp;amp;gt;
    &amp;amp;amp;amp;lt;input type = &quot;text&quot; id = &quot;text&quot; value = &quot;&quot; /&amp;amp;amp;amp;gt;
    &amp;amp;amp;amp;lt;input type = &quot;button&quot; id = &quot;s&quot; value = &quot;write&quot; onclick = &quot;test()&quot;/&amp;amp;amp;amp;gt;
&amp;amp;amp;amp;lt;/html&amp;amp;amp;amp;gt;

[/php]</pre>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">点击write之后，a标签后面出现一个超链接，链接地址就是input里面的地址，当按下button之时，test这个函数既可以触发，通过innerHTML将input里面的值写入html志宏，这就是DOM Based XSS发生的原因。
 </span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">和XSS一样，为了融入HTML之中，我们构造：
 </span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">' onclick = alert(/xss/) //
 </span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">那么再输入之后，页面代码就变成了：
 </span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">&lt;a herf = '' onclick = alert(/xss/) //'&gt;testLink&lt;/a&gt;
 </span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">首先用一个单引号闭合原来herf之后的单引号，然后插入一个onclick事件，最后使用注释符"//"注释掉第二个单引号，那么点击的时候，事件被执行…
 </span>

![](/wp-content/uploads/2015/08/080515_1010_WebSafetyXS2.png)<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">
 </span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">然而遵循这种思路，我们还有另一种利用方式，通过闭合&lt;a&gt;标签，插入一个新的HTML标签，尝试以下输入：
 </span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">'&gt;&lt;img src = # onerror = alert(/xss2/) /&gt;&lt;'
 </span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">那么代码id = t将变成：
 </span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;"> &lt;a herf = ''&gt;&lt;img src = # onerror = alert(/xss2/) /&gt;&lt;''&gt;testLink&lt;/a&gt;
 </span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;"> 脚本被执行。
 </span>

![](/wp-content/uploads/2015/08/080515_1010_WebSafetyXS3.png)<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">
 </span>

<span style="font-family: Microsoft YaHei Mono; font-size: 14pt;">XSS 被执行。</span>