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

选择使用 <span class="wp_keywordlink_affiliate" style="text-rendering: optimizeLegibility; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; margin: 0px; padding: 0px;">[WordPress](http://www.lamp99.com/tag/wordpress-cases "View all posts in WordPress")</span> 来搭建博客，主要原因便在于 <span class="wp_keywordlink_affiliate" style="text-rendering: optimizeLegibility; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; margin: 0px; padding: 0px;">[WordPress](http://www.lamp99.com/tag/wordpress-cases "View all posts in WordPress")</span> 有较高的流行度，还有各种围绕其进行的<span class="wp_keywordlink_affiliate" style="text-rendering: optimizeLegibility; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; margin: 0px; padding: 0px;">[开发](http://www.lamp99.com/tag/%e5%bc%80%e5%8f%91 "View all posts in 开发")</span>的扩展功能应有尽有，基本上可以说我们在博客建设中所需的任何功能，都已有人想到并得到实现，让你不必在博客具体的技术实现及功能扩展方面投入过多的精力，而更专注于内容建设。

本文以技术手册的方式简单汇总 WordPress 主题模板的基本资料，希望能对 WordPress 主题模板<span class="wp_keywordlink_affiliate" style="text-rendering: optimizeLegibility; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; margin: 0px; padding: 0px;">[开发](http://www.lamp99.com/tag/%e5%bc%80%e5%8f%91 "View all posts in 开发")</span>的朋友解渴。

# 2 结构

WordPress 主题模板基本文件

一套完整的 WordPress 主题模板应至少具有如下文件：,WordPress基本模板文件，WordPress模板必备文件：
<pre class="lang:default highlight:0 decode:true">style.css : CSS(样式表)文件
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
search.php : 搜索结果模板</pre>

 <span style="color: #636b75; font-family: HelveticaNeue-Regular, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22.4px;">基本条件判断Tag：</span>
<pre class="lang:default highlight:0 decode:true">is_home() : 是否为主页
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
is_paged() : 主页/Category/Archive页是否以多页显示</pre>

 <span style="color: #636b75; font-family: HelveticaNeue-Regular, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22.4px;">Header部分常用到的PHP</span><span class="wp_keywordlink_affiliate" style="text-rendering: optimizeLegibility; border: 0px; font-stretch: inherit; font-size: 14px; line-height: 22.4px; font-family: HelveticaNeue-Regular, 'Helvetica Neue', Helvetica, Arial, sans-serif; vertical-align: baseline; margin: 0px; padding: 0px; color: #636b75;">[函数](http://www.lamp99.com/tag/%e5%87%bd%e6%95%b0 "View all posts in 函数")</span>
<pre class="lang:default highlight:0 decode:true">&lt;!--?php bloginfo (’name’); ?--&gt; : 博客名称(Title)
&lt;!--?php bloginfo (’stylesheet_url’); ?--&gt; : CSS文件路径
&lt;!--?php bloginfo (’pingback_url’); ?--&gt; : PingBack Url
&lt;!--?php bloginfo (’template_url’); ?--&gt; : 模板文件路径
&lt;!--?php bloginfo (’version’); ?--&gt; : WordPress版本
&lt;!--?php bloginfo (’atom_url’); ?--&gt; : Atom Url
&lt;!--?php bloginfo (’rss2_url’); ?--&gt; : RSS 2.o Url
&lt;!--?php bloginfo (’url’); ?--&gt; : 博客 Url
&lt;!--?php bloginfo (’html_type’); ?--&gt; : 博客网页Html类型
&lt;!--?php bloginfo (’charset’); ?--&gt; : 博客网页编码
&lt;!--?php bloginfo (’description’); ?--&gt; : 博客描述
&lt;!--?php wp_title(); ?--&gt; : 特定内容页(Post/Page)的标题</pre>

 <span style="color: #636b75; font-family: HelveticaNeue-Regular, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22.4px;">模板常用的PHP</span><span class="wp_keywordlink_affiliate" style="text-rendering: optimizeLegibility; border: 0px; font-stretch: inherit; font-size: 14px; line-height: 22.4px; font-family: HelveticaNeue-Regular, 'Helvetica Neue', Helvetica, Arial, sans-serif; vertical-align: baseline; margin: 0px; padding: 0px; color: #636b75;">[函数](http://www.lamp99.com/tag/%e5%87%bd%e6%95%b0 "View all posts in 函数")</span><span style="color: #636b75; font-family: HelveticaNeue-Regular, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22.4px;">及命令</span>
<pre class="lang:default highlight:0 decode:true">&lt;!--?php get_header(); ?--&gt; : 调用Header模板
&lt;!--?php get_sidebar(); ?--&gt; : 调用Sidebar模板
&lt;!--?php get_footer(); ?--&gt; : 调用Footer模板
&lt;!--?php the_content(); ?--&gt; : 显示内容(Post/Page)
&lt;!--?php the_excerpt(); ?--&gt;: 显示摘要
&lt;!--?php if(have_posts()) : ?--&gt; : 检查是否存在Post/Page
&lt;!--?php while(have_posts()) : the_post(); ?--&gt; : 如果存在Post/Page则予以显示
&lt;!--?php endwhile; ?--&gt; : While 结束
&lt;!--?php endif; ?--&gt; : If 结束
&lt;!--?php the_time(’字符串’) ?--&gt; : 显示时间，时间格式由“字符串”参数决定，具体参考PHP手册
&lt;!--?php comments_popup_link(); ?--&gt; : 正文中的留言链接。如果使用 comments_popup_script() ，则留言会在新窗口中打开，反之，则在当前窗口打开
&lt;!--?php the_title(); ?--&gt; : 内容页(Post/Page)标题
&lt;!--?php the_permalink() ?--&gt; : 内容页(Post/Page) Url
&lt;!--?php the_category(’, ‘) ?--&gt; : 特定内容页(Post/Page)所属Category
&lt;!--?php the_author(); ?--&gt; : 作者
&lt;!--?php the_ID(); ?--&gt; : 特定内容页(Post/Page) ID
&lt;!--?php edit_post_link(); ?--&gt; : 如果用户已登录并具有权限，显示编辑链接
&lt;!--?php get_links_list(); ?--&gt; : 显示Blogroll中的链接
&lt;!--?php comments_template(); ?--&gt; : 调用留言/回复模板
&lt;!--?php wp_list_pages(); ?--&gt; : 显示Page列表
&lt;!--?php wp_list_categories(); ?--&gt; : 显示Categories列表
&lt;!--?php next_post_link(’ %link ‘); ?--&gt; : 下一篇文章链接
&lt;!--?php previous_post_link(’%link’); ?--&gt; : 上一篇文章链接
&lt;!--?php get_calendar(); ?--&gt; : 日历
&lt;!--?php wp_get_archives() ?--&gt; : 显示内容存档
&lt;!--?php posts_nav_link(); ?--&gt; : 导航，显示上一篇/下一篇文章链接
&lt;!--?php include(TEMPLATEPATH . ‘/文件名’); ?--&gt; : 嵌入其他文件，可为定制的模板或其他类型文件</pre>

 <span style="color: #636b75; font-family: HelveticaNeue-Regular, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22.4px;">与模板相关的其他函数</span>
<pre class="lang:default highlight:0 decode:true">&lt;!--?php _e(’Message’); ?--&gt; : 输出相应信息
&lt;!--?php wp_register(); ?--&gt; : 显示注册链接
&lt;!--?php wp_loginout(); ?--&gt; : 显示登录/注销链接
&lt;!--–next page–--&gt; : 将当前内容分页
&lt;!--–more–--&gt; : 将当前内容截断，以不在主页/目录页显示全部内容
&lt;!--?php timer_stop(1); ?--&gt; : 网页加载时间(秒)
&lt;!--?php echo get_num_queries(); ?--&gt; : 网页加载查询量</pre>

 其他：
<pre class="lang:default highlight:0 decode:true">&lt;!--?php get_archives(’postbypost’, 10); ?--&gt; 调用最近的10篇日志
&lt;!--?php
$rand_posts = get_posts(’numberposts=10&amp;orderby=rand’);
foreach( $rand_posts as $post ) :
?--&gt;
&lt;li&gt;&lt;a href="”&lt;?php" the_permalink();="" ?=""&gt;”&gt;
&lt;!--?php the_title(); ?--&gt;&lt;/a&gt;&lt;/li&gt;
&lt;!--?php endforeach; ?--&gt;</pre>

 <span style="color: #636b75; font-family: HelveticaNeue-Regular, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22.4px;">随机调用10篇日志</span>
<pre class="lang:default highlight:0 decode:true">&lt;!--?php the_tags(’Post Tags :’, ‘, ‘, ‘&lt;br /--&gt;’); ?&gt; 调用标签

&lt;!--?php if (get_the_tags()) the_tags(’Tags:’,’,’,’end’); ?--&gt;
</pre>

 <span style="color: #636b75; font-family: HelveticaNeue-Regular, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22.4px;">标签存在时调用</span>
<pre class="lang:default highlight:0 decode:true ">&lt;!--?php wp_tag_cloud(’smallest=1&amp;largest=9&amp;’); ?--&gt; 调用标签云
&lt;!--?php $posts = get_posts( “category=12&amp;numberposts=4″ ); ?--&gt; 获得4篇12分类中的日志</pre>

 <span style="color: #636b75; font-family: HelveticaNeue-Regular, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22.4px;">下面是直接来自wordpress.org</span>
<pre class="lang:default highlight:0 decode:true">is_single() 判断是否是具体文章的页面
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
面，例如：if(is_home() &amp;&amp; !is_paged() )
is_attachment() //When an attachment document to a post or Page is being displayed. An attachment is an image or other file uploaded through the post editor’s upload utility. Attachments can be displayed on their own ‘page’ or template. For more information, see Using Image and File Attachments.
is_feed() //When the site requested is a Syndication.This tag is not typically used by users; it is used internally by
WordPress and is available for Plugin Developers.
is_trackback() //When the site requested is WordPress’ hook into its Trackback engine. This tag is not typically used by users; it is used internally by WordPress and is available for Plugin Developers.</pre>