from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import View


# Create your views here.

class FrontIndexView(View):
    def get(self, request):
        username = request.GET.get("username")
        if username:
            return HttpResponse("this is FrontIndexView")
        else:
            return redirect(reverse('front:login'))


class LoginView(View):
    def get(self, request):
        return HttpResponse('this is FrontIndexView login page')