"""django_restful_framwork URL Configuration

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
from article.models import Article,TagModel
from django.http import HttpResponse
from article.serializers import ArticleSerializer
from django.http import JsonResponse
from django.shortcuts import render


def add(request):
    # TagModel.objects.create(name="美女")
    # TagModel.objects.create(name="美食")
    tag = TagModel.objects.first()
    article = Article.objects.create(content='article1')
    article.tags.add(tag)
    article.save()
    return HttpResponse("ok")

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    else:
        serializer = ArticleSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            print('保存')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



urlpatterns = [
    #path('admin/', admin.site.urls),
    #path("",add,name='add'),
    path("",list,name='list')
]
