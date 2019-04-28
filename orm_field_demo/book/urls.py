#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/27 20:48
from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('person/',views.EmailView.as_view()),
    path('author/',views.AuthorView.as_view()),
    path('ordering/',views.OrderingView.as_view()),
]