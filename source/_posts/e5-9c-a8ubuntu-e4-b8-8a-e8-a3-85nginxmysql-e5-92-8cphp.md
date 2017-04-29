---
title: 在Ubuntu上装Nginx，MySQL和PHP
tags:
  - MySQL
  - Nginx
  - Ubuntu
id: 1355
categories:
  - Ubuntu
date: 2016-10-16 21:34:04
---

# 前言

最近倒腾tornado以及这个网站从SAE迁回了腾讯云，花了不少时间和nginx打交道。所以准备记录一下我怎么倒腾Nginx的过程。（同时控诉一下Apache2的恶心）

# 安装Nginx服务器

为了展现一个动态网页，我们现在就部署Nginx，Nginx是一款现代和高效的网络服务器。

下面所有的命令都是基于Ubuntu自带的默认源，也就是说，你只需要巧妙的使用`apt`来安装就可以了。

因为我们这是第一次使用apt来安装，所以我们需要先更新源。

<pre class="lang:sh decode:true ">sudo apt-get update
sudo apt-get install nginx</pre>

在Ubuntu 14.04这个版本里，Nginx会根据安装时候的配置来决定启动方式。

你可以直接通过访问IP或者域名来观察Nginx是否启动完毕了。

如果你不知道的话，很简单，运行下面的命令就可以知道自己服务器公共的IP地址了。

<pre class="lang:sh decode:true">ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'</pre>
<pre class="lang:default decode:true">111.111.111.111
fe80::601:17ff:fe61:9801</pre>

或者你觉得麻烦，这样也可以：

<pre class="lang:sh decode:true ">curl http://icanhazip.com</pre>
<pre class="lang:default decode:true">111.111.111.111</pre>

这样就知道了地址。这里由于我在的RWTH-Aachen屏蔽了这个网站，所以就查不到，具体情况你可以联系网管。

直接输入IP或者域名。

<pre class="lang:default highlight:0 decode:true ">http://server_domain_name_or_IP</pre>

&nbsp;

![nginx_default](http://kidozh.com/wp-content/uploads/2016/10/nginx_default.png)

如果你看到了Nginx的欢迎页面，那么恭喜您，Ngnix就装好了。

# 安装MySQL来储存数据

现在我们已经安装好了网络服务器了，那么我们就需要一个数据库来支撑我们整个网站的数据储存业务了。

最简单的就是输入下面的命令：

<pre class="lang:sh decode:true ">sudo apt-get install mysql-server</pre>

在此期间，你会被要求输入一个MySQL管理员的密码。

这样，MySQL就安装好了，但是需要我们来配置。

首先，我们需要让MySQL生成一个可以存储信息和数据结构的目录，我们只需要键入下面的命令：

<pre class="lang:sh decode:true ">sudo mysql_install_db</pre>

接下来，你可以运行一个安全脚本来引导你做一些安全的配置，你需要输入命令：

<pre class="lang:sh decode:true ">sudo mysql_secure_installation</pre>

在这个过程中，你需要在安装过程中提供您MySQL管理员的密码。

接着，他会询问您是否想变更密码，如果您对您现在的MySQL密码很满意的话，输入`N`然后按下`Enter`键就可以了，接着，您需要移除测试的数据库和用户。在这个过程中，您只需要一路按`Enter`来继续就可以了。

一旦脚本跑完了，那么MySQL就对数据饥渴难耐了。

# 安装PHP

现在，我们已经安装好了承载页面的Nginx服务器和存储数据的MySQL数据库，但是我们还是需要一些东西来串接这两个东西并且生成动态界面。这样我们就可以使用PHP来完成这个任务。

因为Nginx和其他服务器不同，其并不包含原生的PHP处理模块，所以我们需要安装`php5-fpm`（fastCGI process manager）。我们会指定Nginx将PHP请求给这个软件用于处理。

我们可以安装这个模块并且还需要一个安装一个能够让PHP和我们后台数据库交互的包。这次安装会放入所有必要的PHP核心文件。你需要键入：

<pre class="lang:sh decode:true ">sudo apt-get install php5-fpm php5-mysql</pre>

## 配置PHP处理模块

现在我们已经安装了PHP，但是我们还是要做一些细微的调整来让我们的安装更为安全。

使用root权限来打开`php5-fpm`的配置文件：

<pre class="lang:sh decode:true">sudo vim /etc/php5/fpm/php.ini</pre>

在这个文件中，我们找到第一个参数`cgi.fix_pathinfo`，这个被一个`;`所注释掉，并且默认设置为1。

这个是一个非常危险的设定，因为其告诉PHP对于那些没有办法完全匹配的请求执行最为接近的文件。这样就可能使得用户能够执行一些他们并不能被允许执行的脚本。

我们就需要关闭这个设定：

<pre class="lang:sh decode:true ">cgi.fix_pathinfo=0</pre>

保存这个文件，并且完成设定。

现在，我们就需要重启我们的PHP处理器：

<pre class="lang:sh decode:true ">sudo service php5-fpm restart</pre>

这样我们的设定就会应用了。

# 配置Nginx使用我们的PHP处理器

现在，我们啥都安装好了，现在我们唯一要做的就是配置Nginx来使用我们的PHP来处理动态界面。

我们需要在服务器层次上配置。如果我们想要Nginx默认的话，只需要这样：

<pre class="lang:sh decode:true ">sudo vim /etc/nginx/sites-available/default</pre>

移除掉注释之后，整个文件就会像这样：

<pre class="lang:default decode:true ">server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    root /usr/share/nginx/html;
    index index.html index.htm;

    server_name localhost;

    location / {
        try_files $uri $uri/ =404;
    }
}</pre>

