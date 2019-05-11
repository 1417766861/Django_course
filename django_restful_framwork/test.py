#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/11 16:57
# __time__ = 2019/5/11 11:46
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_restful_framwork.settings")

django.setup()

from article.models import TagModel

name = ["美女","美食","汽车"]
for n in name:
    TagModel.objects.get_or_create(name=n)
