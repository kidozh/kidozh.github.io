---
title: '[Web]将BING的桌面作为博客的主题'
tags:
  - bing
  - 爬虫
  - 网页
id: 60
categories:
  - 网页
date: 2015-03-29 23:34:18
---

![](http://f.hiphotos.baidu.com/baike/w%3D268/sign=dc905211612762d0803ea3b998ec0849/1b4c510fd9f9d72a1525fd2fd62a2834349bbbbb.jpg)众所周知，Bing的搜索的桌面实在是好看的一笔，现在我们也可以通过PHP的爬虫来实现我们的主页和微软的Bing的图片保持一致。

PHP代码如下：
<pre class="lang:php decode:true ">function bavotasan_header_images() {
global $post;
$post_id = ( is_attachment() &amp;&amp; isset( $post-&gt;post_parent ) ) ? $post-&gt;post_parent : get_queried_object_id();
$custom_image = ( is_singular() || get_option( 'page_for_posts' ) == $post_id || is_attachment() ) ? get_post_meta( $post_id, 'arcade_basic_custom_image', true ) : '';

$str=file_get_contents('http://cn.bing.com/HPImageArchive.aspx?idx=0&amp;n=1');
if(preg_match("/(.+?)&lt;\/url&gt;/ies",$str,$matches)){
$imgurl='http://cn.bing.com'.$matches[1];
}

if ( $custom_image ) {
//echo '&lt;/pre&gt;
&lt;img class="header-img" src="' . esc_url( $custom_image ) . '" alt="" /&gt;
&lt;pre&gt;';
echo '&lt;/pre&gt;
&lt;img class="header-img" src="' . $imgurl . '" alt="Bing" /&gt;
&lt;pre&gt;';
} else {
if ( $header_image = get_header_image() ) :
?&gt;
&lt;!--&lt;img class="header-img" src="&lt;?//php header_image(); ?&gt;" alt="" /&gt;--&gt;
&lt;/pre&gt;
&lt;img class="header-img" src="&lt;? echo $imgurl?&gt;" alt="" /&gt;
&lt;pre&gt;
&lt;!--?php &lt;br ?--&gt; endif;
}
}</pre>

<div>这样就能够使用Bing的桌面了，简直简单粗暴</div>