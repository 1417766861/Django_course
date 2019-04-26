#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/26 11:30
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

context = {
    'users':
        [{
        'name':'donghao',
        'age':20
        },
        {
            'name':'tanyajuan',
            'age':21
        },
        {
            'name':'xxx',
            'age':32
        }],
    'person':{
        'money':20,
        'gender':'男',
    },
    'comments': [
        # {
        #     'user':'donghoa',
        #     'content':'文章真好'
        # },
        # {
        #     'user':'xxx',
        #     'content':'666'
        # }
    ],
    'heros':[
        '鲁班七号',
        '赵云'
    ],
    'books': [
        {
            'id':'djlsfj',
            'name':'三国演义'
        },
        {
            'id':'jxcovaj',
            'name':'西游记'
        }
    ]
}

def index(request):
    content = loader.render_to_string('index.html',context=context)
    #return render(request,'index.html')
    return HttpResponse(content)


def detailpage(request,book_id):
    print(book_id)
    content = 'bookid is %s'%book_id
    return HttpResponse(content)


def login(request):
    next = request.GET.get('next')
    print(next)
    a = request
    return HttpResponse('this is login')