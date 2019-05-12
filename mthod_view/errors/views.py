from django.shortcuts import render

# Create your views here.
def view_404(request):
    return render(request,'404.html',404)

def view_500(request):
    return render(request,'500.html',500)