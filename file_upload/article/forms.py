#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/13 21:52
from django import forms
from .models import Book
from django.core import validators

class BookForm(forms.ModelForm):
    cover_url = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['jpg','jpeg'])])
    class Meta:
        model = Book
        fields = ['title','cover_url']