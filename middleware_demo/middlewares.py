#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/19 18:44

# def front_user_middleware(get_response):
#     #执行一些初始化代码
#     def middleware(request):
#         print('到达视图函数之前')
#         response = get_response(request)
#         print('到达浏览器之前')
#         return response
#     return middleware


class FrontMiddleware(object):
    def __init__(self,get_response):
        # 执行一些初始化代码
        self.get_response = get_response

    def __call__(self,request, *args, **kwargs):
        print('到达视图函数之前')
        resp = self.get_response(request)
        print('到达浏览器之前')
        return resp


















