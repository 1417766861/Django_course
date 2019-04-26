"""revese_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse
from django.shortcuts import redirect,reverse

def index(request):
    username = request.GET.get('username')
    print(username)
    if username:
        return HttpResponse('this is index')
    else:
        #return redirect(reverse('login'))
        #参数方式
        #return redirect(reverse('detail',kwargs={'article_id':2}))
        #查询字符串方式
        redirect_url = reverse('detail',kwargs={'article_id':123})+'?next=hahaha'
        return redirect(redirect_url)

def login(request):
    return HttpResponse('this is login page')

def article_detail(request,article_id):
    return HttpResponse('article detail')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', index),
    path('login/', login,name='login'),
    path('detail/<article_id>', article_detail,name='detail'),
]
