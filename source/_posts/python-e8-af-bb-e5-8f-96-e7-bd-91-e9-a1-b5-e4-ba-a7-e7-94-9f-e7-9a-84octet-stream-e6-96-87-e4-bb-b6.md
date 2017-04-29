---
title: python读取网页产生的octet-stream文件
tags:
  - Python
  - Vjudge
  - 爬虫
  - 网页
id: 1342
categories:
  - Python
date: 2016-07-30 00:36:12
---

# 前言

在爬取Vjudge的导出代码的时候，之前我们采用的是纯正则一个个抓取，速度很慢，当时Vjudge官方向我们提供了一种解决方法就是从URL中获得比赛源代码。

# 获得验证

众所周知，Vjudge获取比赛源代码需要登陆拉题人的账号密码，所以我使用了`Request`这个库来处理含有cookie的请求。所以首先需要模拟登陆这个过程：
<pre class="lang:python decode:true ">def login(self,username=None,password=None):

        #username = raw_input('Your username : ')
        #password = raw_input('Your password : ')
        #username = 'ArrowLLL'
        #password = 'lll1314'
        VJheaders = {
            'Host':'acm.hust.edu.cn',
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'en-US,en;q=0.5',
            'Accept-Encoding':'deflate',
            #'Cookie':'ga=GA1.3.1416134436.1469179876',
        }

        postData = {
            'username':username,
            'password':password
        }

        postData = urllib.urlencode(postData)
        print postData
        req = urllib2.Request(
            #url = 'http://acm.hust.edu.cn/vjudge/contest/fetchStatus.action?cid=88638',
            url='http://acm.hust.edu.cn/vjudge/user/login',
            headers=VJheaders,
            data=postData
        )
        res = self.opener.open(req).read()
        print res
        if res == '"success"':
            return True
        else:
            return False</pre>

# 获得流

下一步是爬虫中常见的，使用`opener.open`来访问这个URL并且获得结果，需要注意的是，这个过程需要带一个合适的`header`。

接着我从浏览器中发现其`Content-Type`为`application/octet-stream`，而`request`返回的数据中`fp`正是`CStringIO`类型，所以我们需要通过这个数据结构来获得我们需要的文件。
<pre class="lang:default decode:true ">def getExportedSourceCode(self,cid='121125'):
        VJheaders = {
            'Host':'acm.hust.edu.cn',
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'en-US,en;q=0.5',
            'Accept-Encoding':'deflate',
            #'Cookie':'ga=GA1.3.1416134436.1469179876',
        }
        exportUrl ='http://acm.hust.edu.cn/vjudge/contest/exportSource/%s'%cid
        tarReq= urllib2.Request(
            #url = 'http://acm.hust.edu.cn/vjudge/contest/fetchStatus.action?cid=88638',
            url=exportUrl,
            headers=VJheaders,
            #data=postData
        )
        res = self.opener.open(tarReq)
        f = cStringIO.StringIO(res.read())
        #f.read()
        now = datetime.datetime.now()
        tarName ='%s%s.zip' %(now.strftime('%Y-%m-%d'),cid)
        #print '#',res.fp,res.code
        with open(tarName,'wb') as tarFile:
            tarFile.write(f.read())
        print 'TAR File has been Downloaded..'</pre>

这样就能够正确的把导出的zip文件存储到本地磁盘之中了。