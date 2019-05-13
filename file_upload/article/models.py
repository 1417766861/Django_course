from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    # cover_url = models.FileField(upload_to="files")
    cover_url = models.FileField(upload_to="files")


