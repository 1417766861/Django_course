"""atomic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from book.models import BookModel
from django.db import transaction


def do_something():
    print('事务成功提交')


# @transaction.atomic
def index(request):
    with transaction.atomic():
        # book = BookModel(title='7858883')
        # book.save()
        # book = BookModel.objects.first()
        # book.delete()
        # try:
        colums = {"id":'id','book_title':"title"}
        # 这是一个字典，将查询中字段的名称映射到模型上字段的名称
        # books = BookModel.objects.raw("select id,title from book_bookmodel",translations=colums)[:-1]
        books = BookModel.objects.raw("select * from book_bookmodel",translations=colums)
        for book in books:
            print(book)
        # a = 1/0
        # except:
        #     pass
        # 如果需要执行参数化查询，可以使用以下params
        # 参数raw()：
        #
        # >> > lname = 'Doe'
        # >> > Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
    # transaction.on_commit(do_something)

    #celery任务
    # transaction.on_commit(lambda: some_celery_task.delay('arg1'))
    return HttpResponse("ok")





urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",index,name="index")
]

# from django.db import DatabaseError, transaction
#
# obj = MyModel(active=False)
# obj.active = True
# try:
#     with transaction.atomic():
#         obj.save()
# except DatabaseError:
#     obj.active = False
#
# if obj.active:
#     ...