from django.db import models

# Create your models here.

# 购物车信息
class CartInfo(models.Model):
    user=models.ForeignKey('User.UserInfo')
    goods=models.ForeignKey('Goods.GoodsInfo')
    isDelete= models.BooleanField(default=False)
    count=models.IntegerField()