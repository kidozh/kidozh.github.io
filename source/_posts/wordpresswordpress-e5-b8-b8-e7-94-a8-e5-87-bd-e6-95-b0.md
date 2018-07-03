---
title: '[WordPress]WordPress常用函数'
tags:
  - wordpress
id: 747
categories:
  - 网页
date: 2015-12-21 17:41:17
---

> 本文来自：[Lamp99](http://www.lamp99.com/wordpress-commonly-used-functions.html)

# 1 前言

选择使用 [WordPress](http://www.lamp99.com/tag/wordpress-cases "View all posts in WordPress") 来搭建博客，主要原因便在于 [WordPress](http://www.lamp99.com/tag/wordpress-cases "View all posts in WordPress") 有较高的流行度，还有各种围绕其进行的[开发](http://www.lamp99.com/tag/%e5%bc%80%e5%8f%91 "View all posts in 开发")的扩展功能应有尽有，基本上可以说我们在博客建设中所需的任何功能，都已有人想到并得到实现，让你不必在博客具体的技术实现及功能扩展方面投入过多的精力，而更专注于内容建设。

本文以技术手册的方式简单汇总 WordPress 主题模板的基本资料，希望能对 WordPress 主题模板[开发](http://www.lamp99.com/tag/%e5%bc%80%e5%8f%91 "View all posts in 开发")的朋友解渴。

# 2 结构

WordPress 主题模板基本文件

一套完整的 WordPress 主题模板应至少具有如下文件：,WordPress基本模板文件，WordPress模板必备文件：
```default
style.css : CSS(样式表)文件
index.php : 主页模板
archive.php : Archive/Category模板
404.php : Not Found 错误页模板
comments.php : 留言/回复模板
footer.php : Footer模板
header.php : Header模板
sidebar.php : 侧栏模板
page.php : 内容页(Page)模板
single.php : 内容页(Post)模板
searchform.php : 搜索表单模板
search.php : 搜索结果模板
```


 基本条件判断Tag：
```default
is_home() : 是否为主页
is_single() : 是否为内容页(Post)
is_page() : 是否为内容页(Page)
is_category() : 是否为Category/Archive页
is_tag() : 是否为Tag存档页
s_date() : 是否为指定日期存档页
is_year() : 是否为指定年份存档页
is_month() : 是否为指定月份存档页
is_day() : 是否为指定日存档页
is_time() : 是否为指定时间存档页
is_archive() : 是否为存档页
is_search() : 是否为搜索结果页
s_404() : 是否为 “HTTP 404: Not Found” 错误页
is_paged() : 主页/Category/Archive页是否以多页显示
```


 Header部分常用到的PHP[函数](http://www.lamp99.com/tag/%e5%87%bd%e6%95%b0 "View all posts in 函数")
```default
<!--?php bloginfo (’name’); ?--> : 博客名称(Title)
<!--?php bloginfo (’stylesheet_url’); ?--> : CSS文件路径
<!--?php bloginfo (’pingback_url’); ?--> : PingBack Url
<!--?php bloginfo (’template_url’); ?--> : 模板文件路径
<!--?php bloginfo (’version’); ?--> : WordPress版本
<!--?php bloginfo (’atom_url’); ?--> : Atom Url
<!--?php bloginfo (’rss2_url’); ?--> : RSS 2.o Url
<!--?php bloginfo (’url’); ?--> : 博客 Url
<!--?php bloginfo (’html_type’); ?--> : 博客网页Html类型
<!--?php bloginfo (’charset’); ?--> : 博客网页编码
<!--?php bloginfo (’description’); ?--> : 博客描述
<!--?php wp_title(); ?--> : 特定内容页(Post/Page)的标题
```


 模板常用的PHP[函数](http://www.lamp99.com/tag/%e5%87%bd%e6%95%b0 "View all posts in 函数")及命令
```default
<!--?php get_header(); ?--> : 调用Header模板
<!--?php get_sidebar(); ?--> : 调用Sidebar模板
<!--?php get_footer(); ?--> : 调用Footer模板
<!--?php the_content(); ?--> : 显示内容(Post/Page)
<!--?php the_excerpt(); ?-->: 显示摘要
<!--?php if(have_posts()) : ?--> : 检查是否存在Post/Page
<!--?php while(have_posts()) : the_post(); ?--> : 如果存在Post/Page则予以显示
<!--?php endwhile; ?--> : While 结束
<!--?php endif; ?--> : If 结束
<!--?php the_time(’字符串’) ?--> : 显示时间，时间格式由“字符串”参数决定，具体参考PHP手册
<!--?php comments_popup_link(); ?--> : 正文中的留言链接。如果使用 comments_popup_script() ，则留言会在新窗口中打开，反之，则在当前窗口打开
<!--?php the_title(); ?--> : 内容页(Post/Page)标题
<!--?php the_permalink() ?--> : 内容页(Post/Page) Url
<!--?php the_category(’, ‘) ?--> : 特定内容页(Post/Page)所属Category
<!--?php the_author(); ?--> : 作者
<!--?php the_ID(); ?--> : 特定内容页(Post/Page) ID
<!--?php edit_post_link(); ?--> : 如果用户已登录并具有权限，显示编辑链接
<!--?php get_links_list(); ?--> : 显示Blogroll中的链接
<!--?php comments_template(); ?--> : 调用留言/回复模板
<!--?php wp_list_pages(); ?--> : 显示Page列表
<!--?php wp_list_categories(); ?--> : 显示Categories列表
<!--?php next_post_link(’ %link ‘); ?--> : 下一篇文章链接
<!--?php previous_post_link(’%link’); ?--> : 上一篇文章链接
<!--?php get_calendar(); ?--> : 日历
<!--?php wp_get_archives() ?--> : 显示内容存档
<!--?php posts_nav_link(); ?--> : 导航，显示上一篇/下一篇文章链接
<!--?php include(TEMPLATEPATH . ‘/文件名’); ?--> : 嵌入其他文件，可为定制的模板或其他类型文件
```


 与模板相关的其他函数
```default
<!--?php _e(’Message’); ?--> : 输出相应信息
<!--?php wp_register(); ?--> : 显示注册链接
<!--?php wp_loginout(); ?--> : 显示登录/注销链接
<!--–next page–--> : 将当前内容分页
<!--–more–--> : 将当前内容截断，以不在主页/目录页显示全部内容
<!--?php timer_stop(1); ?--> : 网页加载时间(秒)
<!--?php echo get_num_queries(); ?--> : 网页加载查询量
```


 其他：
```default
<!--?php get_archives(’postbypost’, 10); ?--> 调用最近的10篇日志
<!--?php
$rand_posts = get_posts(’numberposts=10&orderby=rand’);
foreach( $rand_posts as $post ) :
?-->
<li><a href="”<?php" the_permalink();="" ?="">”>
<!--?php the_title(); ?--></a></li>
<!--?php endforeach; ?-->
```


 随机调用10篇日志
```default
<!--?php the_tags(’Post Tags :’, ‘, ‘, ‘<br /-->’); ?> 调用标签

<!--?php if (get_the_tags()) the_tags(’Tags:’,’,’,’end’); ?-->

```


 标签存在时调用
```default
<!--?php wp_tag_cloud(’smallest=1&largest=9&’); ?--> 调用标签云
<!--?php $posts = get_posts( “category=12&numberposts=4″ ); ?--> 获得4篇12分类中的日志
```


 下面是直接来自wordpress.org
```default
is_single() 判断是否是具体文章的页面
is_single(’17′) 判断是否是具体文章（id=17）的页面
is_single(’Beef Stew’) 判断是否是具体文章（标题判断）的页面
is_single(’beef-stew’) 判断是否是具体文章（slug判断）的页面
comments_open() 是否留言开启
pings_open() 是否开启ping
is_page() 是否是页面
is_page(’42′) 同single，id判断，即是否是id为42的页面
is_page(’About Me’) title判断
is_page(’about-me’) slug判断
is_category() 是否是分类
is_category(’6′) 同single，id判断，即是否是id为6的分类
is_category(’Cheeses’) title判断
is_category(’cheeses’) slug判断
in_category(’5′) 判断当前的文章是否属于分类5
is_author() 将所有的作者的页面显示出来
is_author(’1337′) 显示author number为1337的页面
is_author(’Elite Hacker’) 通过昵称来显示当前作者的页面
is_author(’elite-hacker’)
is_date()
is_year()
is_month()
is_day()
is_time()
is_archive() 判断当前是否是归档页面
is_search() 判断是否是搜索
is_404() 判断页面是否404
is_paged() 判断是否翻页，比如你当前的blog是http://domain.com
显示http://domain.com?paged=2的时候，这个判断将返回真，通过这个函数可以配合is_home来控制某些只能在首页显示的界
面，例如：if(is_home() && !is_paged() )
is_attachment() //When an attachment document to a post or Page is being displayed. An attachment is an image or other file uploaded through the post editor’s upload utility. Attachments can be displayed on their own ‘page’ or template. For more information, see Using Image and File Attachments.
is_feed() //When the site requested is a Syndication.This tag is not typically used by users; it is used internally by
WordPress and is available for Plugin Developers.
is_trackback() //When the site requested is WordPress’ hook into its Trackback engine. This tag is not typically used by users; it is used internally by WordPress and is available for Plugin Developers.
```
