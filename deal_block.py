import os

infoStr = '''
source/_posts/latexlatex-e7-9a-84-e6-a8-a1-e6-9d-bf.md:{% raw %}
source/_posts/latexlatex-e7-9a-84-e6-a8-a1-e6-9d-bf.md:\lstloadlanguages{% Check Dokumentation for further languages ...
source/_posts/latexlatex-e7-9a-84-e6-a8-a1-e6-9d-bf.md:{% endraw %}
source/_posts/djangodjango-e5-bc-80-e5-9d-91-e7-af-87.md:<pre class="lang:default decode:true" title="mysite/news/templates/news/year_archive.html">{% extends "base.html" %}
source/_posts/djangodjango-e5-bc-80-e5-9d-91-e7-af-87.md:{% block title %}Articles for {{ year }}{% endblock %}
source/_posts/djangodjango-e5-bc-80-e5-9d-91-e7-af-87.md:{% block content %}
source/_posts/djangodjango-e5-bc-80-e5-9d-91-e7-af-87.md:{% for article in article_list %}
source/_posts/djangodjango-e5-bc-80-e5-9d-91-e7-af-87.md:{% endfor %}
source/_posts/djangodjango-e5-bc-80-e5-9d-91-e7-af-87.md:{% endblock %}</pre>
source/_posts/djangodjango-e5-bc-80-e5-9d-91-e7-af-87.md:最后，Django的模板系统采用了“继承”的这种概念来丰富其形式，这也是`{% extends "base.html" %}`的意义。他指明了Django首先需要引用base.html中的内容（在被继承的模板中应有一串这样的区块）然后替换就可以了。简而言之，每个模板必须定义好一个相对于其继承模板的一个独一无二的量。
source/_posts/djangodjango-e5-bc-80-e5-9d-91-e7-af-87.md:<pre class="lang:python decode:true" title="mysite/templates/base.html">{% load staticfiles %}
source/_posts/djangodjango-e5-bc-80-e5-9d-91-e7-af-87.md:    &lt;title&gt;{% block title %}{% endblock %}&lt;/title&gt;
source/_posts/djangodjango-e5-bc-80-e5-9d-91-e7-af-87.md:    &lt;img src="{% static "images/sitelogo.png" %}" alt="Logo" /&gt;
source/_posts/djangodjango-e5-bc-80-e5-9d-91-e7-af-87.md:    {% block content %}{% endblock %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-884-ef-bc-89.md:{% if error_message %}&lt;p&gt;&lt;strong&gt;{{ error_message }}&lt;/strong&gt;&lt;/p&gt;{% endif %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-884-ef-bc-89.md:&lt;form action="{% url 'polls:vote' question.id %}" method="post"&gt;
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-884-ef-bc-89.md:{% csrf_token %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-884-ef-bc-89.md:{% for choice in question.choice_set.all %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-884-ef-bc-89.md:{% endfor %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-884-ef-bc-89.md:*   当我们设定表单提交到的地址` {% url 'polls:vote' question.id %}`并且我们也设定了表格提交方式为POST，使用POST这种方法能够很安全的传递数据，而且这个对表格提交的动作会改变服务器上的数据，所以使用POST这种方法是非常合理的方法。
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-884-ef-bc-89.md:*   由于我们已经创建了一个POST的表单，所以我们必须注意CSRF（跨站点欺骗攻击），由于Django使用了一个十分易用的系统来抵御CSRF，所以在表单里面需要给予` {% csrf_token %} `的模板标签
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-884-ef-bc-89.md:{% for choice in question.choice_set.all %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-884-ef-bc-89.md:{% endfor %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-884-ef-bc-89.md:&lt;a href="{% url 'polls:detail' question.id %}"&gt;Vote again?&lt;/a&gt;</pre>
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-886-ef-bc-89.md:<pre class="lang:css decode:true " title="polls/templates/polls/index.html">{% load staticfiles %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-886-ef-bc-89.md:&lt;link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" /&gt;</pre>
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-886-ef-bc-89.md:`{% load staticfiles %}` 从模板文件夹`staticfiles`之中加载了模板标签`{% static %}`，模板标签`{% static %}`将会生成静态文件的绝对URL地址。
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-886-ef-bc-89.md:需要注意的是，在CSS样式表里` {% static %}`并不被静态文件所解析，所以必须要使用相对路径，这样你就能在修改`STATIC_URL`的时候不用去重新修改路径。
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-882-ef-bc-89.md:<pre class="lang:xhtml decode:true ">{% block branding %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-882-ef-bc-89.md:&lt;h1 id="site-name"&gt;&lt;a href="{% url 'admin:index' %}"&gt;Polls Administration&lt;/a&gt;&lt;/h1&gt;
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-882-ef-bc-89.md:{% endblock %}</pre>
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-882-ef-bc-89.md:这个模板系统包含大量的类似于 {% block branding %}和{ { title } }的文本 和{{都是模板之中的语言，当Django渲染admin/base_site.html的时候，这些标记就会被转义最终形成最终的HTML页面。这样Django的模板系统就会被重载了。
source/_posts/e5-9c-a8tornado-e7-9a-84-e6-a8-a1-e6-9d-bf-e4-b8-ad-e4-bd-bf-e7-94-a8-e5-b5-8c-e5-a5-97-e5-be-aa-e7-8e-af.md:只需要把被嵌套循环的变量设置为当前的局部变量就可以了。具体的方法就是使用`<span class="pre">{%</span> <span class="pre">set</span> <span class="pre">*x*</span> <span class="pre">=</span> <span class="pre">*y*</span> `<span class="pre">`%}`来设置一个局部变量</span>
source/_posts/e5-9c-a8tornado-e7-9a-84-e6-a8-a1-e6-9d-bf-e4-b8-ad-e4-bd-bf-e7-94-a8-e5-b5-8c-e5-a5-97-e5-be-aa-e7-8e-af.md:<pre class="lang:default mark:10 decode:true " title="一个简单的处理方法">{% for app,model in modelsList %}
source/_posts/e5-9c-a8tornado-e7-9a-84-e6-a8-a1-e6-9d-bf-e4-b8-ad-e4-bd-bf-e7-94-a8-e5-b5-8c-e5-a5-97-e5-be-aa-e7-8e-af.md:   {% if len(model) == 0 %}
source/_posts/e5-9c-a8tornado-e7-9a-84-e6-a8-a1-e6-9d-bf-e4-b8-ad-e4-bd-bf-e7-94-a8-e5-b5-8c-e5-a5-97-e5-be-aa-e7-8e-af.md:    {% continue %}
source/_posts/e5-9c-a8tornado-e7-9a-84-e6-a8-a1-e6-9d-bf-e4-b8-ad-e4-bd-bf-e7-94-a8-e5-b5-8c-e5-a5-97-e5-be-aa-e7-8e-af.md:    {% end %}
source/_posts/e5-9c-a8tornado-e7-9a-84-e6-a8-a1-e6-9d-bf-e4-b8-ad-e4-bd-bf-e7-94-a8-e5-b5-8c-e5-a5-97-e5-be-aa-e7-8e-af.md:    {% set modelAl = model %}
source/_posts/e5-9c-a8tornado-e7-9a-84-e6-a8-a1-e6-9d-bf-e4-b8-ad-e4-bd-bf-e7-94-a8-e5-b5-8c-e5-a5-97-e5-be-aa-e7-8e-af.md:    {% for name,cls in modelAl %}
source/_posts/e5-9c-a8tornado-e7-9a-84-e6-a8-a1-e6-9d-bf-e4-b8-ad-e4-bd-bf-e7-94-a8-e5-b5-8c-e5-a5-97-e5-be-aa-e7-8e-af.md:    {% end %}
source/_posts/e5-9c-a8tornado-e7-9a-84-e6-a8-a1-e6-9d-bf-e4-b8-ad-e4-bd-bf-e7-94-a8-e5-b5-8c-e5-a5-97-e5-be-aa-e7-8e-af.md:{% end %}</pre>
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-883-ef-bc-89.md:<pre class="lang:xhtml decode:true" title="polls/templates/polls/index.html">{% if latest_question_list %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-883-ef-bc-89.md:    {% for question in latest_question_list %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-883-ef-bc-89.md:    {% endfor %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-883-ef-bc-89.md:{% else %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-883-ef-bc-89.md:{% endif %}</pre>
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-883-ef-bc-89.md:{% for choice in question.choice_set.all %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-883-ef-bc-89.md:{% endfor %}
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-883-ef-bc-89.md:`{% for %}`循环question.choice_set.all会被Python解释为`question.choice_set.all()`，这样会返回一个可以迭代的choice的对象，并且能够被`{% for %}`所迭代。
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-883-ef-bc-89.md: 用这种直接编码URL的方法为标题在于需要频繁的变更URLS地址在不同的模板之中。然而由于你已经在polls.urls模块之中定义了`url()`的名称变量，你可以使用`{% url %}`的方法去除掉对在URL配置过程中特定URL路径的依赖。
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-883-ef-bc-89.md:<pre class="lang:xhtml decode:true ">&lt;li&gt;&lt;a href="{% url 'detail' question.id %}"&gt;{{ question.question_text }}&lt;/a&gt;&lt;/li&gt;</pre>
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-883-ef-bc-89.md:# the 'name' value as called by the {% url %} template tag
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-883-ef-bc-89.md:<pre class="lang:xhtml decode:true " title="polls/templates/polls/index.html">&lt;li&gt;&lt;a href="{% url 'detail' question.id %}"&gt;{{ question.question_text }}&lt;/a&gt;&lt;/li&gt;</pre>
source/_posts/django-e7-bc-96-e5-86-99-e4-bd-a0-e7-9a-84-e7-ac-ac-e4-b8-80-e4-b8-aadjango-e7-a8-8b-e5-ba-8f-ef-bc-883-ef-bc-89.md:<pre class="lang:default decode:true " title="polls/templates/polls/index.html">&lt;li&gt;&lt;a href="{% url 'polls:detail' question.id %}"&gt;{{ question.question_text }}&lt;/a&gt;&lt;/li&gt;</pre>

'''

for everySentence in infoStr.split('\n'):
    filePath = everySentence.split(':')[0]
    fileName =  filePath.split('/')[-1]
    print('rm %s'% fileName)
