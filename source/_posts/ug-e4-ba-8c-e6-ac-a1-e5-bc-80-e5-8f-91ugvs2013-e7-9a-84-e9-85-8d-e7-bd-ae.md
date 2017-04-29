---
title: '[UG二次开发]UG+VS2013 的配置'
tags:
  - C++
  - UG
  - 机械
id: 323
categories:
  - 机械
date: 2015-05-01 23:36:43
---

   

<span style="color:black; font-family:宋体"><span style="font-size:14pt">手工搭建Win32项目文件？？<span style="color:red">（测试VS2005可行，VS2013可行）<span style="color:black">
					</span></span></span><span style="font-size:12pt">
			</span></span>

1.  <div><span style="color:black; font-size:14pt">在工程属性的 C/C++ <span style="font-family:Cambria Math">→</span> General常规 <span style="font-family:Cambria Math">→</span> Additional Include Directories附加包含目录中添加NXOpen链接库路径$(UGII_BASE_DIR)\ugopen </span>
			</div>

    ![](/wp-content/uploads/2015/05/050115_1536_UGUGVS201.png)<span style="font-family:宋体; font-size:12pt">
				</span>

2.  <div><span style="color:black; font-size:14pt">Linker连接器<span style="font-family:Cambria Math">→</span> General常规<span style="font-family:Cambria Math">→</span>Additional Include Directories附加包含目录中添加NXOpen链接库路径$(UGII_BASE_DIR)\ugopen </span>
			</div>

    ![](/wp-content/uploads/2015/05/050115_1536_UGUGVS202.png)<span style="font-family:宋体; font-size:12pt">
				</span>

3.  <div><span style="color:black; font-size:14pt">添加预编译宏_SECURE_SCL=0; 到工程属性C/C++<span style="font-family:Cambria Math">→</span> Preprocessor预处理器<span style="font-family:Cambria Math">→</span> Preprocessor Definitions预处理器定义 </span>
			</div>

    ![](/wp-content/uploads/2015/05/050115_1536_UGUGVS203.png)<span style="font-family:宋体; font-size:12pt">
				</span>

4.  <div><span style="color:black; font-size:14pt">在工程属性的 Linker链接器<span style="font-family:Cambria Math">→</span> Input输入<span style="font-family:Cambria Math">→</span> Additional Dependencies附加依赖项 根据需要添加以下链接库 </span>
			</div>

    <span style="font-family:宋体"><span style="color:black; font-size:14pt">libufun.lib  支持 UFUNC API 函数库 </span><span style="font-size:12pt">
					</span></span>

<span style="font-family:宋体"><span style="color:black; font-size:14pt">libugopenint.lib  支持 UFUNC对话框 API 函数库 </span><span style="font-size:12pt">
					</span></span>

<span style="font-family:宋体"><span style="color:black; font-size:14pt">libnxopencpp.lib  支持 NXOpenAPI函数库 </span><span style="font-size:12pt">
					</span></span>

<span style="font-family:宋体"><span style="color:black; font-size:14pt">libnxopenuicpp.lib  支持 NXOpen对话框即Block UI Styler API 函数库 </span><span style="font-size:12pt">
					</span></span>

![](/wp-content/uploads/2015/05/050115_1536_UGUGVS204.png)<span style="font-family:宋体; font-size:12pt">
				</span>

<span style="font-family:宋体"><span style="color:black; font-size:14pt">注意：在调试时使用多线程调试 </span><span style="font-size:12pt">
			</span></span>

![](/wp-content/uploads/2015/05/050115_1536_UGUGVS205.png)