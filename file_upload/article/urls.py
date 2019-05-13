#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/13 21:49
from django.urls import path
from . import views
app_name = "article"
urlpatterns = [
    path("",views.index,name='index')
]