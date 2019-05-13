from django.shortcuts import render
from .forms import BookForm
from .models import Book
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'GET':
        aritcles = Book.objects.all()
        return render(request,'index.html',context={"aritcles":aritcles})
    else:
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            a = request.FILES
            pass
            Book.objects.create(title=form.cleaned_data.get("title"),cover_url=form.cleaned_data.get("cover_url").name)
            return HttpResponse("ok")
        else:
            print(form.errors.get_json_data())
            return render(request, 'index.html',context={"errors":form.errors})

