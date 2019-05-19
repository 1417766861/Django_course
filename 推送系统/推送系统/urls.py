"""推送系统 URL Configuration
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
import redis
from django.contrib import admin
from django.urls import path
import threading
from django.http import HttpResponse

# def date_add():
#     for x in range(20000):
#         Article.objects.create(
#             title='title,threading %s %s' % (x,threading.Thread.name)
#         )
#

#
import redis,time
pool = redis.ConnectionPool(encoding='utf-8',decode_responses=True)
cache = redis.Redis(connection_pool=pool)

from article.models import AccountAccount
from django.db.models import F

def index(request):
    with cache.pipeline(transaction=True) as p:
        start = time.time()
        # for x in range(100):
        #     p.lpush("user:xx:message", 'message:%s' % x).rpush('user:yy:message','haha%s'%x)
        [p.lpush('account',account.id) for account in AccountAccount.objects.filter(subscribed='0').all()]
        p.execute()
        end = time.time()
        print('耗时%0.2fs' % (end - start))  #耗时 0.25s
    return HttpResponse("ok")




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
