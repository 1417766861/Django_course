#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/11 14:45

from rest_framework import serializers
from .models import Article,TagModel
from rest_framework.fields import empty

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = ("id",'name')

class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    # tags = TagSerializer(many=True)
    class Meta:
        model = Article
        fields = ("id","content","create_time","tags")

    def save(self, **kwargs):
        article = super(ArticleSerializer, self).save(**kwargs)
        tags = self.initial_data.get("tags",None)
        if tags:
            try:
                for tag in eval(tags):
                    article.tags.add(TagModel.objects.get_or_create(name=tag))
                article.save()
            except Exception:
                pass





