from distutils.text_file import TextFile
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=20,default='')
    author=models.CharField(max_length=20,default='')
    price=models.IntegerField(default='')
    origin_price=models.IntegerField(default='')
    seller=models.CharField(max_length=20,default='')
    sell_date=models.DateTimeField(auto_now=True)
    content=models.TextField(max_length=100,default='')
    def __str__(self):
        return self.title
