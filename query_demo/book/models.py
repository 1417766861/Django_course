from django.db import models

# Create your models here.

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'article'

    def __str__(self):
        return '<Article %s> %s'%(self.id,self.title)



