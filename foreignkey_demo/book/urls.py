#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/28 18:03
from django.urls import path
from .views import index,delete

urlpatterns = [
    path('',index),
    path('delete/',delete),
]