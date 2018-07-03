---
title: Nginx对于Tornado的配置
tags:
  - HTTPS
  - Nginx
  - tornado
id: 1414
categories:
  - Python
  - 网页
date: 2016-11-27 23:38:23
---

# 前言

最近一直被轰炸HTTPS的好处，于是咬咬牙把[lab.npuacm.info](https://lab.npuacm.info)加了个SSL。下面我就简单的说一下步骤。

# 获得SSL证书

对于SSL证书，我们可以在下面这些网站获得：

1.  [Let's encrypt](https://letsencrypt.org/)
2.  [StartSSL](https://www.startssl.com/)
3.  腾讯云提供的[SSL](https://www.qcloud.com/product/ssl.html)证书

前面几种网上案例很多，我就不多说了，需要注意的是第一和第二个都是需要Shell权限的，所以如果你没有权限的话，那就需要联系一下你的server提供商了。

# 配置Nginx服务器

网上主要可以配置Nginx和Tornado主程序两种，不过我还是建议各位dalao直接去配置Nginx，毕竟耐艹，而且对于静态文件而言，还需要Nginx来处理。

首先，我的思路是，需要对原来的HTTP访问全部转发到HTTPS上，所以，我们可以在Nginx中配置这一项。

```default
server {
    listen 80;
    server_name example.com;

    rewrite /(.*) https://$http_host/$1 redirect;
}
```


然后就要对HTTPS进行配置

```default
server {
    listen 443;
    ssl on;
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/cert.key;

    default_type application/octet-stream;

    location /static/ {
        root /var/www/static;
        if ($query_string) {
            expires max;
        }
    }

    location = /favicon.ico {
        rewrite (.*) /static/favicon.ico;
    }

    location / {
        proxy_pass_header Server;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_pass http://tornadoes;
    }
}
```


但是这样明显不够，因为我的tornado中使用了Websocket技术，这里就不能使用`ws://`协议而应该是`wss://`了，所以我们需要告诉Nginx开启Websocket服务。

所以最终的代码应该是

```default
upstream tornados{
    server 127.0.0.1:8003;
    server 127.0.0.1:8001;
    server 127.0.0.1:8002;
}
proxy_next_upstream error;
server {
    listen  80;
    server_name lab.npuacm.info;

    # rewrite
    rewrite /(.*) https://$http_host/$1 redirect;
}
server{
    listen 443;
    ssl on;
    server_name lab.npuacm.info;

    ssl_certificate your_public_key.crt;
    ssl_certificate_key your_key.key;

    default_type application/octet-stream;

	# Nginx处理这个问题
    location /static/ {
        root /home/ubuntu/npuacmLab;
        if ($query_string){
            expires 24h;
        }
    }
    location / {
        proxy_pass_header Server;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_pass http://tornados;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}


```


自然，如果你并不想配置ngnix的话，你可以直接在本地开启HTTPS服务。

```python
    http_server = tornado.httpserver.HTTPServer(app
        ssl_options={
        "certfile": os.path.join(os.path.abspath("SSL"), "public_key.crt"),
        "keyfile": os.path.join(os.path.abspath("SSL"), "private_key.key"),
    }
    )
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
```


这样本地调试的时候，你就可以直接输入HTTPS调试了，同样的Websocket也可以直接使用`wss://`协议了。

# 后记

被国内运营商劫持的满屏幕都是充话费的。。。也是醉了。