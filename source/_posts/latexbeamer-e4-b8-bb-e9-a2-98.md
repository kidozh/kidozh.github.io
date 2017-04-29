---
title: '[LaTeX]beamer主题'
tags:
  - beamer
  - LaTeX
id: 752
categories:
  - LaTeX
date: 2015-12-22 17:24:09
---

# 1 简介

在前面的代码中出现了<span class="lang:tex decode:true  crayon-inline ">\usetheme{AnnArbor}</span> ，他是beamer提供的演示主题调用命令，AnnArbor就是主题中的一种，如果这个被改成Hannover，主题将发生巨大变化。

# 2 类别

其主要分为外部主题、内部主题、颜色主题、字体主题和演示主题；而且每类主题又具有多种样式，调用主题的命令就相当于调用命令<span class="lang:tex decode:true  crayon-inline ">\usepackage</span> 。

## 2.1 外部主题

幻灯文类定义了许多的外部主题，一种外部主题就是一种幻灯片的基本外观样式，其可以使用命令
<pre class="lang:tex decode:true">\useoutertheme[pattern]{outertheme}</pre>

 其中外部主题的名称和功能说明如下：

*   default 只有符号条，是最基本的配置，帧标题左对齐，徽标的位置在每幅幻灯片的右下角
*   infolines 添加顶边导航条，并且中分两段，左侧显示当前节标题，右端显示当前小节标题，增添导航条，等分为三段，从左至右分别是作者姓名和院校名称，论文题名简称，日期和帧码
*   miniframes 添加定边导航条，分为三层，上层显示所有节标题，中层用若干小圆圈表示该节中帧数目，下层显示当前小节标题。该主题的样式具有三种常用选项：1.footline=authorinstitute，增添底边导航条，显示作者姓名和院校名称，2.footline=authortitle，<span style="line-height: 22.8571px;">增添底边导航条，显示</span><span style="line-height: 22.8571px;">论文题名简称和作者姓名，3.footline=institutetitle，</span><span style="line-height: 22.8571px;">增添底边导航条，显示</span><span style="line-height: 22.8571px;">论文题名简称和院校名称。4.subsection=false，取消再定边导航条中显示当前小节标题</span>
*   split 增设顶边导航条，中分两段，左侧显示节标题，每个节标题占一行，右侧显示当前节中个小节标题，每个小节标题各占一行，例如使用beamer的compress选项，将左侧各标题和右端各小节标题压缩至一行，添加底边导航栏，中分两段，左端显示作者姓名，右端显示题名简称
*   shadow 该主题是split的扩展，出了具有与spilt相同的功能外，还能在定边导航栏或者帧标题底部添加阴影，产生立体感
*   sidebar 增加左侧导航条，自上而下显示题名简称、作者姓名、节标题一级小节标题，<span class="lang:tex decode:true  crayon-inline ">\section*</span> 和<span class="lang:tex decode:true  crayon-inline" style="font-size: 14px;">\subsection*</span><span style="line-height: 22.8571px;"> 标题也在导航栏中显示，但是目录中不予显示，徽标位置设定在每幅导航栏的左上角，其具有以下选项：1.height=高度 weight=宽度 设置帧标题条的高度和宽度，高度默认值是字体行高的2.5倍，足以排版两行帧标题或者一行帧副题，宽度默认为字体行高的2.5被，若设定0pt，则侧边导航条消失；2.hideothersubsections  在侧边导航条之中，除节标题外仅显示当前小节标题，其他小节标题不予显示。3.hideallsubsections 仅显示节标题，所有小节标题都不再显示 4\. right 将导航条置于右侧 </span>
*   smoothbars 与miniframes主题功能基本相同，不同之处在于导航条背景与帧背景色过渡的较为平滑，其仅有一个参数：subsection=false 取消顶边导航条中显示当前小节标题
*   tree 添加顶边导航栏，中分三行，上行显示题名简称，中行显示当前节标题，下行显示当前小节标题，两行之间使用树形指引线连接
*   smoothtree 与tree类似，但是没有树形指引线，其次就是每种背景色之间具有一段平滑的过渡

## 2.2 内部主题

也就是设定多种幻灯片的内部主题以及内部细节，其使用命令：

<span class="lang:tex decode:true  crayon-inline ">\useinnertheme[pattern]{innertheme}</span> 

