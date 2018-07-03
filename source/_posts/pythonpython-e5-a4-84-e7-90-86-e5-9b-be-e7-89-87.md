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

[**<a href="/wp-content/uploads/2015/04/512733.jpg">![](/wp-content/uploads/2015/04/512733-1024x575.jpg "512733")](http://www.cnblogs.com/way_testlife/archive/2011/04/17/2019013.html)使用PIL库做图像处理**</a>**
**

1\. 简介。


图像处理是一门应用非常广的技术，而拥有非常丰富的第三方扩展库的 Python 当然不会错过这一门盛宴。PIL （Python Imaging Library）是 Python 中最常用的图像处理库，目前版本为 1.1.7，我们可以[在这里](http://www.pythonware.com/products/pil/index.htm)下载学习和查找资料。


Image 类是 PIL 库中一个非常重要的类，通过这个类来创建实例可以有直接载入图像文件，读取处理过的图像和通过抓取的方法得到的图像这三种方法。


2\. 使用。


    导入 Image 模块。然后通过 Image 类中的 open 方法即可载入一个图像文件。如果载入文件失败，则会引起一个 IOError ；若无返回错误，则 open 函数返回一个 Image 对象。现在，我们可以通过一些对象属性来检查文件内容，即：


1 >>> import Image
2 >>> im = Image.open("j.jpg")
3 >>> print im.format, im.size, im.mode
4 JPEG (440, 330) RGB


这里有三个属性，我们逐一了解。


format : 识别图像的源格式，如果该文件不是从文件中读取的，则被置为 None 值。


size : 返回的一个元组，有两个元素，其值为象素意义上的宽和高。


mode : RGB（true color image），此外还有，L（luminance），CMTK（pre-press image）。


现在，我们可以使用一些在 Image 类中定义的方法来操作已读取的图像实例。比如，显示最新载入的图像：


1 >>>im.show()
2 >>>


    输出原图：


![](/wp-content/uploads/2015/04/041715_1702_PythonPytho1.jpg)


3\. 函数概貌。


3.1 Reading and Writing Images : open( infilename ) , save( outfilename )


3.2 Cutting and Pasting and Merging Images :


crop() : 从图像中提取出某个矩形大小的图像。它接收一个四元素的元组作为参数，各元素为（left, upper, right, lower），坐标系统的原点（0, 0）是左上角。


paste():


merge() :


[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho2.gif)](javascript:void(0); ""复制代码"")


1 >>> box = (100, 100, 200, 200)
2 >>> region = im.crop(box)
3 >>> region.show()
4 >>> region = region.transpose(Image.ROTATE_180)
5 >>> region.show()
6 >>> im.paste(region, box)
7 >>> im.show()


[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho3.gif)](javascript:void(0); ""复制代码"")


    其效果图为：


![](/wp-content/uploads/2015/04/041715_1702_PythonPytho4.jpg)


旋转一幅图片：


[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho5.gif)](javascript:void(0); ""复制代码"")


 1
def roll(image, delta):
 2
"Roll an image sideways"
 3

 4 xsize, ysize = image.size
 5

 6 delta = delta % xsize
 7
if delta == 0: return image
 8

 9 part1 = image.crop((0, 0, delta, ysize))
10 part2 = image.crop((delta, 0, xsize, ysize))
11 image.paste(part2, (0, 0, xsize-delta, ysize))
12 image.paste(part1, (xsize-delta, 0, xsize, ysize))
13

14
return image


[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho6.gif)](javascript:void(0); ""复制代码"")


3.3几何变换。


3.3.1简单的几何变换。


[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho7.gif)](javascript:void(0); ""复制代码"")


1 >>>out = im.resize((128, 128)) #
2 >>>out = im.rotate(45)  #逆时针旋转 45 度角。
3 >>>out = im.transpose(Image.FLIP_LEFT_RIGHT) #左右对换。
4 >>>out = im.transpose(Image.FLIP_TOP_BOTTOM) #上下对换。
5 >>>out = im.transpose(Image.ROTATE_90) #旋转 90 度角。
6 >>>out = im.transpose(Image.ROTATE_180) #旋转 180 度角。
7 >>>out = im.transpose(Image.ROTATE_270) #旋转 270 度角。


[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho8.gif)](javascript:void(0); ""复制代码"")


各个调整之后的图像为：


图片1：![](/wp-content/uploads/2015/04/041715_1702_PythonPytho9.jpg)


图片2：![](/wp-content/uploads/2015/04/041715_1702_PythonPytho10.jpg)


图片3：![](/wp-content/uploads/2015/04/041715_1702_PythonPytho11.jpg)


图片4：![](/wp-content/uploads/2015/04/041715_1702_PythonPytho12.jpg)


3.3.2色彩空间变换。


convert():该函数可以用来将图像转换为不同色彩模式。


3.3.3    图像增强。


    Filters : 在 ImageFilter 模块中可以使用 filter 函数来使用模块中一系列预定义的增强滤镜。


1 >>> import ImageFilter
2 >>> imfilter = im.filter(ImageFilter.DETAIL)
3 >>> imfilter.show()


3.4 序列图像。


即我们常见到的动态图，最常见的后缀为 .gif ，另外还有 FLI / FLC 。PIL库对这种动画格式图也提供了一些基本的支持。当我们打开这类图像文件时，PIL 自动载入图像的第一帧。我们可以使用 seek 和 tell 方法在各帧之间移动。


[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho13.gif)](javascript:void(0); ""复制代码"")


1
import Image
2 im.seek(1) # skip to the second frame
3

4
try:
5
while 1:
6 im.seek( im.tell() + 1)
7
# do something to im
8
except EOFError:
9
pass


[![](/wp-content/uploads/2015/04/041715_1702_PythonPytho14.gif)](javascript:void(0); ""复制代码"")


3.5    更多关于图像文件的读取。


    最基本的方式：im = Image.open("filename")


    类文件读取：fp = open("filename", "rb"); im = Image.open(fp)


    字符串数据读取：import StringIO; im = Image.open(StringIO.StringIO(buffer))


    从归档文件读取：import TarIO; fp = TarIo.TarIO("Image.tar", "Image/test/lena.ppm"); im = Image.open(fp)
