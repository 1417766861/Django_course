from django.shortcuts import render,reverse
from django.http import HttpResponse
# Create your views here.

def article_index(request):
    return HttpResponse("article_index")

def article_list(request,categories):
    print(categories)
    path = reverse('article:articlelist',kwargs={'categories':'python+hahaha'})
    print(path)
    return HttpResponse(categories)


def detail(request,article_id):
   # print(type(article_id))
    return HttpResponse('detail'+str(article_id))


