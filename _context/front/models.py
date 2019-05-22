from django.db import models

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return 'id: %s  <username %s>'%(self.id,self.username)

