#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/24 15:41
from .models import Article
from django.http import HttpResponse
from django import views
from django.views.generic import ListView

def add_article(request):
    articles = []
    for x in range(100):
        article = Article(title='标题 %s'%x,content = "内容 %s"%x)
        articles.append(article)
    Article.objects.bulk_create(articles) #一次性插入。传递一个列表
    return HttpResponse('添加成功')


class ArticleListView(ListView):
    model = Article #模型
    template_name = 'article_list.html' #模板名称
    paginate_by = 10 #每一页展示多少页
    ordering = "create_time"  #排序
    context_object_name = 'articles' #在模板中的变量
    #page_kwarg = 'p' 更换默认翻页传递的page参数

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        print(context)
        #context['xxx'] = 'xxx' #添加额外的键值对，传到模板中
        """
        paginator: 分页
        page_obj：当前这一页参数
        is_paginated: True
        object_list: 对象名字
        view：视图名字
        """


        """
        Paginator常用属性和方法：
            count：总共有多少条数据。
            num_pages：总共有多少页。
            page_range：页面的区间。比如有三页，那么就range(1,4)。
        Page常用属性和方法：
            has_next：是否还有下一页。
            has_previous：是否还有上一页。
            next_page_number：下一页的页码。
            previous_page_number：上一页的页码。
            number：当前页。
            start_index：当前这一页的第一条数据的索引值。
            end_index：当前这一页的最后一条数据的索引值。
        """
        return context

   # def get_queryset(self):
        # return Article.objects.all() #默认返回全部
      #  return Article.objects.filter(id__lte=9)



class DetailView(views.View):
    def get(self,request,book_id):
        text = '获取的book_id 是 %s'%book_id
        print(request.GET['page'])
        return HttpResponse(text)