当然，我们需要为我们的网站做一些细微的调整：

*   首先，我们需要添加一个`index.php`的选项来置于我们索引页。这样当处理一些针对目录的请求的时候，就会自动寻找这个目录下的`index.php`文件来加载动态页面。
*   我们同样需要修改server_name来指出我们服务器的域名或者是IP地址
*   事实上，一些配置文件有一些被注释掉的定义处理错误行为的函数，我们需要消掉这些注释，以便于我们能够支持这些行为。
*   对于每一个PHP的请求，我们需要消掉其他的部分的注释。并且我们还需要添加`add_files`来使得我们的Nginx不会向PHP处理器传递太多的错误请求。

所以说，现在我们要变成这样（注意高亮）

<pre class="lang:default mark:6,8,14-28 decode:true ">server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    root /usr/share/nginx/html;
    index index.php index.html index.htm;

    server_name server_domain_name_or_IP;

    location / {
        try_files $uri $uri/ =404;
    }

    error_page 404 /404.html;
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /usr/share/nginx/html;
    }

    location ~ \.php$ {
        try_files $uri =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass unix:/var/run/php5-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}</pre>

当修改好了之后，你就可以保存文件了。

然后重启Nginx服务器：

<pre class="lang:sh decode:true ">sudo service nginx restart</pre>

# 创建一个PHP文件来测试配置

你的LEMP环境就这样被配置好了，但是我们还是要测试来确保Nginx能够正确的处理`.php`文件。

就上面所述，我们可以直接在文件夹中创建一个PHP文件。打开一个名为info.php的新文件。

<pre class="lang:sh decode:true ">sudo vim /usr/share/nginx/html/info.php</pre>

我们可以把下面的内容键入到文件之中，这个有效的PHP代码就能够反映我们服务器的一些情况。

<pre class="lang:php decode:true ">&lt;?php
phpinfo();
?&gt;</pre>

保存并且关闭文件。

现在你可以在浏览器中访问这个界面：

<pre class="lang:default decode:true ">http://server_domain_name_or_IP/info.php</pre>

这样你就可以看见一个被PHP创建的反映你情况的界面。

![php_info](http://kidozh.com/wp-content/uploads/2016/10/php_info.png)

如果你看见了一个像这样的页面，那么你的Nginx的PHP环境就配置完毕了。

接着，为了防止我们信息的泄露，删除这个文件就可以了。

<pre class="lang:sh decode:true ">sudo rm /usr/share/nginx/html/info.php</pre>

&nbsp;