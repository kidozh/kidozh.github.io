---
title: phpstorm开发wordpress
tags:
  - PHPStorm
  - wordpress
id: 1332
categories:
  - 网页
date: 2016-07-27 17:56:40
---

# 前言

众所周知，phpstorm是一个非常易用的PHP的IDE，而wordpress则是一款比较常见的博客后台。这里就可以使用PHPStorm来开发wordpress（比如插件，主题以及核心）。

# 把wordpress集成到一个现存的PHPStorm工程

你可以这样创建一个WordPress插件工程。

![创建WordPress](/wp-content/uploads/2016/07/创建WordPress.png)

当你就绪的工程被认为是wordPress的插件的时候，你就能够在事件日志（Event Log）中启用对于WordPress的支持。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_enable_integration.png?version=1&amp;modificationDate=1395243268000&amp;api=v2)

你需要提供WordPress的一个安装路径（也就是WordPress的根目录，里面需要包含wp-admin和wp-include这两个子文件夹）

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_enable_integration_dialog.png?version=1&amp;modificationDate=1395243403000&amp;api=v2)

WordPress集成可以在`Setting/WordPress`下设置：

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_integration_settings.png?version=1&amp;modificationDate=1395243492000&amp;api=v2)

而在我的PHPStorm里是这样的：![WordPress设置](/wp-content/uploads/2016/07/WordPress设置-1-1024x693.jpg)

# 创建一个WordPress的新插件

新的WordPress插件可以在欢迎屏幕中通过选择`File | New Project`来创建。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorual_new_project_plugin.png?version=1&amp;modificationDate=1395243626000&amp;api=v2)

工程类型应该被设置为WordPress Plugin。在点到OK之后，你需要提供WordPress的安装路径。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_new_project_plugin_path.png?version=1&amp;modificationDate=1395243763000&amp;api=v2)

初始的插件文件就会被自动创建（插件名称和一个合适的元信息摘要）

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_new_project_structure.png?version=1&amp;modificationDate=1395243914000&amp;api=v2)

# 开发环境的配置

不管你是否做了上面的事情，IDE都会检查开发环境是否为WordPress开发所正确配置。如果配置不满足要求的话，气泡就会弹出一个修复的建议。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_enable_integration_event_log.png?version=1&amp;modificationDate=1395244820000&amp;api=v2)

## 路径配置

你所处于的`wp-content`文件夹和插件需要都在WordPress安装文件夹之外。为了利用PHPStorm的智能代码，代码补全还有其他特征，WordPress的安装文件夹需要包含在外部引用中。只要WordPress安装路径在WordPress集成配置之中提供了，IDE把WordPress安装路径添加到你工程的`Include Path`之中。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_include_path_notification.png?version=1&amp;modificationDate=1395245104000&amp;api=v2)

你也可以在`Setting | PHP | Include Path`中变更Include Path：

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_include_path_settings.png?version=1&amp;modificationDate=1395245203000&amp;api=v2)

在这个使用案例之中，WordPress安装路径需要被添加到一个外部库之中（此时所有WordPress核心文件夹都被索引了），但是其他的插件和主题默认是不会被添加了，并且为了把他们安装到`Settings | PHP | Include path`之中。

## 内容根目录配置

如果你开发的WordPress插件安装在WordPress安装文件夹之中，IDE就会建议把整个WordPress安装目录加到目录之中接着移除初始文件根目录。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_content_root_notification.png?version=1&amp;modificationDate=1395245507000&amp;api=v2)

内容目录也可以在`Setting | Directories`中设置：

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_settings_directories_content_root.png?version=1&amp;modificationDate=1395245612000&amp;api=v2)

## WordPress代码风格

当WordPress集成被启用之后，你就能够基于代码格式来设置WordPress的代码风格。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_coding_style_notification.png?version=1&amp;modificationDate=1395249434000&amp;api=v2)

代码风格可以在Setting | Code Style | PHP 中重新配置。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_set_code_style.png?version=3&amp;modificationDate=1395249724000&amp;api=v2)

# WordPress钩子函数的支持

## WordPress的action和filter函数参数的补齐

所有在WordPress核心函数以及插件的钩子函数都会被IDE检索，并且钩子名称也可以使用Ctrl+Space来补齐`add_action`和`add_filter`的参数。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_hook_completion.png?version=1&amp;modificationDate=1395318637000&amp;api=v2)

## action和filter钩子函数的导航

从WordPress的钩子注册中你从一个导航图标可以寻找到其来源。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_hook_invokation_nav.png?version=1&amp;modificationDate=1395319085000&amp;api=v2)

你可以在特定的一行中找到来源：

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_hook_invokation_nav_res.png?version=2&amp;modificationDate=1395319196000&amp;api=v2)

## 钩子函数注册的回调函数

第二个钩子函数参数如果被声明是一个函数(`add_action`和`add_filter`)的话，你可以使用`Ctrl+B`或者`Ctrl+单击`来查看这个函数的来源。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_goto_declaration.png?version=1&amp;modificationDate=1395319687000&amp;api=v2)

你可以点击这个名称到相关函数的声明处。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_goto_declaration_res.png?version=1&amp;modificationDate=1395319758000&amp;api=v2)

## 钩子函数的导航

通过在`Ctrl+Alt+Shift+N`键（`Navigate | Symbol`），你就能够轻松的搜索钩子并且轻松的找到他们。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_goto_symbol.png?version=1&amp;modificationDate=1395320131000&amp;api=v2)

你也可以使用双击`Shift`来找到钩子函数。如果有必要的话，同样需要确保开启纳入非工程文件选项。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_goto_symbol_everywhere.png?version=3&amp;modificationDate=1395320419000&amp;api=v2)

## 找到钩子注册函数的用法

你也可以使用`Alt+F7`来找到钩子函数的用法，这样会提供一系列可能的选项（在`find usage of XXX`中找到）

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_find_usages.png?version=1&amp;modificationDate=1395321271000&amp;api=v2)

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_find_usages_options.png?version=2&amp;modificationDate=1395321325000&amp;api=v2)

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_find_usages_results.png?version=1&amp;modificationDate=1395321335000&amp;api=v2)

## 从WordPress.org上找到详情

WordPress文档可以在IDE通过搜索文档上得到消息，你需要做的仅仅是选择你所需要的文本，右键转到`Search on WordPress.org`就可以了。

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_search_wordpress_org.png?version=1&amp;modificationDate=1395321743000&amp;api=v2)

默认浏览器也能够接受到IDE的请求，并且访问请求

![](http://confluence.jetbrains.com/download/attachments/53335443/wordpress_tutorial_search_wordpress_org_res.png?version=1&amp;modificationDate=1395321890000&amp;api=v2)

# WordPress命令行WP-CLI集成