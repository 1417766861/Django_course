from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.

def index(request):
    book = Book(name='三国',price=10,content='haha')
    book.save()
    return HttpResponse("ok")
