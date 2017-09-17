from django.db import models

# Create your models here.

# 购物车信息
class CartInfo(models.Model):
    # 链接User应用中的模型类
    user=models.ForeignKey('User.UserInfo')
    # 链接Goods应用中的模型类
    goods=models.ForeignKey('Goods.GoodsInfo')
    # 购物车商品计数
    count=models.IntegerField()