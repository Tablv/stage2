#coding:utf-8
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
from django.http import HttpResponse
#读取json文件
def return_json(request):
    rejson = open('hellywood.json','r').read()
    return HttpResponse(content=rejson,content_type='application/json',status=200)
def return_html(request):
    rehtml = open('use_template.html','r').read()
    return HttpResponse(content=rehtml,content_type='text/html',status=200)
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^re_json.html$', return_json),
    url(r'^re_html.html$', return_html)
]
