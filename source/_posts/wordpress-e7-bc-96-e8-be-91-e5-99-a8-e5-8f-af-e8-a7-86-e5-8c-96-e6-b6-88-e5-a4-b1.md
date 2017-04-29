---
title: '[WordPress]编辑器可视化消失'
tags:
  - wordpress
  - 网页
id: 455
categories:
  - 网页
date: 2015-11-22 17:51:47
---

<article class="entry" style="font-size: 14px; line-height: 28px; font-family: 'Microsoft Yahei', Verdana, Tahoma, Arial, Helvetica, sans-serif, 宋体;">

WordPress文章编辑器可视化/文本状态无法切换消失的问题有用户遇到过，出现这样的问题时，我们首先应该回忆一下，之前自己进行了哪些操作导致这种情况的出现，比如：

*   更换了新主题？
*   安装了新插件或升级插件？
*   更新了WordPress版本？
*   网站数据进行了备份还原？
*   网站更换空间、更换域名？

![WP_Problem](/wp-content/uploads/2015/11/5fdf8db1cb134954627be9e2574e9258d0094aca.jpg)

如果遇到了这种情况，我们可以尝试以下方法：

**1\. 检查是否开启了可视化编辑器**：

在网站后台，找到【** 用户 – 我的个人资料 **】，查看是否勾选了“**撰写文章时不使用可视化编辑器**”，如果勾选了，则表示不使用可视化编辑器，所以，这里我们要取消勾选，如下图所示：

[caption id="attachment_466" align="alignnone" width="486"][![错误项](/wp-content/uploads/2015/11/wp-editor-02.jpg)](/wp-content/uploads/2015/11/wp-editor-02.jpg) 错误项[/caption]

如果还是无法解决，则进行下面的操作再来测试看看。

2\. 更换为WP自带默认主题，禁用所有插件(尤其是**Markdown**)；

3. 清理你的当前浏览器缓存，或者使用其他浏览器；

4\. 下载相同版本的WordPress安装包，解压后通过FTP上传覆盖老的WordPress程序；

5\. 打开网站根目录，找到 wp-config.php ，在底部添加以下代码：

define(‘CONCATENATE_SCRIPTS’, false);

</article>