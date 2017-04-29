---
title: 构建WordPress主题函数
tags:
  - PHP
  - wordpress
  - 主题
id: 1436
categories:
  - 网页
date: 2016-12-20 06:04:11
---

# 前言

我们已经创建了一个文件结构，那么现在就让我们开始一个主题把。

我们需要添加一些主题函数到我们的主题之中，这些函数将会完成下面的任务：

*   为WordPress主题特征添加一些支持，比如自定义的背景，页首，博文格式等
*   设置主题的默认值
*   对于主题的代码复用

# 编辑文件

首先，让我们创建以及编辑这些文件

*   functions.php
*   inc/template-tags.php
*   inc/tweaks.php
如果你是PHP新人的话，那么PHP的函数的保留字为`function`，比如这样：
<pre class="lang:php decode:true ">function my_function() {
  ...contents of the function
}</pre>
当我们创建这个函数之后，我们就可以在主题之中调用这个函数了。函数能够被调用：
<pre class="lang:php decode:true ">&lt;div&gt;
    &lt;?php my_function(); ?&gt;
&lt;/div&gt;</pre>
其他的函数调用方法就可能有些复杂了：
<pre class="lang:php decode:true ">&lt;div&gt;
    &lt;?php my_second_function( 'parameter 1', 'parameter 2' ); ?&gt;
&lt;/div&gt;</pre>
在上面的例子之中，我们都会向函数之中传递参数，这个函数将会使用其并将其作为最终的输出结果。

# Functions.php

事不宜迟，我们就开始把。

在上节课创建的主题目录之中，打开functions.php文件，在文件最上面，粘贴下面的值：
<pre class="lang:php decode:true ">&lt;?php
/**
 * Shape functions and definitions
 *
 * @package Shape
 * @since Shape 1.0
 */</pre>
如果你是PHP新手的话，我们就从`&lt;?php`开始编辑文件吧。

