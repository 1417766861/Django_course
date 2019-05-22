from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import UserModel
from .forms import UserForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

@require_http_methods(['GET','POST'])
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            cleaned_date = form.cleaned_data
            username = cleaned_date.get("username")
            user = UserModel.objects.filter(username=username).first()
            if user and user.password == cleaned_date.get("password"):
                request.session['user_id'] = user.id
                return redirect(reverse('index'))
            else:
                messages.info(request,"账号不存在")
                return render(request, 'login.html')
        else:
            error = form.get_error()
            messages.info(request, error)
            return render(request, 'login.html')


@require_http_methods(['GET','POST'])
def signup(request):
    if request.method == "GET":
        return render(request,'sign.html')
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            cleaned_date = form.cleaned_data
            print('ok')
            UserModel.objects.create(username=cleaned_date.get("username"),password=cleaned_date.get("password"))
            return redirect(reverse('login'))
        else:
            error = form.get_error()
            messages.info(request, error)
            return render(request, 'sign.html')

def blog(request):
    return render(request, 'blog.html')


def video(request):
    return render(request, 'video.html')

def logout(request):
    request.session.flush()
    return redirect(reverse('index'))