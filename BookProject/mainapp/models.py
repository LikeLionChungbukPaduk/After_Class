from django.db import models
from django.contrib.auth.models import User

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
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return '[{}] {}'.format(self.id, self.title)
# class Photo(models.Model):
#     # post 하나에 여러개의 photo가 들어있을 수 있음 one to many관계 -> foreignkey관계
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)