其内部主题名称以及功能有：

*   default 默认值，其定义了论文题名、作者姓名、各种列表、插图以及表格标题、各种模块、摘要、脚注以及参考文献等文本元素的样式
*   circles 将itemize item中的小三角改为小圆盘，排序列表enumerate items添加背景小圆盘，目录中每个条目前加一个小圆盘
*   rectangle <span style="line-height: 22.8571px;">将itemize item中的小三角改为小方块，排序列表enumerate items添加背景小方块，目录中每个条目前加一个小方块</span>
*   rounded <span style="line-height: 22.8571px;">将itemize item中的小三角改为小圆，排序列表enumerate items添加背景小圆，目录中每个条目前加一个小圆，题名和各种模块的背景框由直角变更为圆弧，其有下列参数：shadow 给各种木块添加阴影，以满足立体感。</span>

## 2.3 颜色主题

幻灯片文类域定义了多种幻灯片的颜色主题，一种颜色主题就是一种幻灯片的基本色调，调用某种颜色命令可以使用命令：
<pre class="lang:tex decode:true">\usecolortheme[pattern]{colorTheme}</pre>

 其中颜色主题的名称以及其功能说明如下：

*   <span style="line-height: 1.42857;">default 默认值，其定义了论文题名、作者姓名、各种列表、插图和表格标题、各种模块、摘要、脚注和参考文献等文本元素的前景和背景颜色。其中常规文本白底黑字，实例模块的标题字体是暗绿色，论文名、节标题和帧标题的字体均是暗蓝色。</span>
*   albatross 主背景、各种导航条和各种模块的背景均为深蓝色或者青色，常规文本字体改成了金黄色，每幅幻灯片以深蓝色和金黄色作为主色调。当论文陈述环境的光线较暗时候，这种深色调不利于观看，该主题也只有一种可选项：overlystylish：每幅幻灯片的中部都有背景色
*   beaver 顶边导航栏和底边导航栏变为暗红色、灰色和浅灰色，字体变更为白色和暗红色，帧标题的北京为浅灰色，字体为暗红色；左侧导航条背景为浅灰色
*   beetle 常规文本为黑色，背景为灰色；题名、帧标题和节标题为白色；定边、底边和左侧导航条背景色为深蓝和青色。主色调为**黑白灰**。
*   crane 证明等木块的标题北京为橙色，文本背景为黄色，实力木块的标题背景为绿色，文本背景为浅绿；顶边和底边导航栏的背景为橙色或者黄色
*   dolphin 将顶边和底边导航条的背景换成深蓝、蓝和浅蓝色
*   dove 常规字体、顶边和底边导航条均为白底黑字；适合黑白打印
*   fly 常规文本灰底黑字；顶边和底边导航条背景色均为灰色，左侧导航条的背景为深灰色；论文标题、帧标题和节标题均为灰底白字
*   lily 取消其他颜色对各种模块背景色的设置，恢复为白色
*   orchid 定理类模块标题背景为深蓝色，文本背景为浅蓝色，示例模块的标题北京为深绿，文本背景为浅绿色
*   rose <span style="line-height: 22.8571px;">定理类模块标题背景为浅蓝，文本背景为浅蓝色，示例模块的标题北京为浅绿，文本背景为浅淡绿</span>
*   seagull 所有模块的标题均为浅灰色，背景为灰色；左侧、顶边、底边导航栏中的字体为黑色，背景为深灰色、灰色和浅灰色
*   seahorse 将论文标题、帧标题、顶边和底边导航栏等背景变更为浅蓝色或者浅淡蓝色
*   structure 在样式这个可选参数使用任意选项指定颜色，可将论文题名、帧标题、节标题和侧边导航栏等的字体颜色以及符号条的颜色改为所指定的颜色。named=颜色名，颜色名必须在xcolor宏包中定义的颜色名，例如<span class="lang:tex decode:true  crayon-inline ">\usecolortheme[named=yellow]{structure}</span> 就可以将主题色调设定为黄色。当RGB=三原色值时候，就可以把颜色指定为所选的RGB值，例如<span class="lang:tex decode:true  crayon-inline ">\usecolortheme[RGB={128,0,0}]{structure}</span> 就可以设定为暗红色了。
*   whale 顶边和底边导航栏的字体改为白色，背景换为黑色、深蓝和蓝色
*   wolverine 论文题名和帧标题背景变更为金黄色，左侧导航条背景为橘红色

