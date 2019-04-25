#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/24 21:06


from django.urls import path
from .views import FrontIndexView,LoginView

app_name ="front"

urlpatterns = [
    path('',FrontIndexView.as_view(),name='index'),
    path('login/',LoginView.as_view(),name='login')
]