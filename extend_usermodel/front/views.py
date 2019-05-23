from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django import views
# Create your views here.

class IndexView(views.View):
    def get(self,request):
        # Person.objects.create_superuser(email='1417766861@qq.com',username='tanyajuan',password='111111')
        print(Person.get_blacklist())
        return HttpResponse("create success")


