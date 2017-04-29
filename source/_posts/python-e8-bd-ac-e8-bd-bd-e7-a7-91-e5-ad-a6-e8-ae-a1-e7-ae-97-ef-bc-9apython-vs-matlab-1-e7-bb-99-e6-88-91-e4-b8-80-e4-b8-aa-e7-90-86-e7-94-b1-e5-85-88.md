---
title: '[Python][转载] 科学计算：Python VS. MATLAB (1)----给我一个理由先'
tags:
  - MATLAB
  - Python
id: 329
categories:
  - Python
date: 2015-05-03 14:31:14
---

 

<span style="font-family:Microsoft YaHei UI; font-size:14pt">MATLAB 是一种用于算法开发、数据可视化、数据分析以及数值计算的高级技术计算语言和交互式环境。使用 MATLAB，您可以较使用传统的编程语言（如 C、C++ 和 Fortran）更快地解决技术计算问题。（官网：[http://www.mathworks.com/matlabcentral/linkexchange/links/1573-matlab-科学计算语言](http://www.mathworks.com/matlabcentral/linkexchange/links/1573-matlab-%E7%A7%91%E5%AD%A6%E8%AE%A1%E7%AE%97%E8%AF%AD%E8%A8%80)）
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">        随着MATLAB工具箱的不断添加和完善，M语言也逐渐成为工程界的准通用标准语言，官网称：MATLAB - The Language Of Technical Computing。大学理工科专业一般都开设了或选修或必修的MATLAB相关课程。很多新出版的教材，计算机辅助教学的工具软件开始选用MATLAB。MATLAB以其简洁易学的语法、友好的界面和完善的文档系统逐渐深入人心并将继续扩大它的控制领地。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">        然而，MATLAB也有着很大的局限性。**首先，是价格。**作为一款商业软件，获得正版授权，价格不菲。就说最便宜的学生版，核心组件单个授权要花99刀，想使用额外工具箱，则是每个工具箱29刀。（[http://www.mathworks.com/store/platformReleaseStuSubmit.do](http://www.mathworks.com/store/platformReleaseStuSubmit.do)） 正如你能想到的，商业版本更贵。**其次，是版权。**mathworks论坛活跃着很多用户，也有很多有价值的代码，但是，版权归mathworks公司，要想使用必须获得它的授权。**再次，是语言完善性。**MATLAB进行数学计算的表现无可置疑，但是实际的科学计算还有文件操作、界面设计等任务。MATLAB在这些领域功能较弱或者很麻烦。应该可以说，MATLAB不是一种完善的语言。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">        穷则思变。这时，我们发现了Python。MATLAB的以上不足，恰是Python的优势。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">       **首先，Python完全免费**（[http://python.org/](http://python.org/)），绝大多数科学计算相关扩展库也都是免费的，大多也都是是开源的，所以金钱问题完全不用考虑。版权问题也基本不用考虑，众多的实例程序可以让你拿去就用。（有时候也需要考虑，因为有些授权，如GPL授权，具有"传染性"）。考虑控制版权更严格的诸如美国之类的国家，有着众多的研究人员和大学生使用Python，并有很多网络提供了交流平台，在这个平台可以获得更多的交流学习机会。**其次，Python是一门更易学更严谨的面向对象的程序设计语言。**作为通用程序设计语言的Python，有更为严格清晰的语法，可以轻易完成界面、文件、封装等高阶需求。**最后，不得不提的就是性能。**MATLAB作为科学计算工具，经过了近乎苛刻的优化，Python呢？实话说，纯Python的速度确实不怎么地，但是使用Python的科学计算扩展库numpy、scipy等之后，速度和MATLAB不相上下。（[http://www.scipy.org/PerformancePython#head-a73fa06d3c4f3bda71b3526d30d51c492d8f80df](http://www.scipy.org/PerformancePython)）
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">        以上理由似乎足以让我们割爱MATLAB，选择使用"Python+扩展"来完成科学计算问题。然而，我想起班固的名言"爱而知其恶"，Python进行科学计算是不是完美？又有哪些劣势呢？Google了一阵子，发现大致是这样：第一，因为沉浸在开源的环境下，想私藏代码似乎不是那么容易了，甚至不好意思了。第二，文档系统不是很完善，中文的更是少之又少，这就要求一定的英语文档阅读功底。不过MATLAB至今也没有提供过中文的文档。第三，MATLAB中的有些生僻的专用工具箱没有Python环境下的对应模块功能实现。第四，貌似没有第四了。
</span>

<span style="font-family:Microsoft YaHei UI; font-size:14pt">        以上对比不敢说写的就对，后续有关具体技术和代码的文章更是可能会有重大错误甚至误导。之所以还敢写出来，放到这里，权当借此平台和同道中人进行交流、切磋。文章假设您有初级的Python基础，这样就可以把重心放到科学计算而不是纯粹的语言上来；也假设您有一定的MATLAB基础，因为文中经常拿两者来对比并给出两者的各自实现。欢迎批评！
</span>