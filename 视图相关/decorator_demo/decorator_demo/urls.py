"""decorator_demo URL Configuration

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
from django.urls import path


articles = [
    'article1','article2'
]

from django.shortcuts import render
#from django.views.decorators.http import require_http_methods,require_GET,require_POST,require_safe
from django.http import HttpResponse

def require_http_methods(request_method_list):
    def decorator(func):
        #@wraps(func)
        def inner(request, *args, **kwargs):
            if request.method not in request_method_list:
                return HttpResponse('Method Not Allowed (%s): %s'% (request.method, request.path))
            return func(request, *args, **kwargs)
        return inner
    return decorator

@require_http_methods(['GET','POST'])
def index(request):
    if request.method == 'GET':
        return render(request,'index.html',context={'articles':articles})
    else:
        name = request.POST.get("username",'null')
        print(name)
        return HttpResponse("this is post")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
]


