from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import ArticleModel,Person,Author

class IndexView(View):
    def get(self,request):
        # article = ArticleModel(name='三国演义')
        # article.save()
        article = ArticleModel.objects.get(pk=2)
        create_time = article.create_time
        print(create_time)
        # return HttpResponse('operaion success')
        return render(request,'index.html',context={'create_time':create_time})

class EmailView(View):
    def get(self,request):
        person = Person(email='123')
        person.save()
        return HttpResponse('操作成功')


class AuthorView(View):
    def get(self,request):
        #author = Author(username='') #没有传递，设置一个空字符串。null=True 时，设置为null
        #author.save()

        author = Author(username='1',phone='13262059002')
        #(1062, "Duplicate entry '13262059002' for key 'phone'")  不可重复
        author.save()
        return HttpResponse('操作成功')

class OrderingView(View):
    def get(self,request):
        books = ArticleModel.objects.all()
        print(books)
        return HttpResponse('操作成功')
