from django.shortcuts import render

# Create your views here.
"""
其实模型名字.objects是一个django.db.models.manager.Manager对象，而Manager这个类是一个“空壳”的类，
他本身是没有任何的属性和方法的。他的方法全部都是通过Python动态添加的方式，从QuerySet类中拷贝过来的
"""
from django.db.models.manager import  Manager


"""
返回新的QuerySet的方法：
filter：将满足条件的数据提取出来，返回一个新的QuerySet。具体的filter可以提供什么条件查询

exclude：排除满足条件的数据，返回一个新的QuerySet。示例代码如下：
Article.objects.exclude(title__contains='hello')
以上代码的意思是提取那些标题不包含hello的图书。

annotate：给QuerySet中的每个对象都添加一个使用查询表达式（聚合函数、F表达式、Q表达式、Func表达式等）的新字段。示例代码如下：

 articles = Article.objects.annotate(author_name=F("author__name"))
以上代码将在每个对象中都添加一个author__name的字段，用来显示这个文章的作者的年龄。


order_by：指定将查询的结果根据某个字段进行排序。如果要倒叙排序，那么可以在这个字段的前面加一个负号


values：用来指定在提取数据出来，需要提取哪些字段。默认情况下会把表中所有的字段全部都提取出来，可以使用values来进行指定，并且使用了values方法后，提取出的QuerySet中的数据类型不是模型，而是在values方法中指定的字段和值形成的字典：

 articles = Article.objects.values("title",'content')
 

values_list：类似于values。只不过返回的QuerySet中，存储的不是字典，而是元组。示例代码如下：

 articles = Article.objects.values_list("id","title")
 print(articles)
 
 
 all：获取这个ORM模型的QuerySet对象
 
 
 
 select_related：在提取某个模型的数据的同时，也提前将相关联的数据提取出来。比如提取文章数据，可以使用select_related将author信息提取出来，以后再次使用article.author的时候就不需要再次去访问数据库了。可以减少数据库查询的次数。示例代码如下：

 article = Article.objects.get(pk=1)
 >> article.author # 重新执行一次查询语句
 article = Article.objects.select_related("author").get(pk=2)
 >> article.author # 不需要重新执行查询语句了
selected_related只能用在一对多或者一对一中，不能用在多对多或者多对一中。比如可以提前获取文章的作者，但是不能通过作者获取这个作者的文章，或者是通过某篇文章获取这个文章所有的标签

prefetch_related：这个方法和select_related非常的类似，就是在访问多个表中的数据的时候，减少查询的次数。这个方法是为了解决多对一和多对多的关系的查询问题。比如要获取标题中带有hello字符串的文章以及他的所有标签，示例代码如下：

 from django.db import connection
 articles = Article.objects.prefetch_related("tag_set").filter(title__contains='hello')
 print(articles.query) # 通过这条命令查看在底层的SQL语句
 for article in articles:
     print("title:",article.title)
     print(article.tag_set.all())
     
     
bulk_create：一次性创建多个数据。示例代码如下：

Tag.objects.bulk_create([
    Tag(name='111'),
    Tag(name='222'),
])


count：获取提取的数据的个数。如果想要知道总共有多少条数据，那么建议使用count，而不是使用len(articles)这种。因为count在底层是使用select count(*)来实现的，这种方式比使用len函数更加的高效。

first和last：返回QuerySet中的第一条和最后一条数据。

aggregate：使用聚合函数。

exists：判断某个条件的数据是否存在

distinct：去除掉那些重复的数据


update：执行更新操作，在SQL底层走的也是update命令


delete：删除所有满足条件的数据。删除数据的时候，要注意on_delete指定的处理方式。

切片操作：有时候我们查找数据，有可能只需要其中的一部分

get_or_create：根据某个条件进行查找，如果找到了那么就返回这条数据，如果没有查找到，那么就创建一个


create：创建一条数据，并且保存到数据库中。这个方法相当于先用指定的模型创建一个对象，然后再调用这个对象的save方法。示例代码如下：

article = Article(title='abc')
article.save()

# 下面这行代码相当于以上两行代码
article = Article.objects.create(title='abc')


only：跟defer类似，只不过defer是过滤掉指定的字段，而only是只提取指定的字段。

get：获取满足条件的数据。这个函数只能返回一条数据，并且如果给的条件有多条数据，那么这个方法会抛出MultipleObjectsReturned错误，如果给的条件没有任何数据，那么就会抛出DoesNotExit错误。所以这个方法在获取数据的只能，只能有且只有一条


defer：在一些表中，可能存在很多的字段，但是一些字段的数据量可能是比较庞大的，而此时你又不需要，比如我们在获取文章列表的时候，文章的内容我们是不需要的，因此这时候我们就可以使用defer来过滤掉一些字段。这个字段跟values有点类似，只不过defer返回的不是字典，而是模型。示例代码如下：

articles = list(Article.objects.defer("title"))
for sql in connection.queries:
    print('='*30)
    print(sql)
在看以上代码的sql语句，你就可以看到，查找文章的字段，除了title，其他字段都查找出来了。当然，你也可以使用article.title来获取这个文章的标题，但是会重新执行一个查询的语句。示例代码如下：

articles = list(Article.objects.defer("title"))
for article in articles:
    # 因为在上面提取的时候过滤了title
    # 这个地方重新获取title，将重新向数据库中进行一次查找操作
    print(article.title)
for sql in connection.queries:
    print('='*30)
    print(sql)
defer虽然能过滤字段，但是有些字段是不能过滤的，比如id，即使你过滤了，也会提取出来。


"""
