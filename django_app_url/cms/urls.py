#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/24 21:06


from django.urls import path
from .views import CmsLoginView,CmsIndex

app_name ="cms"

urlpatterns = [
    path('',CmsIndex.as_view(),name='index'),
    path('login/',CmsLoginView.as_view(),name='login')
]