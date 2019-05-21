from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware
# Create your views here.

def cookie_view(request):
    resp = HttpResponse("cookie set")
    resp.set_cookie('age',20,
                    max_age=100,
                    expires=make_aware(datetime(year=2019,month=5,day=30,hour=5,minute=5,second=5)
                                       ),
                    ) #path='/cms/'

    # return resp
    # cookie = request.COOKIES.get('username')
    # request.COOKIES.pop('username')
    # print(request.COOKIES)
    return resp

def mylist(request):
    print(request.COOKIES)
    return HttpResponse("this is mylist")

def cms_view(request):
    print(request.COOKIES)
    return HttpResponse("this is cms_view")

def clear(request):
    # request.COOKIES.clear()
    resp = HttpResponse("COOKIES delete")
    resp.delete_cookie('age') #删除cookie
    return resp

"""
key：这个cookie的key。
value：这个cookie的value。
max_age：最长的生命周期。单位是秒。
expires：过期时间。跟max_age是类似的，只不过这个参数需要传递一个具体的日期，比如datetime或者是符合日期格式的字符串。如果同时设置了expires和max_age，那么将会使用expires的值作为过期时间。
path：对域名下哪个路径有效。默认是对域名下所有路径都有效。
domain：针对哪个域名有效。默认是针对主域名下都有效，如果只要针对某个子域名才有效，那么可以设置这个属性.
secure：是否是安全的，如果设置为True，那么只能在https协议下才可用。
httponly：默认是False。如果为True，那么在客户端不能通过JavaScript进行操作。
"""

def session_view(request):
    request.session['username'] = 'donghao'
    request.session['age'] = 20
    # print(request.session.get("username"))
    # print(request.session.get("age"))
    # username = request.session.get("username")
    # print(request.session)
    # request.session.clear() # clear：清除当前这个用户的session数据。
    #request.session.flush() #删除session并且删除在浏览器中存储的session_id，一般在注销的时候用得比较多。
    request.session.set_expiry(-1)   # set_expiry  ：设置过期时间。
    request.session.clear_expired()   # clear_expired  ：clear_expired：清除过期的session。。
    return HttpResponse("session set ok")
"""
session常用的方法如下：

get：用来从session中获取指定值。

pop：从session中删除一个值。

keys：从session中获取所有的键。

items：从session中获取所有的值。

clear：清除当前这个用户的session数据。

flush：删除session并且删除在浏览器中存储的session_id，一般在注销的时候用得比较多。

set_expiry(value)：设置过期时间。

整形：代表秒数，表示多少秒后过期。

0：代表只要浏览器关闭，session就会过期。

None：会使用全局的session配置。在settings.py中可以设置SESSION_COOKIE_AGE来配置全局的过期时间。默认是1209600秒，也就是2周的时间。

clear_expired：清除过期的session。Django并不会清除过期的session，需要定期手动的清理，或者是在终端，使用命令行python manage.py clearsessions来清除过期的session。
"""