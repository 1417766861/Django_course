from django.db import models

# Create your models here.

class TagModel(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'tag'

class Article(models.Model):
    content = models.TextField('内容')
    create_time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("TagModel",related_name="articles")
    class Meta:
        db_table = 'article'



