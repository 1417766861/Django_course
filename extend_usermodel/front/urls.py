#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/23 22:23

from django.urls import path
from . import views
urlpatterns = [
    path("",views.IndexView.as_view()),
    path("one/",views.OneVIew),
    path("inherit/",views.inherit_view),
]
