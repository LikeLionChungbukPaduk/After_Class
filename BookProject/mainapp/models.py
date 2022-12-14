import imp
from re import I
from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=20,default='')
    author=models.CharField(max_length=20,default='')
    price=models.IntegerField(default='')
    origin_price=models.IntegerField(default='')
    # seller : Post 1 : N 관계 하나의 유저가 여러개의 포스트를 작성 가능
    seller=models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    sell_date=models.DateTimeField(auto_now_add=True)
    content=models.TextField(max_length=100,default=' ')
    # image = ResizedImageField(size=[300,200],upload_to='images/', blank=True, null=True)
    def __str__(self):
        ordering = ['-date',]
        return '[{}] {}'.format(self.id, self.title)
class PostImage(models.Model):
    post=models.ForeignKey(Post,default='None',on_delete=models.CASCADE)
    images=models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.post.title