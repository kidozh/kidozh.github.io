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

    XSS,
 跨站脚本攻击（Cross Site Script Attack）,一种很常见的攻击方法。

1\. 一个简单的简单的XSS示例PHP示例
```default
<html>
<head></head>
<?php
        $input = $_GET["param"];
        echo "<div>".$input."</div>"
    ?>
</html>
```


这个时候我们在本地的PHP服务器中创建了一个带有GET的网页，这种不加区分的GET方法就是一个很简单的XSS注入点。


当我们插入这样的代码：（好像拿Chrome浏览器就不会alert）


    [http://localhost/chart.php?param=%3Cscript%3Ealert(/xss/)%3C/script%3E%3C/div%3E](http://localhost/chart.php?param=%3Cscript%3Ealert(/xss/)%3C/script%3E%3C/div%3E)


也就是[http://localhost/chart.php?param=<script>alert(/xss/)<script><div](http://localhost/chart.php?param=%3cscript%3ealert(/xss/)%3cscript%3e%3cdiv)>


这个时候，对话框就出现/XSS/了，意味着代码被执行了。


    ![](/wp-content/uploads/2015/08/080515_1010_WebSafetyXS1.png)


这个时候我们查看源代码就发现用户输入的内容被错误的认为是JavaScript被执行了。
```default
<html>
    <head>

    </head>
    <body>
        <div>
            <script>
				alert(/xss/)
			</script>
        </div>
    </body>
</html>
```


*   第一种类型：反射型XSS（非持久性XSS）
 

    上面简单的例子就是一个很简单的反射型XSS，他只是一个简单的把用户输入的数据"反射"给浏览器。也就是说只有诱骗用户点击一个恶意链接的时候，才能攻击成功。
 

*   第二种类型：储存型XSS
 

    存储型XSS会把用户的数据储存在服务器上，在用户访问该服务器的时候将会运行该JavaScript，从而导致XSS攻击。比如，一个很常见的例子，攻击者在某论坛上发表了一个带有恶意JavaScript的博客文章，所有访问该文章的用户都会执行这段恶意的JavaScript代码。这种往往是对于标签的过滤不到位导致的。
 

*   第三种类型：DOM Based XSS
 

    这种XSS原理上来说也是反射性XSS，但是由于这个是因为修改DOM节点的XSS，所以被称为DOM Based XSS。同样的使用本地服务器做演示。
 

PHP代码如下：
 
```
[php]
&amp;amp;amp;lt;html&amp;amp;amp;gt;
    &amp;amp;amp;lt;head&amp;amp;amp;gt;&amp;amp;amp;lt;/head&amp;amp;amp;gt;
    &amp;amp;amp;lt;script&amp;amp;amp;gt;
    function test(){
        var string = document.getElementById("text").value;
        document.getElementById("t").innerHTML = "&amp;amp;amp;lt;a herf = '"+string+"'&amp;amp;amp;gt;testLink&amp;amp;amp;lt;/a&amp;amp;amp;gt;";
    }
    &amp;amp;amp;lt;/script&amp;amp;amp;gt;
    &amp;amp;amp;lt;div id = "t"&amp;amp;amp;gt;&amp;amp;amp;lt;/div&amp;amp;amp;gt;
    &amp;amp;amp;lt;input type = "text" id = "text" value = "" /&amp;amp;amp;gt;
    &amp;amp;amp;lt;input type = "button" id = "s" value = "write" onclick = "test()"/&amp;amp;amp;gt;
&amp;amp;amp;lt;/html&amp;amp;amp;gt;

[/php]
```


点击write之后，a标签后面出现一个超链接，链接地址就是input里面的地址，当按下button之时，test这个函数既可以触发，通过innerHTML将input里面的值写入html志宏，这就是DOM Based XSS发生的原因。
 

和XSS一样，为了融入HTML之中，我们构造：
 

' onclick = alert(/xss/) //
 

那么再输入之后，页面代码就变成了：
 

<a herf = '' onclick = alert(/xss/) //'>testLink</a>
 

首先用一个单引号闭合原来herf之后的单引号，然后插入一个onclick事件，最后使用注释符"//"注释掉第二个单引号，那么点击的时候，事件被执行…
 

![](/wp-content/uploads/2015/08/080515_1010_WebSafetyXS2.png)
 

然而遵循这种思路，我们还有另一种利用方式，通过闭合<a>标签，插入一个新的HTML标签，尝试以下输入：
 

'><img src = # onerror = alert(/xss2/) /><'
 

那么代码id = t将变成：
 

 <a herf = ''><img src = # onerror = alert(/xss2/) /><''>testLink</a>
 

 脚本被执行。
 

![](/wp-content/uploads/2015/08/080515_1010_WebSafetyXS3.png)
 

XSS 被执行。