beamer中，每幅幻灯片的背景由两层组成，下层是background canvas主背景层，上层则是background次背景层，而所有文本元素都在这两层的上。主背景层提供主背景色，次背景层则用于设置栅格或者背景图案。在有侧边导航条的幻灯片之中，侧边导航条具有自己的背景层sidebar canvas

## 2.4 字体主题

幻灯文类同样预定义了许多的字体元素，其中一种字体主题就是一种幻灯片的字体样式，其设定了幻灯片中标题、数学式等文本元素和导航条之中的字体属性。调用某种字体主题可以使用命令：
<pre class="lang:tex decode:true">\usefonttheme[pattern][fontTheme]</pre>

其中字体主题的名称和功能如下：

*   default 各种标题和文本字体均为等线体，数学式中的字体为等斜线体
*   serif 各种标题和字体均改为直立罗马体，该主题的样式可选参数有：1\. stillsansserifmath 指定数学式中的字体仍为斜等线体，2\. stillsansserifsmall 侧边、顶边和底边导航栏中字体仍为等线体。<span style="line-height: 22.8571px;">3\. stillsansseriflarge 各种标题的字体仍用等线体。 4. </span><span style="line-height: 22.8571px;">stillsansseriftext 所有常规文本字体仍为等线体 5\. onlymath 只有数学式中的字体改为斜罗马体</span>
*   structurebold 各种标题的字体和各种导航栏的字体变更为粗体，该主题的可选样式有：1\. onlysmall 只把各种导航条中的字体改为粗体 2\. 只把各种标题的字体改为粗体
*   <span style="line-height: 22.8571px;">structureitalicserif 各种标题的字体和各种导航条中的字体改为斜罗马体。该主题样式的可选参数具有下列参数：1\. onlysmall 只将各种导航条中的字体变更为斜罗马体 2. </span><span style="line-height: 22.8571px;">onlylarge 只将各种标题中的字体变更为斜罗马体</span>
*   <span style="line-height: 22.8571px;">structuresmallcapsserif 各种标题的字体和各种导航条中的字体变更为小型大写字体。该主题的可选参数具有以下选项：</span><span style="line-height: 22.8571px;">1\. onlysmall 只将各种导航条中的字体变更为<span style="line-height: 22.8571px;">小型大写字体</span> 2. </span><span style="line-height: 22.8571px;">onlylarge 只将各种标题中的字体变更为</span><span style="line-height: 22.8571px;">小型大写字体</span>

字体主题命令无法变更字体的默认字族。_若需要，则须另行调用相关的字体宏包，例如arev、bookman、helvet、mathptmx和times等或者定义系统的默认字族。_

## 2.5 演示主题

幻灯文类预定义了多种演示主题，其详细定义了幻灯片之中的所有细节，主要是上述四种主题的不同组合。可以使用命令：
<pre class="lang:tex decode:true">\usetheme[pattern]{displayTheme}</pre>

其中演示主题的名称以及功能可以按照**导航条的有无**分述如图：

### 2.5.1 无导航条

<span style="line-height: 1.42857;">default 默认值，只附带符号条，常规文本白底黑字，论文题名、帧标题和节标题等为白底蓝字，实际上该主题由以下四个主题组合而成。</span>
<pre class="lang:tex decode:true">\useoutertheme{default}
\useinnertheme{default}
\usecolortheme{default}
\usefonttheme{default}</pre>

Pittsburgh 只有符号条，帧标题由默认的左对齐改成右对齐

Rochester 只有符号条，帧标题蓝底白字，左对齐。该主题的样式只有一个选项：height=高度 设定帧标题条高度

### 2.5.2 侧边导航条

