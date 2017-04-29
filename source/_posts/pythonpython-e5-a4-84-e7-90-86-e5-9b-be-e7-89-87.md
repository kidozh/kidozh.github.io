---
title: '[Python]Python处理图片'
tags:
  - Python
  - 图像处理
id: 196
categories:
  - Python
date: 2015-04-18 01:03:02
---

[<span style="color: black; font-family: 微软雅黑;">**<a href="/wp-content/uploads/2015/04/512733.jpg">![](/wp-content/uploads/2015/04/512733-1024x575.jpg "512733")](http://www.cnblogs.com/way_testlife/archive/2011/04/17/2019013.html)使用PIL库做图像处理**</span></a><span style="color: #4b4b4b; font-family: 微软雅黑;">**
**</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">1\. 简介。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">图像处理是一门应用非常广的技术，而拥有非常丰富的第三方扩展库的 Python 当然不会错过这一门盛宴。PIL （Python Imaging Library）是 Python 中最常用的图像处理库，目前版本为 1.1.7，我们可以[<span style="color: black; text-decoration: underline;">在这里</span>](http://www.pythonware.com/products/pil/index.htm)下载学习和查找资料。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">Image 类是 PIL 库中一个非常重要的类，通过这个类来创建实例可以有直接载入图像文件，读取处理过的图像和通过抓取的方法得到的图像这三种方法。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">2\. 使用。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">    导入 Image 模块。然后通过 Image 类中的 open 方法即可载入一个图像文件。如果载入文件失败，则会引起一个 IOError ；若无返回错误，则 open 函数返回一个 Image 对象。现在，我们可以通过一些对象属性来检查文件内容，即：
</span>

<span style="color: teal; font-family: Microsoft YaHei Mono; font-size: 12pt;">1<span style="color: black;"> &gt;&gt;&gt; <span style="color: blue;">import<span style="color: black;"> Image
<span style="color: teal;">2<span style="color: black;"> &gt;&gt;&gt; im = Image.open(<span style="color: maroon;">"j.jpg"<span style="color: black;">)
<span style="color: teal;">3<span style="color: black;"> &gt;&gt;&gt; <span style="color: blue;">print<span style="color: black;"> im.format, im.size, im.mode
<span style="color: teal;">4<span style="color: black;"> JPEG (440, 330) RGB
</span></span></span></span></span></span></span></span></span></span></span></span></span></span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">这里有三个属性，我们逐一了解。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">format : 识别图像的源格式，如果该文件不是从文件中读取的，则被置为 None 值。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">size : 返回的一个元组，有两个元素，其值为象素意义上的宽和高。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">mode : RGB（true color image），此外还有，L（luminance），CMTK（pre-press image）。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">现在，我们可以使用一些在 Image 类中定义的方法来操作已读取的图像实例。比如，显示最新载入的图像：
</span>

<span style="color: teal; font-family: Microsoft YaHei Mono; font-size: 12pt;">1<span style="color: black;"> &gt;&gt;&gt;im.show()
<span style="color: teal;">2<span style="color: black;"> &gt;&gt;&gt;
</span></span></span></span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">    输出原图：
</span>

![](/wp-content/uploads/2015/04/041715_1702_PythonPytho1.jpg)<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">3\. 函数概貌。
</span>

<span style="color: #4b4b4b; font-family: Source Code Pro; font-size: 10pt;">3.1 Reading and Writing Images : open( infilename ) , save( outfilename )
</span>

<span style="color: #4b4b4b; font-family: Source Code Pro; font-size: 10pt;">3.2 Cutting and Pasting and Merging Images :
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">crop() : 从图像中提取出某个矩形大小的图像。它接收一个四元素的元组作为参数，各元素为（left, upper, right, lower），坐标系统的原点（0, 0）是左上角。
</span>

<span style="color: #4b4b4b; font-family: Source Code Pro; font-size: 10pt;">paste():
</span>

<span style="color: #4b4b4b; font-family: Source Code Pro; font-size: 10pt;">merge() :
</span>

[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho2.gif)](javascript:void(0); "&quot;复制代码&quot;")<span style="color: black; font-family: 微软雅黑; font-size: 10pt;">
</span>

<span style="color: teal; font-family: Microsoft YaHei Mono; font-size: 12pt;">1<span style="color: black;"> &gt;&gt;&gt; box = (100, 100, 200, 200)
<span style="color: teal;">2<span style="color: black;"> &gt;&gt;&gt; region = im.crop(box)
<span style="color: teal;">3<span style="color: black;"> &gt;&gt;&gt; region.show()
<span style="color: teal;">4<span style="color: black;"> &gt;&gt;&gt; region = region.transpose(Image.ROTATE_180)
<span style="color: teal;">5<span style="color: black;"> &gt;&gt;&gt; region.show()
<span style="color: teal;">6<span style="color: black;"> &gt;&gt;&gt; im.paste(region, box)
<span style="color: teal;">7<span style="color: black;"> &gt;&gt;&gt; im.show()
</span></span></span></span></span></span></span></span></span></span></span></span></span></span>

[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho3.gif)](javascript:void(0); "&quot;复制代码&quot;")<span style="color: black; font-family: 微软雅黑; font-size: 10pt;">
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">    其效果图为：
</span>

