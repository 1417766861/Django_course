from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category
from front.models import FrontUser
# Create your views here.

def index(request):
    article = Article(title='辣条')
    category = Category(name='美食')
    user = FrontUser(username='donghao')
    category.save()
    user.save()
    article.category = category
    article.author = user
    article.save()
    return HttpResponse('success')

def delete(request):
    category = Category.objects.first()
    print(category)
    category.delete()
    return HttpResponse("delete success")
