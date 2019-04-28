from django.shortcuts import render
from django.views  import View
from django.http import HttpResponse
from .models import Article,Tag
from front.models import FrontUser,UserExtension
# Create your views here.

class IndexView(View):
    def get(self,request):
        # user = FrontUser(username='donghao')
        # user.save()
        # article = Article(title='title 1')
        # article.author = user
        # article.save()

        user = FrontUser.objects.first()
        # article = Article(title='title 2')
        # article.author = user
        # article.save()

        #外键关联的数据获取
        # article = user.article_set.first()
        # print(article) <Article 1> title 1

        # articles = user.article_set.all()
        # print(articles) #<QuerySet [<Article: <Article 1> title 1>, <Article: <Article 3> title 2>]>

        # 设置了related_name
        # articles = user.articles.all()
        # print(articles) <QuerySet [<Article: <Article 1> title 1>, <Article: <Article 3> title 2>]>


        #add()方法
        article1 = Article(title='new title1')
        article2 = Article(title='new title2')
        user.articles.add(article1,article2,bulk=False) #

        #bulk = False  添加到数据库中，不用保存
        return HttpResponse('index')


class One_to_one(View):
    def get(self,request):
        user = FrontUser.objects.first()
        # extension = UserExtension(school='nyist')
        # extension.user = user
        # extension.save()

        # extension = UserExtension.objects.first()
        # print(extension.user.username)

        # print(user.userextension) UserExtension object (1)
        print(user.extension) #指定了 related_name = extension

        return HttpResponse("one to one")


class Many_to_many(View):
    def get(self,request):
        # author = FrontUser.objects.first()
        # article = Article(title='成都一日游')
        # article.author = author
        # article.save()
        #
        # tag = Tag(name='美食')
        # tag.save()
        # article.tags.add(tag)

        tag = Tag.objects.first()
        # print(tag.articles.all()) #<QuerySet [<Article: <Article 5> new title1>, <Article: <Article 7> 成都一日游>, <Article: <Article 11> 成都一日游>]>
        article = tag.articles.filter(title="成都一日游")
        print(article)
        return HttpResponse("Many_to_many")