![](/wp-content/uploads/2015/04/041715_1702_PythonPytho4.jpg)<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">旋转一幅图片：
</span>

[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho5.gif)](javascript:void(0); "&quot;复制代码&quot;")<span style="color: black; font-family: 微软雅黑; font-size: 10pt;">
</span>

<span style="color: teal; font-family: Microsoft YaHei Mono; font-size: 12pt;"> 1<span style="color: black;">
<span style="color: blue;">def<span style="color: black;"> roll(image, delta):
<span style="color: teal;"> 2<span style="color: black;">
<span style="color: maroon;">"Roll an image sideways"<span style="color: black;">
<span style="color: teal;"> 3</span></span></span></span></span></span></span></span></span>

<span style="color: teal;"> 4<span style="color: black;"> xsize, ysize = image.size
<span style="color: teal;"> 5</span></span></span>

<span style="color: teal;"> 6<span style="color: black;"> delta = delta % xsize
<span style="color: teal;"> 7<span style="color: black;">
<span style="color: blue;">if<span style="color: black;"> delta == 0: <span style="color: blue;">return<span style="color: black;"> image
<span style="color: teal;"> 8</span></span></span></span></span></span></span></span></span>

<span style="color: teal;"> 9<span style="color: black;"> part1 = image.crop((0, 0, delta, ysize))
<span style="color: teal;">10<span style="color: black;"> part2 = image.crop((delta, 0, xsize, ysize))
<span style="color: teal;">11<span style="color: black;"> image.paste(part2, (0, 0, xsize-delta, ysize))
<span style="color: teal;">12<span style="color: black;"> image.paste(part1, (xsize-delta, 0, xsize, ysize))
<span style="color: teal;">13</span></span></span></span></span></span></span></span></span>

<span style="color: teal;">14<span style="color: black;">
<span style="color: blue;">return<span style="color: black;"> image
</span></span></span></span>

[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho6.gif)](javascript:void(0); "&quot;复制代码&quot;")<span style="color: black; font-family: 微软雅黑; font-size: 10pt;">
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">3.3几何变换。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">3.3.1简单的几何变换。
</span>

[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho7.gif)](javascript:void(0); "&quot;复制代码&quot;")<span style="color: black; font-family: 微软雅黑; font-size: 10pt;">
</span>

<span style="color: teal; font-family: Microsoft YaHei Mono; font-size: 12pt;">1<span style="color: black;"> &gt;&gt;&gt;out = im.resize((128, 128)) <span style="color: green;">#
<span style="color: teal;">2<span style="color: black;"> &gt;&gt;&gt;out = im.rotate(45) <span style="color: green;"> #逆时针旋转 45 度角。
<span style="color: teal;">3<span style="color: black;"> &gt;&gt;&gt;out = im.transpose(Image.FLIP_LEFT_RIGHT) <span style="color: green;">#左右对换。
<span style="color: teal;">4<span style="color: black;"> &gt;&gt;&gt;out = im.transpose(Image.FLIP_TOP_BOTTOM) <span style="color: green;">#上下对换。
<span style="color: teal;">5<span style="color: black;"> &gt;&gt;&gt;out = im.transpose(Image.ROTATE_90) <span style="color: green;">#旋转 90 度角。
<span style="color: teal;">6<span style="color: black;"> &gt;&gt;&gt;out = im.transpose(Image.ROTATE_180) <span style="color: green;">#旋转 180 度角。
<span style="color: teal;">7<span style="color: black;"> &gt;&gt;&gt;out = im.transpose(Image.ROTATE_270) <span style="color: green;">#旋转 270 度角。<span style="color: black;">
</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>

