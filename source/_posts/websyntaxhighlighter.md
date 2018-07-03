---
title: '[Web]SyntaxHighlighter'
tags:
  - 网页，代码
id: 33
categories:
  - 网页
date: 2015-03-27 17:01:53
---

我的博客中使用了WordPress的插件 [SyntaxHighlighter](http://alexgorbatchev.com/SyntaxHighlighter/) 这是一个代码高亮、模式化的工具，能让你的代码在网页上以类似IDE编辑器里的样子高亮关键字。功能挺强的，支持的语言很多，我列在下面了。在文章的最后，我将SyntaxHighlighter自带帮助文档列了出来，并稍微翻译了一下。
具体用法：


1.  在代码前根据代码语言的不同加上不同的[%Lang]在代码后加上[/%Lang]，%Lang = 你用的语言对应的Brush aliases（具体对应罗列于下）。例如**[@cpp]#include <stdio.h>[/cpp]**（@去掉）。
2.  或者只用一次%Lang，[@code lang=%Lang]你的代码[/code]或者[@source lang=%Lang]你的代码[@source lang=%Lang]，其中lang都可以换成language。


<table width="90%">
<thead>
<tr>
<th>Brush name</th>
<th>Brush aliases</th>
<th>File name</th>
</tr>
</thead>
<tbody>
<tr>
<td>[ActionScript3](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/actionscript3.html)</td>
<td>as3, actionscript3</td>
<td>shBrushAS3.js</td>
</tr>
<tr>
<td>[Bash/shell](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/bash.html)</td>
<td>bash, shell</td>
<td>shBrushBash.js</td>
</tr>
<tr>
<td>[ColdFusion](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/coldfusion.html)</td>
<td>cf, coldfusion</td>
<td>shBrushColdFusion.js</td>
</tr>
<tr>
<td>[C#](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/csharp.html)</td>
<td>c-sharp, csharp</td>
<td>shBrushCSharp.js</td>
</tr>
<tr>
<td>[C++](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/cpp.html)</td>
<td>cpp, c</td>
<td>shBrushCpp.js</td>
</tr>
<tr>
<td>[CSS](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/css.html)</td>
<td>css</td>
<td>shBrushCss.js</td>
</tr>
<tr>
<td>[Delphi](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/delphi.html)</td>
<td>delphi, pas, pascal</td>
<td>shBrushDelphi.js</td>
</tr>
<tr>
<td>[Diff](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/diff.html)</td>
<td>diff, patch</td>
<td>shBrushDiff.js</td>
</tr>
<tr>
<td>[Erlang](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/erlang.html)</td>
<td>erl, erlang</td>
<td>shBrushErlang.js</td>
</tr>
<tr>
<td>[Groovy](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/groovy.html)</td>
<td>groovy</td>
<td>shBrushGroovy.js</td>
</tr>
<tr>
<td>[JavaScript](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/javascript.html)</td>
<td>js, jscript, javascript</td>
<td>shBrushJScript.js</td>
</tr>
<tr>
<td>[Java](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/java.html)</td>
<td>java</td>
<td>shBrushJava.js</td>
</tr>
<tr>
<td>[JavaFX](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/javafx.html)</td>
<td>jfx, javafx</td>
<td>shBrushJavaFX.js</td>
</tr>
<tr>
<td>[Perl](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/perl.html)</td>
<td>perl, pl</td>
<td>shBrushPerl.js</td>
</tr>
<tr>
<td>[PHP](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/php.html)</td>
<td>php</td>
<td>shBrushPhp.js</td>
</tr>
<tr>
<td>[Plain Text](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/plain.html)</td>
<td>plain, text</td>
<td>shBrushPlain.js</td>
</tr>
<tr>
<td>[PowerShell](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/powershell.html)</td>
<td>ps, powershell</td>
<td>shBrushPowerShell.js</td>
</tr>
<tr>
<td>[Python](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/python.html)</td>
<td>py, python</td>
<td>shBrushPython.js</td>
</tr>
<tr>
<td>[Ruby](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/ruby.html)</td>
<td>rails, ror, ruby</td>
<td>shBrushRuby.js</td>
</tr>
<tr>
<td>[Scala](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/scala.html)</td>
<td>scala</td>
<td>shBrushScala.js</td>
</tr>
<tr>
<td>[SQL](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/sql.html)</td>
<td>sql</td>
<td>shBrushSql.js</td>
</tr>
<tr>
<td>[Visual Basic](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/vb.html)</td>
<td>vb, vbnet</td>
<td>shBrushVb.js</td>
</tr>
<tr>
<td>[XML](http://alexgorbatchev.com/SyntaxHighlighter/manual/brushes/xml.html)</td>
<td>xml, xhtml, xslt, html, xhtml</td>
<td>shBrushXml.js</td>
</tr>
</tbody>
</table>



简码参数

这些参数你能够设置在简码中。对于布尔值（即 on/off），使用 true/1 或者 false/0。

lang or language — The language syntax to highlight with. You can alternately just use that as the tag, such as [@php]code[/php]. （代码语言）
autolinks — Toggle automatic URL linking.（将URL自动转换成链接）
classname — Add an additional CSS class to the code box.（加载额外CSS控制）
collapse — Toggle collapsing the code box by default, requiring a click to expand it. Good for large code posts.（收缩代码框，对于大量代码很有用）
firstline — An interger specifying what number the first line should be (for the line numbering).（首行号）
gutter — Toggle the left-side line numbering.（是否显示左侧行号）
highlight — A comma-sperated list of line numbers to highlight. You can also specify a range. Example: 2,5-10,12（高亮行号）
htmlscript — Toggle highlighting any extra HTML/XML. Good for when you're mixing HTML/XML with another language, such as having PHP inside an HTML web page. The above preview has it enabled for example. This only works with certain languages.（在HTML中插入PHP经常使用这种方法）
light — Toggle light mode which disables the gutter and toolbar all at once.（不显示行号和工具条）
padlinenumbers — Controls line number padding. Valid values are false (no padding), true (automatic padding), or an integer (forced padding).（控制行号行间距）
title (v3 only) — Sets some text to show up before the code. Very useful when combined with the collapse parameter.
toolbar — Toggle the toolbar (buttons in v2, the about question mark in v3)（标题，显示在代码前）
wraplines (v2 only) — Toggle line wrapping.（自动换行）
一些简码示例

[php]这里写你的代码[/php]
[css autolinks="false" classname="myclass" collapse="false" firstline="1" gutter="true" highlight="1-3,6,9" htmlscript="false" light="false" padlinenumbers="false" smarttabs="true" tabsize="4" toolbar="true" title="example-filename.php"]这里写你的代码[/css]


