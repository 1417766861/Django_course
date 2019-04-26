#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/26 20:19
from django.http import HttpResponse
from django.template import defaultfilters
from django.shortcuts import render
from datetime import datetime

def index(request):
    #hello = 'this is hello'
    now = datetime.now()
    print(now)
    context = {
        'list1':['book1','book2'],
        'list2':['book3','book4'],
        'hello':'hello world',
        'now': now,
        'detailword':'',
        'word':'hello WORLD',
        'randomlist':[1,2,3,4,5,6,7,8],
        'content':"""<h1>this is index</h1>
        <button onclick="alert('hello world')">click me</button>,
""",
        'text':['haha','xixi','hehe','heihei','gaga'],
        'contenttext':'Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的。本章节我们将详细介绍Python的面向对象编程。'
    }
    return render(request,'index.html',context=context)
"""
def add(value, arg):
    '''Add the arg to the value.'''
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''
            
            
            
def cut(value, arg):
    "Remove all values of arg from the given string."
    safe = isinstance(value, SafeData)
    value = value.replace(arg, '')
    if safe and arg != ';':
        return mark_safe(value)
    return value
"""



