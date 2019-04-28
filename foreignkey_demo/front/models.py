from django.db import models

# Create your models here.

class FrontUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100)
    class Meta:
        db_table = 'front_user'
