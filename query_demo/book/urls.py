#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/28 18:56
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view()),
    path('aggregate/',views.Aggregate_View.as_view()),
    path('f/',views.F_view.as_view()),
]