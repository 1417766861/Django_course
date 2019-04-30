from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Article
# Create your views here.

class Index(View):
    def get(self,request):
        #准确查找
        #article = Article.objects.filter(title__exact='hello world')

        #article1 = Article.objects.filter(title__exact='Abc asdf') #  =
        #windows 上colletction,在linux mysql排序规则是utf-bin那么就是大小写敏感的 大小写不敏感
        """
        所以exact和iexact的区别实际上就是LIKE和=的区别，在大部分collation=utf8_general_ci情况下都是一样的（collation是用来对字符串比较的）。
        """
        #article2 = Article.objects.filter(title__iexact='%bc asd%') #  like
        #print('article1',article1)
        #print('article2',article2)

        """
        contains：大小写敏感，判断某个字段是否包含了某个数"""
        #翻译成的sql语句左右两边是有百分号的，意味着使用的是模糊查询
        # article = Article.objects.filter(title__contains='Hello') #大小写敏感
        # article2 = Article.objects.filter(title__icontains='Hello') #大小写不敏感
        # print('article1', article)
        # print('article2', article2)

        #in  提取那些给定的field的值是否在给定的容器中
        #articles = Article.objects.filter(id__in=[1,2]) 当然也可以传递一个QuerySet对象进去
        #print(type(Article.objects)) #<class 'django.db.models.manager.Manager'>
        #print(articles.query) # query 只能用在query_set对象上，如果通过get获取数据，就不能使用query.get是返回条件的orm模型，而不是query_set

        # gt：
        # 某个field的值要大于给定的值
        #articles = Article.objects.filter(id__gt=0)
        # gte：
        # 类似于gt，是大于等于
        # lt：
        # 类似于gt是小于。
        # lte：
        # 类似于lt，是小于等于。

        # startswith：
        # 判断某个字段的值是否是以某个值开始的。大小写敏感
        # istartswith：
        # 类似于startswith，但是大小写是不敏感的
        # endswith：
        # 判断某个字段的值是否以某个值结束大小写敏感
        # iendswith：
        # 类似于endswith，只不过大小写不敏感

        # range：
        # 判断某个field的值是否在给定的区间中
        # from django.utils.timezone import make_aware
        # from datetime import datetime
        # start_date = make_aware(datetime(year=2019, month=3, day=25))
        # end_date = make_aware(datetime(year=2019, month=4, day=18, hour=16))
        # articles = Article.objects.filter(create_time__range=(start_date,end_date))
        # print(articles)

        from datetime import date
        articles = Article.objects.filter(create_time__date=date(2019, 4, 16))
        print(articles)
        print(articles.query)
        """
        注意，因为默认情况下MySQL的表中是没有存储时区相关的信息的。因此我们需要下载一些时区表的文件，然后添加到Mysql的配置路径中。如果你用的是windows操作系统。那么在http://dev.mysql.com/downloads/timezones.html下载timezone_2018d_posix.zip - POSIX standard。然后将下载下来的所有文件拷贝到C:\ProgramData\MySQL\MySQL Server 5.7\Data\mysql中，如果提示文件名重复，那么选择覆盖即可。
如果用的是linux或者mac系统，那么在命令行中执行以下命令：mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -D mysql -u root -p，然后输入密码，从系统中加载时区文件更新到mysql中
        """

        # year：
        # 根据年份进行查找。示例代码如下：
        #
        # articles = Article.objects.filter(pub_date__year=2018)

        # month：
        # 同year，根据月份进行查找。
        #
        # day：
        # 同year，根据日期进行查找。
        #
        # week_day：
        # Django
        # 1.11
        # 新增的查找方式。同year，根据星期几进行查找。1
        # 表示星期天，7
        # 表示星期六，2 - 6
        # 代表的是星期一到星期五

        # time：
        # 根据时间进行查找。示例代码如下：
        #
        # articles = Article.objects.filter(pub_date__time=datetime.time(12, 12, 12));
        # 以上的代码是获取每一天中12点12分12秒发表的所有文章

        """
        
        isnull：
        根据值是否为空进行查找。示例代码如下：
        
        articles = Article.objects.filter(pub_date__isnull=False)
        以上的代码的意思是获取所有发布日期不为空的文章
        
        
        
        
        
        regex和iregex：
        大小写敏感和大小写不敏感的正则表达式。示例代码如下：
        
        articles = Article.objects.filter(title__regex=r'^hello')
        以上代码的意思是提取所有标题以hello字符串开头的文章。
        将翻译成以下的SQL语句：
        
        select ... where title regexp binary '^hello';
        iregex是大小写不敏感的
        """


        return HttpResponse("success")

from .models import Book,Author
from django.db.models import Avg,Count,Sum
from django.db import connection

class Aggregate_View(View):
    def get(self,request):
        # 平均值 ：{'price__avg': 97.25}
        avg = Book.objects.aggregate(Avg('price'))

        # result = Book.objects.aggregate(my_avg=Avg('price'))
        # print(result) 平均值 ：{'my_avg': 97.25}

        # Count类中，还有另外一个参数叫做distinct，默认是等于False，如果是等于True，那么将去掉那些重复的值。比如要获取作者表中所有的不重复的邮箱总共有多少个，那么可以通过以下代码来实现：
        # result = Author.objects.aggregate(count=Count('email', distinct=True))
        # print(result) #{'count': 4}
        # print(connection.queries)

        # from django.db.models import Max, Min
        # result = Author.objects.aggregate(Max('age'), Min('age')) #{'age__max': 46, 'age__min': 28}
        # print(result)

        # result = Book.objects.annotate(total=Sum("bookorder__price")).values("name", "total")
        # print(result) #<QuerySet [{'name': '三国演义', 'total': 268.0}, {'name': '水浒传', 'total': 187.0}, {'name': '西游记', 'total': None}, {'name': '红楼梦', 'total': None}]>

        return HttpResponse("success")

"""
aggregate和annotate的区别：
aggregate：返回使用聚合函数后的字段和值。

annotate：在原来模型字段的基础之上添加一个使用了聚合函数的字段，并且在使用聚合函数的时候，会使用当前这个模型的主键进行分组（group by）。
比如以上Sum的例子，如果使用的是annotate，那么将在每条图书的数据上都添加一个字段叫做total，计算这本书的销售总额。
而如果使用的是aggregate，那么将求所有图书的销售总额。

aggregate返回单一字段
"""




