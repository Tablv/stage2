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
from django.http import HttpResponse
# from django.contrib import admin
#1.做一个页面,从页面上采集数据(玩家信息-姓名,id,积分)
#姓名自己输入,id自动分配,积分为0
#2.采集数据之后,可以提交数据
#按'开始游戏'按钮  提交数据给服务端
#3.服务端拿到数据后,根据玩家积分判定是否给玩家发牌
#4.发完牌之后,把所有玩家手牌信息给客服端
#5.客户端拿到手牌信息后,局部刷新页面,最终呈现多个玩家和手牌的效果


#获取用户信息
def return_user(request):
    rehtml=open('getUser.html','r').read()
    return HttpResponse(content=rehtml,content_type='text/html',status=200)
#存数据
user = []
#客户端获取的信息,发送给服务端
import json
def get_user(request):
    rejson = json.loads(request.body);
    user.append(request.body)
    #如果积分满足条件
    if rejson["ufen"] != 0:
        return HttpResponse(content=request, content_type="appliction/json", status=200)
    else:
        return HttpResponse(content='false', content_type="appliction/json", status=200)

def select(request):
    rehtml = open('index.html','r').read();
    return HttpResponse(content=rehtml, content_type="text/html", status=200)
#展示采集的信息
def show_user(request):
    if request.method == 'POST':
        return HttpResponse(content=user[0], content_type='text/html', status=200)
    if request.method == 'GET':
        rehtml = open('showuser.html','r').read();
        return HttpResponse(content=rehtml,content_type='text/html',status=200)
#获取三张扑克
def get_cards(request):
    result = request.POST('result')
    if (request.POST('result') == 'action'):
        return HttpResponse(content=user, content_type='text/html', status=200)
    return HttpResponse(content='获取成功',content_type='text/html',status=200)

urlpatterns = [
    url(r'^user.html$', return_user),
    url(r'^get_user.info$', get_user),
    url(r'^index.html$', select),
    url(r'^show_user.html$', show_user),
    url(r'^get_cards.html$', get_cards)
]
