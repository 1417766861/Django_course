from django.shortcuts import render
from django.views import View
# Create your views here.
from django.http import HttpResponse
from .models import  BookModel

class IndexView(View):
    def get(self,request):
        #添加
        #book = BookModel(name='三国演义',price=20)
       # book = BookModel(name='西游记',price=10)
        #book.save()

        #查询
        # book = BookModel.objects.get(pk=1)
        # print(book)  Book （1） <name: 三国演义   price: 20.0>
        # book = BookModel.objects.filter(name='西游记') #QuerySet
        # print(book)
        # book = BookModel.objects.filter(name='西游记').first()

        #删除数据
        book = BookModel.objects.get(pk=2) #BookModel matching query does not exist.
        # book.delete()

        book.price = 200
        book.save()
        return HttpResponse('operation success')




