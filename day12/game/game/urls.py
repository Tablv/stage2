#coding:utf-8
"""game URL Configuration

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
#from django.contrib import admin
from django.http import HttpResponse

def return_html(request):
    rehtml = open('game.html','r').read()
    return HttpResponse(content=rehtml,content_type="text/html",status=200)

import json
def return_json(request):
    # 先接受客户端数据
    jdata=json.loads(request.body)
    # 组织需要返回给客户端的json
    if int(jdata["players"][0]["score"]) > 60:#取第一个用户的分数进行判断
        #给玩家一个cards属性
        jdata["players"][0]["cards"]=['club02.jpg','club03.jpg','club04.jpg']
    if int(jdata["players"][1]["score"]) > 60:  # 取第一个用户的分数进行判断
        # 给玩家一个cards属性
        jdata["players"][1]["cards"] = ['diamond02.jpg', 'diamond03.jpg', 'diamond04.jpg']
    resp_data=json.dumps(jdata)
    resp = HttpResponse(content=resp_data,content_type="appliction/json",status=200)
    # 在返回httpresponse之前,加上跨域的标签
    resp['Access-Control-Allow-Origin'] = '*'
    #允许哪些机器访问,* 表示允许所有的不同源的http请求
    return resp

def return_jsonp(request):
    #返回的数据要和请求url\的callback后面数据一致,括号里面是返回的内容
    return HttpResponse("jsonp('hello,client')")

def return_data(request):
    return HttpResponse(u"$ajax收到数据")


def return_jq_jsonp(request):
    return HttpResponse("jsonpFun('jq-jsonp')")
urlpatterns = [
    url(r'^$', return_html),
    url(r'^game.html$',return_html),
    url(r'^recv.info$',return_json),
    url(r'^jsonp$',return_jsonp),
    url(r'^get_data$',return_data),
    url(r'^jq_jsonp$',return_jq_jsonp)
]
