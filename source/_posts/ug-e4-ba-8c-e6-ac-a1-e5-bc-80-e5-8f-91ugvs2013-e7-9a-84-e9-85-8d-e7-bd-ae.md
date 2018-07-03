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

   

手工搭建Win32项目文件？？（测试VS2005可行，VS2013可行）
					
			

1.  在工程属性的 C/C++ → General常规 → Additional Include Directories附加包含目录中添加NXOpen链接库路径$(UGII_BASE_DIR)\ugopen 
			

    ![](/wp-content/uploads/2015/05/050115_1536_UGUGVS201.png)
				

2.  Linker连接器→ General常规→Additional Include Directories附加包含目录中添加NXOpen链接库路径$(UGII_BASE_DIR)\ugopen 
			

    ![](/wp-content/uploads/2015/05/050115_1536_UGUGVS202.png)
				

3.  添加预编译宏_SECURE_SCL=0; 到工程属性C/C++→ Preprocessor预处理器→ Preprocessor Definitions预处理器定义 
			

    ![](/wp-content/uploads/2015/05/050115_1536_UGUGVS203.png)
				

4.  在工程属性的 Linker链接器→ Input输入→ Additional Dependencies附加依赖项 根据需要添加以下链接库 
			

    libufun.lib  支持 UFUNC API 函数库 
					

libugopenint.lib  支持 UFUNC对话框 API 函数库 
					

libnxopencpp.lib  支持 NXOpenAPI函数库 
					

libnxopenuicpp.lib  支持 NXOpen对话框即Block UI Styler API 函数库 
					

![](/wp-content/uploads/2015/05/050115_1536_UGUGVS204.png)
				

注意：在调试时使用多线程调试 
			

![](/wp-content/uploads/2015/05/050115_1536_UGUGVS205.png)