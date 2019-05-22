#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/22 19:58

from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='index'),
    path("login/",views.login,name='login'),
    path("signup/",views.signup,name='signup'),
    path("logout/",views.logout,name='logout'),
    path("blog/",views.blog,name='blog'),
    path("video/",views.video,name='video'),
]