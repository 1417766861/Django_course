#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/27 20:23
from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view())
]