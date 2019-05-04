# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    tags = models.ManyToManyField("Tag",db_table='article_tag') #更改关联,指定中间表
    class Meta:
        #managed = Trur #django不会对模型进行管理
        db_table = 'article'


# class ArticleTag(models.Model):
#     article = models.ForeignKey(Article, models.DO_NOTHING, primary_key=True)
#     tag = models.ForeignKey('Tag', models.DO_NOTHING)
#
#     class Meta:
#         #managed = False
#         db_table = 'article_tag'
#         unique_together = (('article', 'tag'),)


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'tag'


class User(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    age = models.SmallIntegerField(null=True)

    class Meta:
        #managed = False
        db_table = 'user'
