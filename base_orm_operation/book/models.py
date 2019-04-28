from django.db import models

# Create your models here.

class BookModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    price = models.FloatField(default=0)

    def __str__(self):
        return 'Book （%s） <name: %s   price: %s>'%(self.id,self.name,self.price)



