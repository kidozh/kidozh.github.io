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
```php
function bavotasan_header_images() {
global $post;
$post_id = ( is_attachment() && isset( $post->post_parent ) ) ? $post->post_parent : get_queried_object_id();
$custom_image = ( is_singular() || get_option( 'page_for_posts' ) == $post_id || is_attachment() ) ? get_post_meta( $post_id, 'arcade_basic_custom_image', true ) : '';

$str=file_get_contents('http://cn.bing.com/HPImageArchive.aspx?idx=0&n=1');
if(preg_match("/(.+?)<\/url>/ies",$str,$matches)){
$imgurl='http://cn.bing.com'.$matches[1];
}

if ( $custom_image ) {
//echo '</pre>
<img class="header-img" src="' . esc_url( $custom_image ) . '" alt="" />
<pre>';
echo '</pre>
<img class="header-img" src="' . $imgurl . '" alt="Bing" />
<pre>';
} else {
if ( $header_image = get_header_image() ) :
?>
<!--<img class="header-img" src="<?//php header_image(); ?>" alt="" />-->
</pre>
<img class="header-img" src="<? echo $imgurl?>" alt="" />
<pre>
<!--?php <br ?--> endif;
}
}
```


这样就能够使用Bing的桌面了，简直简单粗暴