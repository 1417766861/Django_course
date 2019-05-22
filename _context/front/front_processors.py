#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/22 20:11
from .models import UserModel

def front_processors(request):
    context = {}
    user_id = request.session.get("user_id")
    user = UserModel.objects.filter(pk=user_id).first()
    if user:
        print(user.username)
        context['front_user'] = user
    return context