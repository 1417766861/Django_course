"""WSGIRequest URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
]

"""
WSGIRequest对象
Django在接收到http请求之后，会根据http请求携带的参数以及报文信息创建一个WSGIRequest对象，并且作为视图函数第一个参数传给视图函数。也就是我们经常看到的request参数。在这个对象上我们可以找到客户端上传上来的所有信息。这个对象的完整路径是django.core.handlers.wsgi.WSGIRequest。

WSGIRequest对象常用属性和方法：
WSGIRequest对象常用属性：
WSGIRequest对象上大部分的属性都是只读的。因为这些属性是从客户端上传上来的，没必要做任何的修改。以下将对一些常用的属性进行讲解：

path：请求服务器的完整“路径”，但不包含域名和参数。比如http://www.baidu.com/xxx/yyy/，那么path就是/xxx/yyy/。
method：代表当前请求的http方法。比如是GET还是POST。
GET：一个django.http.request.QueryDict对象。操作起来类似于字典。这个属性中包含了所有以?xxx=xxx的方式上传上来的参数。
POST：也是一个django.http.request.QueryDict对象。这个属性中包含了所有以POST方式上传上来的参数。
FILES：也是一个django.http.request.QueryDict对象。这个属性中包含了所有上传的文件。
COOKIES：一个标准的Python字典，包含所有的cookie，键值对都是字符串类型。
session：一个类似于字典的对象。用来操作服务器的session。
META：存储的客户端发送上来的所有header信息。

CONTENT_LENGTH：请求的正文的长度（是一个字符串）。

CONTENT_TYPE：请求的正文的MIME类型。
HTTP_ACCEPT：响应可接收的Content-Type。
HTTP_ACCEPT_ENCODING：响应可接收的编码。
HTTP_ACCEPT_LANGUAGE： 响应可接收的语言。
HTTP_HOST：客户端发送的HOST值。
HTTP_REFERER：在访问这个页面上一个页面的url。
QUERY_STRING：单个字符串形式的查询字符串（未解析过的形式）。
REMOTE_ADDR：客户端的IP地址。如果服务器使用了nginx做反向代理或者负载均衡，那么这个值返回的是127.0.0.1，这时候可以使用HTTP_X_FORWARDED_FOR来获取，所以获取ip地址的代码片段如下：
  if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
      ip =  request.META['HTTP_X_FORWARDED_FOR']  
  else:  
      ip = request.META['REMOTE_ADDR']
REMOTE_HOST：客户端的主机名。
REQUEST_METHOD：请求方法。一个字符串类似于GET或者POST。
SERVER_NAME：服务器域名。
SERVER_PORT：服务器端口号，是一个字符串类型。
WSGIRequest对象常用方法：
is_secure()：是否是采用https协议。
is_ajax()：是否采用ajax发送的请求。原理就是判断请求头中是否存在X-Requested-With:XMLHttpRequest。
get_host()：服务器的域名。如果在访问的时候还有端口号，那么会加上端口号。比如www.baidu.com:9000。
get_full_path()：返回完整的path。如果有查询字符串，还会加上查询字符串。比如/music/bands/?print=True。
get_raw_uri()：获取请求的完整url。
QueryDict对象：
我们平时用的request.GET和request.POST都是QueryDict对象，这个对象继承自dict，因此用法跟dict相差无几。其中用得比较多的是get方法和getlist方法。

get方法：用来获取指定key的值，如果没有这个key，那么会返回None。
getlist方法：如果浏览器上传上来的key对应的值有多个，那么就需要通过这个方法获取。"""