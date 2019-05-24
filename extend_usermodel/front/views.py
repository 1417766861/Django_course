from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django import views
from django.contrib.auth.models import User
# Create your views here.

class IndexView(views.View):
    def get(self,request):
        # Person.objects.create_superuser(email='1417766861@qq.com',username='tanyajuan',password='111111')
        print(Person.get_blacklist())
        return HttpResponse("create success")



def my_authentication(phone,password):
    user = User.objects.filter(extension__phone=phone).first()
    print(phone,password)
    if user:
        print(user)
        is_correct = user.check_password(password)
        if is_correct:
            return user
        else:
            return None
    else:
        return None

def OneVIew(request):
    # user = User.objects.create_user(username='user3',email='user3@qq.com',password='111111')
    # user.extension.phone = '13262059002'
    # user.save()
    phone = request.GET.get("phone")
    pwd = request.GET.get("pwd")
    user = my_authentication(phone,pwd)
    if user:
        print("验证ok")
    else:
        print('验证失败')
    return HttpResponse("ok")
