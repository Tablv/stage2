#coding:utf-8
"""workserver URL Configuration

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
from django.http import HttpResponse

def return_index(request):
    rehtml=open(u'workserver/../client/index.html','r').read()
    return HttpResponse(content=rehtml,content_type='text/html',status=200)

#获取json数据进行判断
import json
arr = []
def return_result(request):
    jdata = json.loads(request.body)
    if jdata["psele"]:
        #存储json文件
        #通过照片url进行判断,是否是同一件商品
        #如果是同一件商品,则数量加减
        if arr != []:
            index = 0
            i_json = ''
            for i in range(len(arr)):
                i_json=json.loads(arr[i]);
                if jdata['pimg'] ==i_json['pimg']:
                    #该商品已经存在
                    index = i
                    i_json['pcount'] = int(i_json['pcount'])+int(jdata['pcount'])
                else:
                    #不存在该商品
                    jdata = json.dumps(jdata)
                    arr.append(jdata)
            arr[index] = json.dumps(i_json)
        else:
            jdata = json.dumps(jdata)
            arr.append(jdata)
        return HttpResponse(content='true')
    else:
        return HttpResponse(content='false')

def return_show(requst):
    rehtml = open('show.html','r').read()
    return HttpResponse(content=rehtml,content_type='text/html',status=200)

def return_show_arr(request):
    #对存储的内容进行拼接
    str = ''
    for i in arr:
        str+=i+",,"
    return HttpResponse(content=str);

def return_first(requst):
    rehtml = open('first.html','r').read()
    return HttpResponse(content=rehtml,content_type='text/html',status=200)


def return_json(requst):
    rejson = open('commodity_db.json','r');
    return HttpResponse(content=rejson,content_type='application/json',status=200)


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^first.html$', return_first),
    url(r'^index.html$', return_index),
    url(r'^result.info$', return_result),
    url(r'^show.html$', return_show),
    url(r'^show_arr.info$', return_show_arr),
    url(r'^json_db.info$', return_json)
]
