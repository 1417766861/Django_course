#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/24 14:48

from django.http import HttpResponse

def index(request):
    a = request
    print(a)
    return HttpResponse('豆瓣首页')