from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'index.html')

# 为避免static 同名错误渲染
# 解决方式，在static文件夹下创建一个同名app的文件夹，把静态文件放里面。

# 如果有一些静态文件是不和任何app挂钩的。
# 那么可以在settings.py中添加STATICFILES_DIRS，
# 以后DTL就会在这个列表的路径中查找静态文件









