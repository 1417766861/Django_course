#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/26 10:19
from django.urls import path,re_path
from . import views
app_name = 'article'


urlpatterns = [
    path('',views.article_index,name='index'),
    #path('list/<categories>/',views.article_list,name='list')
    # ():捕获参数，命名的参数P
    #re_path(r'list/(?P<categories>\w+|(\w+\+\w+)+)/',views.article_list),
    path('list/<mycategory:categories>/',views.article_list,name='articlelist'),
    path('detail/<int:article_id>/',views.detail)
]

"""
to_python: 负责url类型的转换
to_url：反转时类型转换成str

class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
"""