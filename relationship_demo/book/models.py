from django.db import models

# Create your models here.

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    #反向引用 articles
    author = models.ForeignKey("front.FrontUser",on_delete=models.CASCADE,related_name='articles')

    class Meta:
        db_table = 'article'

    def __str__(self):
        return '<Article %s> %s'%(self.id,self.title)



class Tag(models.Model):
    name = models.CharField(max_length=100)

    articles = models.ManyToManyField("Article",related_name='tags')


