"""mthod_view URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator


def login_required(func):
    def inner(request,*args,**kwargs):
        if request.GET.get("username"):
            return func(request,*args,**kwargs)
        else:
            return HttpResponse("this is login")
    return inner


# class Index(View):
#     def get(self,request):
#         return HttpResponse("this is index")
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         print('dispatch')
#         return super(Index, self).dispatch(request, *args, **kwargs)
#
#     def http_method_not_allowed(self, request, *args, **kwargs):
#         return HttpResponse("method not allowed")

@method_decorator(login_required,name='dispatch') #指定装饰的方法
class Index(View):
    def get(self,request):
        1/0
        return HttpResponse("this is index")

    def dispatch(self, request, *args, **kwargs):
        print('dispatch')
        return super(Index, self).dispatch(request, *args, **kwargs)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("method not allowed")




class About(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['username'] = "donghao"
        return context

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",Index.as_view(),name='index'),
    path("about",About.as_view(),name='about'),
    path("errors/",include("errors.urls",namespace="errors"))
]
