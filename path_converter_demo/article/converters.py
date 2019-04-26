#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/26 11:00
from django.urls import converters,register_converter


class CategoryConverter:
    regex = '\w+|(\w+\+\w+)+'

    def to_python(self, value):
        print('to_python中',value)
        tags = value.split('+')
        return str(tags)

    def to_url(self, value):
        print('to_url中',value)
        return str(value)


register_converter(CategoryConverter, 'mycategory')