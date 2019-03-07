# coding:utf-8
"""webservice URL Configuration

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
from django.http import HttpResponse
import time

def return_index(request):# request存放http请求携带的数据
    # 带html格式的字符串
    restr='<!DOCTYPE html><html lang="en">'\
        '<head><meta charset="UTF-8">'\
        '<title>Title</title>'\
        '</head><body>'\
        '<h1>你好</h1></body></html>'
    restr2=open("index.html").read()
    return HttpResponse(content=restr2,content_type="text/html",
                        status=200)

def return_login(request):
    restr = open("login.html").read()
    return HttpResponse(content=restr, content_type="text/html",
                        status=200)

def return_valid(request):
    # request存放了所有http请求携带的数据
    # 给不同的http方法有不同的响应
    if request.method=='GET':
        name = request.GET['name']#url携带的参数,会放到request,GET中
        pwd = request.GET['pwd']
        if name=="root" and pwd=="root123":
            time.sleep(2)
            return HttpResponse(content="get验证通过", content_type="text/html",
                                status=200)
        else:
            time.sleep(2);
            return HttpResponse(content="get验证不通过", content_type="text/html",
                                status=500)
    if request.method=='POST':
        name = request.POST['name']  # url携带的参数,会放到request,GET中
        pwd = request.POST['pwd']
        if name == "root" and pwd == "root123":
            time.sleep(2)
            return HttpResponse(content="post验证通过", content_type="text/html",
                                status=200)
        else:
            time.sleep(2);
            return HttpResponse(content="post验证不通过", content_type="text/html",
                                status=500)
#获取xml文件
def return_xml(request):
    rexml = open('hollywood.xml',"r")
    return HttpResponse(content=rexml,content_type='application/xml',status=200)
#获取json文件
def return_json(request):
    rejson = open('hollywood.json','r')
    return HttpResponse(content=rejson,content_type='application/json',status=200)
#解析xml
def return_getxml(request):
    rexml = open('getxml.html','r')
    return HttpResponse(content=rexml,content_type='text/html',status=200)
#解析xml
def return_getjson(request):
    rexml = open('getjson.html','r')
    return HttpResponse(content=rexml,content_type='text/html',status=200)

import json
def accept_json(request):
    #取post传递的消息体数据
    jdata=request.body
    print jdata
    #把客户端发过来的数据转成json
    print json.loads(jdata)["hollywood"][1]["star"]["name"]
    return HttpResponse(content="ok",status=200);
def send_json(request):
    rehtml = open("sendjsontoserver.html",'r').read();
    return HttpResponse(content=rehtml,content_type='text/html',status=200)
urlpatterns = [
    url(r'^index$', return_index),
    url(r'^login.html$', return_login),
    url(r'^valid$', return_valid),
    url(r'^xml$', return_xml),
    url(r'^getxml$', return_getxml),
    url(r'^json$', return_json),
    url(r'^getjson$', return_getjson),
    url(r'^accept_json$',accept_json),
    url(r'^send_json$',send_json)
]
