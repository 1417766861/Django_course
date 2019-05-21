#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/21 14:26
from django.urls import re_path,path
from .views import cookie_view,mylist,cms_view,clear,\
session_view

urlpatterns = [
    # re_path(r"^$",cookie_view),
    # path("list/",mylist),
    # path("cms/",cms_view),
    # path("clear/",clear),
    path("",session_view)
]