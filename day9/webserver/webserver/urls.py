# -*- coding:utf-8 -*-
"""webserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin
from django.http import HttpResponse;
def return_str(request):
    return HttpResponse('你好')

# print(html.readlines())
# open函数,打开一个文件并读写里面的内容
# 对于文件的分类大致有两种,一种叫文本文件,一种二进制文件
def return_html(requese):
    return HttpResponse(open(u'webserver/../client.html','r'))

def return_jisuan(request):
    return HttpResponse(open(u"webserver/../简单的计算器.html",'r'))

def return_guanggo(request):
    return HttpResponse(open(u"webserver/../定时器广告.html",'r'))
def return_img(request):
    #Http响应数据,默认格式是text/html.就是文本模式,即字符串
    #图片格式是image/jpg
    # HttpResponse有三个参数,content表示响应数据,content_type表示数据格式,status http响应状态
    data = open(u"webserver/../suolong.jpg",'rb').read()
    return HttpResponse(content=data,content_type='image/jpg',status=200)

def return_zhajinhua(request):
    data = open(u'webserver/课堂-炸金花.html','r').read()
    return HttpResponse(data)
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^str$',return_str),
    url(r'^client$',return_html),
    url(r'^jisuan$',return_jisuan),
    url(r'^guangao$',return_guanggo),
    url(r'^suolong.jpg$',return_img),
    url(r'^zhajinhua$', return_zhajinhua)
]