接下来，我们就有描述内联信息的块注释：一个文件的简短的介绍，接着就是PHP文档的标签：@package和@since。你能够在WordPress Codex的[内联文档](http://codex.wordpress.org/Inline_Documentation)之中找到更多的信息。

php的注释和C语言的注释是很像的。`/* ... */`就是多行注释，而`//` 则是单行注释。

## $content_width

`$content_width` 是一个设置内容（比如图片）最大宽度的全局变量。其能够防止超大图片溢出主要的内容区域。我们应该设置这个值来限制我们主要内容区域的宽度。想想我们之前的HTML结构，这个区域其实就是`#content div`。我们将会使用CSS来设置div的宽度。然而，我们还没有CSS文件。所以在这里，我会告诉你div将会是654px宽。

在`functions.php`之中，无视最后的一个`*/`，粘贴下面的代码：
<pre class="lang:php decode:true ">/**
 * Set the content width based on the theme's design and stylesheet.
 *
 * @since Shape 1.0
 */
if ( ! isset( $content_width ) )
    $content_width = 654; /* pixels */</pre>
所以`$content_width`就被设置好了，PHP变量有一个美元符`$`置于名称之前，在分配值之后，会有一个半角的`;`。

## shape_setup()

接下来，我们将会创建一个函数来新建一个默认主题并且添加一个对于众多WordPress特性支持的函数，跳过在$content_width之后的那一行，添加这个：
<pre class="lang:php decode:true ">if ( ! function_exists( 'shape_setup' ) ):
/**
 * Sets up theme defaults and registers support for various WordPress features.
 *
 * Note that this function is hooked into the after_setup_theme hook, which runs
 * before the init hook. The init hook is too late for some features, such as indicating
 * support post thumbnails.
 *
 * @since Shape 1.0
 */
function shape_setup() {

    /**
     * Custom template tags for this theme.
     */
    require( get_template_directory() . '/inc/template-tags.php' );

    /**
     * Custom functions that act independently of the theme templates
     */
    require( get_template_directory() . '/inc/tweaks.php' );

    /**
     * Make theme available for translation
     * Translations can be filed in the /languages/ directory
     * If you're building a theme based on Shape, use a find and replace
     * to change 'shape' to the name of your theme in all the template files
     */
    load_theme_textdomain( 'shape', get_template_directory() . '/languages' );

    /**
     * Add default posts and comments RSS feed links to head
     */
    add_theme_support( 'automatic-feed-links' );

    /**
     * Enable support for the Aside Post Format
     */
    add_theme_support( 'post-formats', array( 'aside' ) );

    /**
     * This theme uses wp_nav_menu() in one location.
     */
    register_nav_menus( array(
        'primary' =&gt; __( 'Primary Menu', 'shape' ),
    ) );
}
endif; // shape_setup
add_action( 'after_setup_theme', 'shape_setup' );</pre>
代码都是很好注释过的，所以你能很好的了解他们正在做什么。

那么我们就一一说明把：

我们将会引用在inc/文件夹下的两个文件template-tags.php和tweak.php。我们将会在稍后创建这两个文件。

接下来，我们调用了`load_theme_textdomain()`这个函数，这个函数会告诉我们WordPress将会使用我们文件夹下的languages这个来作为翻译的标准。如果你正要创建一个WordPress主题，你一个穷尽你的可能来保证所有字符串都是可翻译的。你永远不知道在啥时候其他人是否需要在其他语言中硬编码。下面有些好的方法来翻译文章，我也会说一些出来，[I18n for WordPress Developers](http://codex.wordpress.org/I18n_for_WordPress_Developers)将会是一个非常好的入门。

接着，下面的两个函数为RSS反馈以及侧边博文格式提供了支持链接。最后一个函数注册了一个导航菜单位置，我们将会在我们的主要菜单中用到。

接下来，我们会用`}`来闭合这个函数，并且使用钩子（hook）的方法将其加到我们的主题函数之中。
<pre class="lang:php decode:true ">add_action( 'after_setup_theme', 'shape_setup' );</pre>
简而言之，我们将会告诉WordPress在运行`after_setup_theme()`之后运行`shape_setup()`函数。

我们将会在functions.php之中加入更多东西。

你可能注意到functions.php文件没有任何PHP的闭合符号?&gt;，这是因为这个文件绝大多数都是PHP代码，所以吞掉闭合符号也是非常安全的。至于我们为什么要这么做的原因，自然是因为其能帮助我们免于闭合PHP代码之后引入的空白符。

## Template-tags.php和Tweak.php

还记得下面的代码吗？
<pre class="lang:php decode:true ">/**
     * Custom template tags for this theme.
     */
    require( get_template_directory() . '/inc/template-tags.php' );

    /**
     * Custom functions that act independently of the theme templates
     */
    require( get_template_directory() . '/inc/tweaks.php' );</pre>
在inc文件夹中创建template-tags.php和tweak.php文件。为什么我们要把自定义的函数分散在众多的文件之中呢？大多数情况下，我们像保持functions.php代码中的干净整洁，但更多的是保证我们主题的模块化，如果你并不需要这些函数的话，你只需要移除这一行就可以了。

### template-tags.php

首先，什么是模板标签？自然是一个函数了。特殊而言，他们是你可以插入到你主题之中来显示动态页面的WordPress函数。你可以在 [everything you want to know about template tags](https://codex.wordpress.org/Template_Tags)找到一些关于模板标签的信息。

在大多数情况下，我们会在任何我们想要的时候将模板标签添加到我们的主题之中。然而，还是有时候我们需要将多个模板标签输出到一起。把所有的标签放到一起自然是一个很好的主意，所以想想我们要添加的模板函数，我们把他们视为一个乐符，最终我们把他们组成到一起成为一个交响乐，就像这样：一句描述博文何时发表，被谁，或者一个上一个和下一个博文的链接，或者是一个评论列表，你就能知道了。我们首先写下了乐符，然后播放多次。或者，从专业的角度上来说，写了一个函数，把他调用多次。

为了保证这个教程不会过于冗长，我们将返回到template-tags.php之中来添加一些我们需要的函数。对现在而言，让我们在文件首添加一些基本的文档信息把。
<pre class="lang:php decode:true ">&lt;?php
/**
 * Custom template tags for this theme.
 *
 * Eventually, some of the functionality here could be replaced by core features
 *
 * @package Shape
 * @since Shape 1.0
 */</pre>
最后需要提到一点：“一些在template-tags.php之中的函数功能也许会被核心特性所替代”。这些我们添加的函数将会和WordPress核心特征一样有用。当我们添加了这些函数之后，这回变得更加有意义。

现在，我们就能够正常的闭合PHP标签了。

### tweak.php

这些我们放在文件中的函数并不会影响到模板标签，而相反的是他们将会提升我们主题的品质。他们提供了一个很好的后台任务，这样使得我们的主题更好。

在文件的页首，粘贴一些寻常的文档信息到里面。
<pre class="lang:php decode:true ">&lt;?php
/**
 * Custom functions that act independently of the theme templates
 *
 * Eventually, some of the functionality here could be replaced by core features
 *
 * @package Shape
 * @since Shape 1.0
 */</pre>
接下来，我们要粘贴下面的函数：
<pre class="lang:php decode:true ">/**
 * Get our wp_nav_menu() fallback, wp_page_menu(), to show a home link.
 *
 * @since Shape 1.0
 */
function shape_page_menu_args( $args ) {
    $args['show_home'] = true;
    return $args;
}
add_filter( 'wp_page_menu_args', 'shape_page_menu_args' );

/**
 * Adds custom classes to the array of body classes.
 *
 * @since Shape 1.0
 */
function shape_body_classes( $classes ) {
    // Adds a class of group-blog to blogs with more than 1 published author
    if ( is_multi_author() ) {
        $classes[] = 'group-blog';
    }

    return $classes;
}
add_filter( 'body_class', 'shape_body_classes' );

/**
 * Filter in a link to a content ID attribute for the next/previous image links on image attachment pages
 *
 * @since Shape 1.0
 */
function shape_enhanced_image_navigation( $url, $id ) {
    if ( ! is_attachment() &amp;&amp; ! wp_attachment_is_image( $id ) )
        return $url;

    $image = get_post( $id );
    if ( ! empty( $image-&gt;post_parent ) &amp;&amp; $image-&gt;post_parent != $id )
        $url .= '#main';

    return $url;
}
add_filter( 'attachment_link', 'shape_enhanced_image_navigation', 10, 2 );</pre>
第一个函数`shape_page_menu_args`，将会影响到我们主要的导航菜单。我们在之前就已经为导航菜单申请了支持，在`shape_setup()`之中。如果导航菜单并没有被配置，WordPress将会显示一连串的页面（由`wp_page_menu()`所决定）

在第二个函数`shape_body_classes()`，我们将会添加一个新的CSS类，`group-blog`，到我们的主题标签之中。我们将会在WordPress Header 模板之中提及到[body class](http://codex.wordpress.org/Function_Reference/body_class)。但是现在，你只需要理解body classes使得我们能够在不同的情况下装饰我们的主题的一些部分（比如我们正在访问的页面类型或者是我们作者的数目）。

最终，第三个函数shape_enhanced_image_navigation()，把#main这个id添加到上一个/下一个图像连接之中。回想一下，“#main”是包装我们的内容和小部件区域的div的ID名称。 ID也是页面内的锚点。 当用户点击您的下一个/上一个图片链接时，他们不必从页面顶部向下滚动来查看每个图片。

这就是tweak.php。记着，我们不需要PHP的闭合标签。

# 后记

Woo，这里有好多函数，我们已经在这个教程之中做出了大量的工作。但是不要太高兴，这只是万里长征的第一步路罢了。

敬请关注