*   <span style="line-height: 1.42857;">Berkeley 带有左侧导航条和符号条。左侧导航条蓝底白字，从上至下显示题名简称、作者姓名、节和小节标题</span>
*   <span style="line-height: 22.8571px;">Goettingen 带有右侧导航条和符号条。左侧导航条浅蓝底黑字，从上至下显示题名简称、作者姓名、节和小节标题</span>
*   <span style="line-height: 22.8571px;">Hannover 带有左侧导航条和符号条。左侧导航条浅蓝底白字，从上至下显示题名简称、作者姓名、节和小节标题</span>
*   Marburg <span style="line-height: 22.8571px;">带有右侧导航条和符号条。左侧导航条深蓝底白字，从上至下显示题名简称、作者姓名、节和小节标题</span>
*   <span style="line-height: 22.8571px;">PaloAlto 带有左侧导航条和符号条。左侧导航条蓝底白字，从上至下显示题名简称、作者姓名、节和小节标题</span>

### 2.5.3 顶边导航栏

*   Antibes 带有顶边导航栏和符号条。顶边导航栏显示带有指引线的树形章节目录，字体为白色，背景为青色
*   JuanLesPins <span style="line-height: 22.8571px;">带有顶边导航栏和符号条。顶边导航栏显示树形章节目录，字体为白色，背景为青色</span>
*   Montepellier <span style="line-height: 22.8571px;">带有顶边导航栏和符号条。顶边导航栏有上下两条蓝色装饰线，中间白底黑字，显示带有指引线的树形章节目录</span>
*   Singapore <span style="line-height: 22.8571px;">带有顶边导航栏和符号条。顶边导航栏显示节标题，每一帧用一个圆点表示，浅蓝底色深蓝字体</span>
*   Darmstadt <span style="line-height: 22.8571px;">带有顶边导航栏和符号条。顶边导航栏黑底白字，显示节和小节标题</span>

### 2.5.4 底边导航栏

*   Boadilla 只有底边导航栏和符号条。底边导航栏等分为三段，左端显示作者姓名和院校名称，深蓝底白字；终端显示题名简称，蓝底白字；右端显示日期和帧码，浅蓝底黑字。该主题样式的可选参数只有一个选项：secheader 增加顶边导航条，中分两段，左端深蓝底白字，显示当前节标题，右端蓝底黑字，显示小节标题
*   Madrid <span style="line-height: 22.8571px;">只有底边导航栏和符号条。底边导航栏等分为三段，左端显示作者姓名和院校名称，黑底白字；终端显示题名简称，深蓝底白字；右端显示日期和帧码，蓝底白字。</span>

### 2.5.5 顶边和底边导航栏

*   AnnArbor 带有顶边、底边导航栏和符号条。顶边导航栏中分两段，左端显示节标题，字体为橘红色，背景为青色；右端显示小节标题，字体为黑色，背景为橘黄色。底边导航栏等分三段，左端显示作者姓名和院校名称，字体为橘红色，背景为深蓝色；中端显示题名简称，字体为青色，背景为橘黄色；右端显示日期和帧码，字体为黑色，背景为黄色
*   CambridgeUS <span style="line-height: 22.8571px;">带有顶边、底边导航栏和符号条。顶边导航栏中分两段，左端显示节标题，褐底白字；右端显示小节标题，灰底褐字。底边导航栏等分三段，左端显示作者姓名和院校名称，<span style="line-height: 22.8571px;">褐底白字</span>；中端显示题名简称，浅灰色褐字；右端显示日期和帧码，灰底褐字</span>
*   Copenhagen <span style="line-height: 22.8571px;">带有顶边、底边导航栏和符号条。顶边导航栏中分两段，左端显示节标题，黑底白字；右端显示小节标题，蓝底白字。底边导航栏等分两段，左端显示作者姓名，</span><span style="line-height: 22.8571px;">黑底白字</span><span style="line-height: 22.8571px;">；右中端显示题名简称，蓝底白字</span>
*   Warsaw 与Copenhagen类似，但是在题名、帧标题和各种模块的背景框外侧添加阴影，产生立体感

徽标的有无和其位置的高低，与所选演示主题和外部主题有关。可使用命令<span class="lang:tex decode:true  crayon-inline ">\insertlogo{logo}</span> 在当前位置插入徽标

演示主题与颜色主题的各种组合所生成的各种幻灯片样式可以查阅网页：

[http://deic.uab.es/~iblanes/beamer_gallery/](http://deic.uab.es/~iblanes/beamer_gallery/ "uab")

[https://www.hartwork.org/beamer-theme-matrix/](https://www.hartwork.org/beamer-theme-matrix/ "Hartwork")

目前在国内都可以自由访问。