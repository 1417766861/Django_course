#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/12 18:22

from django.urls import path
from . import views

app_name = "errors"
urlpatterns = [
    path("404.html",views.view_404,name='404'),
    path("500.html",views.view_500,name='500')
]