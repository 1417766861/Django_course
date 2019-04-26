#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/26 21:22
from django.template import Library
register = Library()

def myfilter(value):
    """this is my first filter"""
    text = 'this is my first filter %s'%value
    return text

register.filter('myfilter',myfilter)
