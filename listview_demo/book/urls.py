#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/24 15:59

from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('add/',views.add_article,name='add_article'),
    path('list/',views.ArticleListView.as_view(),name='article_list'),
    path('detail/<book_id>/',views.DetailView.as_view(),name='article_list')
]