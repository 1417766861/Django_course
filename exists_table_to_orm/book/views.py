from django.shortcuts import render
from django.http import HttpResponse
from .models import  User,Article,Tag
from datetime import datetime
# Create your views here.

"""
python manage.py inspectdb > book/models.py
"""
def index(request):
    # user = User(username='donghao',password='111111')
    # user.save()

    #tag = Tag(name='风景')
    #tag.save()
    user = User.objects.first()

    article = Article(title='123')
    user.article_set.add(article,bulk=False)
    return HttpResponse("ok")

