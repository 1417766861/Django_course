#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/28 18:56
from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('one/',views.One_to_one.as_view()),
    path('many/',views.Many_to_many.as_view()),
]