from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import View
# Create your views here.

class CmsIndex(View):
    def get(self,request):
        username = request.GET.get("username")
        if username:
            return HttpResponse("this is CmsIndex")
        else:
            namespace = request.resolver_match.namespace #获取实例命名空间
            return redirect(reverse('%s:login'%namespace))



class CmsLoginView(View):
    def get(self,request):
        return HttpResponse('this is CmsLoginView page')