[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho8.gif)](javascript:void(0); "&quot;复制代码&quot;")<span style="color: black; font-family: 微软雅黑; font-size: 10pt;">
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">各个调整之后的图像为：
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">图片1：![](/wp-content/uploads/2015/04/041715_1702_PythonPytho9.jpg)
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">图片2：![](/wp-content/uploads/2015/04/041715_1702_PythonPytho10.jpg)
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">图片3：![](/wp-content/uploads/2015/04/041715_1702_PythonPytho11.jpg)
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">图片4：![](/wp-content/uploads/2015/04/041715_1702_PythonPytho12.jpg)
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">3.3.2色彩空间变换。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">convert():该函数可以用来将图像转换为不同色彩模式。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">3.3.3    图像增强。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">    Filters : 在 ImageFilter 模块中可以使用 filter 函数来使用模块中一系列预定义的增强滤镜。
</span>

<span style="color: teal; font-family: Microsoft YaHei Mono; font-size: 12pt;">1<span style="color: black;"> &gt;&gt;&gt; <span style="color: blue;">import<span style="color: black;"> ImageFilter
<span style="color: teal;">2<span style="color: black;"> &gt;&gt;&gt; imfilter = im.filter(ImageFilter.DETAIL)
<span style="color: teal;">3<span style="color: black;"> &gt;&gt;&gt; imfilter.show()
</span></span></span></span></span></span></span></span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">3.4 序列图像。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">即我们常见到的动态图，最常见的后缀为 .gif ，另外还有 FLI / FLC 。PIL库对这种动画格式图也提供了一些基本的支持。当我们打开这类图像文件时，PIL 自动载入图像的第一帧。我们可以使用 seek 和 tell 方法在各帧之间移动。
</span>

[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho13.gif)](javascript:void(0); "&quot;复制代码&quot;")<span style="color: black; font-family: 微软雅黑; font-size: 10pt;">
</span>

<span style="color: teal; font-family: Microsoft YaHei Mono; font-size: 12pt;">1<span style="color: black;">
<span style="color: blue;">import<span style="color: black;"> Image
<span style="color: teal;">2<span style="color: black;"> im.seek(1) <span style="color: green;"># skip to the second frame
<span style="color: teal;">3</span></span></span></span></span></span></span></span>

<span style="color: teal;">4<span style="color: black;">
<span style="color: blue;">try<span style="color: black;">:
<span style="color: teal;">5<span style="color: black;">
<span style="color: blue;">while<span style="color: black;"> 1:
<span style="color: teal;">6<span style="color: black;"> im.seek( im.tell() + 1)
<span style="color: teal;">7<span style="color: black;">
<span style="color: green;"># do something to im
<span style="color: teal;">8<span style="color: black;">
<span style="color: blue;">except<span style="color: black;"> EOFError:
<span style="color: teal;">9<span style="color: black;">
<span style="color: blue;">pass<span style="color: black;">
</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>

[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho14.gif)](javascript:void(0); "&quot;复制代码&quot;")<span style="color: black; font-family: 微软雅黑; font-size: 10pt;">
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">3.5    更多关于图像文件的读取。
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">    最基本的方式：im = Image.open("filename")
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">    类文件读取：fp = open("filename", "rb"); im = Image.open(fp)
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">    字符串数据读取：import StringIO; im = Image.open(StringIO.StringIO(buffer))
</span>

<span style="color: #4b4b4b; font-family: 微软雅黑; font-size: 10pt;">    从归档文件读取：import TarIO; fp = TarIo.TarIO("Image.tar", "Image/test/lena.ppm"); im = Image.open(fp)
</span>