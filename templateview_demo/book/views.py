#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/24 15:35
from django.views.generic import TemplateView


class AboutMe(TemplateView):
    template_name =  'about.html'

    def get_context_data(self,**kwargs): #重写 get_context_data函数
        context = {'name':'donghao'}
        return context


