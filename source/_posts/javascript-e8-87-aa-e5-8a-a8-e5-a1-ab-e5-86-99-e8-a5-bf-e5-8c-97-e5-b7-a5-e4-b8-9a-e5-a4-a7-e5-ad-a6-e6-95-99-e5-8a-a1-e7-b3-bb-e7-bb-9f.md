---
title: '[JavaScript]自动填写西北工业大学教务系统'
tags:
  - javascript
  - 爬虫
id: 716
categories:
  - 网页
date: 2015-12-11 16:57:14
---

# 1.背景和代码

学校的教务系统又更新了，然而依旧要填这么多人，有些老师还没来上课（- -金属仨老师我就认识一个）。我参考了一位学长的JS代码（[点我传送](http://blog.tpircsboy.com/tech/jiaowu-judge/)），然后还是模拟了这个过程。但是现在教务系统的后台不知道是数据库原因还是手工设置的原因，不能一次性把所有的数据都POST上去（坑我一下午- -），所以我手动给出了alert（teacherID，lessonID）来手工设置间隔。
<pre class="show-title:false expand:false expand-toggle:false lang:js decode:true ">var table=document.getElementsByClassName("gridtable")[0];var eachline=table.rows;var info="";for(var i=1;i&lt;table.rows.length;i++){var cellinfo=eachline.item(i).cells.item(5).innerHTML;var regex=/[0-9]+/g;var res=cellinfo.match(regex," ");if(1){alert(res[1]+","+res[0])}if(res.length!=2){alert(res[1]);break}var teacherId=res[1];var lessonId=res[0];var http=new XMLHttpRequest;info=info+teacherId+" "+lessonId+";";http.open("POST","http://us.nwpu.edu.cn/eams/evaluateStd!save.action",true);http.setRequestHeader("Content-type","application/x-www-form-urlencoded");http.send("teacherId="+teacherId+"&amp;select6=5&amp;select7=5&amp;select8=5&amp;select1=5&amp;select2=5&amp;select3=5&amp;select4=5&amp;select5=5&amp;evaluateResult.remark=%E5%BE%88%E5%A5%BD%EF%BC%81&amp;semester.id=15&amp;lesson.id="+lessonId+"&amp;teacher.ids="+teacherId)};</pre>

 然后这个是没有压缩过的代码：
<pre class="lang:js decode:true " title="自动填写西工大教务系统">var table= document.getElementsByClassName('gridtable')[0];
//alert(table.rows.length);
var eachline = table.rows;
var info = ""
for (var i=1;i&lt;table.rows.length;i++)
{
	var cellinfo = eachline.item(i).cells.item(5).innerHTML;
	var regex = /[0-9]+/g;
	var res = cellinfo.match(regex," ");
	//alert(res.toString());
	//alert(cellinfo);
	if (1)
	{
		alert(res[1]+','+res[0])
	}
	if (res.length !=2){
		alert(res[1]);
		break;
	}
	var teacherId = res[1];
	var lessonId = res[0];
	var http = new XMLHttpRequest;
	info = info +teacherId + " "+lessonId+";";
    http.open('POST', "http://us.nwpu.edu.cn/eams/evaluateStd!save.action", true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	http.send("teacherId="+teacherId+"&amp;select6=5&amp;select7=5&amp;select8=5&amp;select1=5&amp;select2=5&amp;select3=5&amp;select4=5&amp;select5=5&amp;evaluateResult.remark=%E5%BE%88%E5%A5%BD%EF%BC%81&amp;semester.id=15&amp;lesson.id="+lessonId+"&amp;teacher.ids="+teacherId);

}
</pre>

 这里最终效果会是这样：

[![@HCT3{O$]9A1@L$FHZ(E}A0](/wp-content/uploads/2015/12/@HCT3O9A1@LFHZEA0.png)](/wp-content/uploads/2015/12/@HCT3O9A1@LFHZEA0.png)

嗯就是这样。

# 2.使用方法

首先进入到这里：

[![QQ图片20151211165226](/wp-content/uploads/2015/12/QQ图片20151211165226.png)](/wp-content/uploads/2015/12/QQ图片20151211165226.png)

然后，<span style="color: rgb(76, 76, 76); font-family: Oxygen, 'Helvetica Neue', Arial, sans-serif; font-size: 18px; line-height: 29.7px; background-color: rgb(245, 245, 245);">在浏览器栏输入 </span><span style="box-sizing: inherit; font-family: Oxygen, 'Helvetica Neue', Arial, sans-serif; font-size: 18px; font-weight: 700; vertical-align: baseline; padding: 0px; border: 0px; margin: 0px; outline: 0px; color: rgb(76, 76, 76); line-height: 29.7px; background-color: rgb(245, 245, 245);">_javascript: _</span><span style="color: rgb(76, 76, 76); font-family: Oxygen, 'Helvetica Neue', Arial, sans-serif; font-size: 18px; line-height: 29.7px; background-color: rgb(245, 245, 245);">，然后粘贴入上面的代码，回车就行了</span>

# 3.兼容性

我在Chrome上测试成功了，别的我还没有测试。