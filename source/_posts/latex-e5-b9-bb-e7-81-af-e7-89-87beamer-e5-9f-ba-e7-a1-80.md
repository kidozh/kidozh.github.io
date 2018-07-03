---
title: '[LaTeX]幻灯片beamer基础'
tags:
  - beamer
  - LaTeX
id: 742
categories:
  - LaTeX
date: 2015-12-21 16:42:23
---

# 1.简述

学术论文答辩或者学术会议上通常有5-20分钟的论文陈述，为了在这么短的时间内迅速准确的了解主要内容和研究成果，在论述过程中使用幻灯片的是非常直接的。

采用$$\LaTeX\$$制作幻灯片主要有以下好处：

*   其使用的是PDF格式，可以不受操作系统和应用软件的限制，在任何计算机上都能使用
*   $$\LaTeX\$$优秀的数学排版功能，可以把论文中各种复杂的数学式直接搬到幻灯片之中

其中较为常见的就是beamer幻灯文类了，其具有以下特点：

1.  幻灯片的源文件可以使用PDFLaTeX、XeLaTeX或者LuaLaTeX编译直接生成PDF格式，也可以使用LaTeX->dvi2ps->ps2pdf的编译方法，任何计算机上都有阅读PDF的阅读器（实在不行还有浏览器），所以放映问题基本是不愁的。
2.  绝大部分的$$\LaTeX\$$命令仍然具有效力，例如章节目录还是可以用\tableofcontents 生成，itemize环境创建常规列表，\section 和\subsection 的层次结构
3.  提供了大量的多种类型的主题样式，可以方便的更改幻灯片的整体风格，或者对某一局部的样式、字体和颜色等细节进行修改
4.  具有多种动画功能，易于调整和使用，可以形象生动的掩饰各种过程的分解动作，有利于加深理解

# 2 基本结构

其源文件分为导言和正文两个部分，大部分的$$\LaTeX\$$命令和环境都可以照搬到beamer中，由于幻灯片的特殊性，beamer也提供了大量的专有命令和环境，便于对幻灯片中的各种细节进行修饰。

使用文档命令\documentclass 调用beamer.cls幻灯片文件的时候，amsfont、amsmath、amssymb、amsthm、enumerate、geometry、graphics、graphicx、hyperref、ifpdf、keyval、xcolor、xxcolor和url等多个相关用途的宏包也被自动加载，所以在制作幻灯片的时候不必重复调用这些包，以免发生冲突。

例如下面这个beamer示例。
```tex
\documentclass[14pt,hyperref={CJKbookmarks=true}]{beamer}
\usepackage[space,noindent]{ctex}
\usetheme{AnnArbor}
\setbeamercolor{normal text}{bg=black!10}
\begin{document}
\kaishu
\title[题名简称]{论文题名}
\subtitle{论文副题}
\author{作者姓名}
\institute[院系简称]{院系全称}
\date[会议简称 2010]{会议全称，2010}
\logo{\includegraphics{TeXlogo.pdf}}
\begin{frame}
\titlepage
\end{frame}
\section{概述}
\subsection{基本理论}
\begin{frame}
\frametitle{帧标题}
\framesubtitle{帧副题}
基本理论的要点 1、2、3...
\end{frame}
...
\section{研究方法}
\begin{frame}
研究和实验方法简介...
\end{frame}
\subsection{主要论点和依据}
...
\section{总结}
\subsection{研究意义与创新点}
\begin{frame}
...
\end{frame}
\end{document}

```


 [PDF文件](/wp-content/uploads/2015/12/13-1.pdf)

首先我们针对这个简要的解释一下生成的文件

1.  由于$$\LaTeX\$$的自动排版，其生成了5帧幻灯片，每篇幻灯片右下角显示的是帧码，例如1/5指的就是当前显示的是第1帧，本幻灯片一共有5帧
2.  每一帧幻灯片顶部都有一个导航条，除了第一篇题名外，每幅定边导航条都显示节标题和小节标题
3.  同样的，在底部也有一个导航条，分别显示的是作者姓名，院系简称、题名简称、回忆简称和编码
4.  右上方的徽标可以用\logo 命令引入插图
5.  幻灯文类分别给题名信息命令\author 、\date 、\title 添加了一个可选参数

## 2.1 选项

幻灯文类的第一条命令就是文档类型命令：
```tex
\documentclass[args1,args2,...]{beamer}
```


 这些参数主要有以下几类：

1.  字体尺寸。默认为11pt，这里bigger这个参数是指的12pt，smaller指的是10pt
2.  字体。文本字体默认为sans（是等线字体），数字字体默认为mathsans（斜等线体），serif（文本字体是罗马体，数字字体是斜罗马体mathserif）
3.  对齐 主要分为c（垂直居中）和t（顶对齐）
4.  色调：

*   blackandwhite 黑色或者浅灰色
*   blue 深蓝色或者浅蓝色
*   brown 棕色或者浅棕色
*   red 红色或者暗红色
*   xcolor= beamer会自动调用xcolor的颜色宏包当时用dvipsnames、svgnames、x11names以下选项就可以使用更多的颜色了

同时也应该注意一下情况envcountsect（以节为排序单位）、fleqn（左缩进对齐）、leqno（行间公式序号改为左侧）、noamsthm（取消自动加载amsthm和amsmath宏包）、notheorems（关闭beamer定义的定理类环境，例如theorem、example，但是仍然加载定理宏包amsthm）

当然还有一些关系到显示的设定：

1.  aspectratio 每幅幻灯片的宽高比，默认值为43，也就是宽高比为4：3，如果需要使用16：9，可以采用169
2.  draft 各种导航条使用灰色长方条取代，插图使用方框替代，符号条也被取消，这样主要用于调试
3.  handout 取消符号条和叠层动画效果，以便于全文打印
4.  trans 用于制作透明幻灯片
5.  hyperref 增加或者取消某项设置，例如节或者小节标题含有中文之时就必须增加设置\hyperref={CJKbookmarks=true} 
6.  compress 尽可能压缩导航条中的内容
7.  table 在编排彩色表格时候使用行颜色命令\rowcolors

beamer可选参数有CJK中文选项，但是他和中文字体宏包ctex的有关设置**冲突**，所以无法使用。

## 2.2 帧环境

幻灯片的源文件主要由一些列的帧环境frame组成的，出了题名命令、节和小节以及其他设置命令，幻灯片中节和小节的内容必须置于帧环境之中。帧环境的命令结构为：
```tex
\begin{frame}
\frametitle{帧标题}
\framesubtitle{帧副题}
基本理论的要点 1、2、3...
\end{frame}
```


 其中就可选参数如下：

*   allowdisplaybreaks 允许多行公式的中间换幅，这个命令必须与allowframebreaks一起使用
*   allowframebreaks 允许帧环境的自动换幅，可以根据内容多出来的情况自动增加若干个帧环境
*   b 底对齐
*   c 默认值，垂直居中，帧环境的t、c优先于beamer中的t、c
*   t 顶对齐
*   fragile 不能按照通常的意义来编译，例如在使用verbatim抄录环境中就需要添加此项
*   label=标签名 为这个帧设定名称，作为跳转或者重复命令识别的目标
*   plain 取消各种导航条和徽标
*   squeeze 压缩文本行之间的间距
*   shrink 当内容超出一副幻灯片所能显示的范围时，自动缩小帧环境中所有内容的字体尺寸，并且压缩行距，是的帧环境中所有内容都被启用