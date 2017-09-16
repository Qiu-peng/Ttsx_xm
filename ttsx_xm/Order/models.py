from django.db import models
from User.models import UserInfo
from Goods.models import GoodsInfo

class OrderInfo(models.Model):
    # 订单编号
    oid=models.CharField(max_length=20, primary_key=True)
    # 关联用户
    user=models.ForeignKey(UserInfo)
    # 下单日期
    odate=models.DateTimeField(auto_now_add=True)
    # 是否支付
    oIsPay=models.BooleanField(default=False)
    # 金额
    ototal=models.DecimalField(max_digits=6,decimal_places=2)
    # 订单地址
    oaddress=models.CharField(max_length=150)



class OrderDetailInfo(models.Model):
    # 关联商品
    goods=models.ForeignKey(GoodsInfo)
    # 关联订单
    order=models.ForeignKey(OrderInfo)
    # 价格
    price=models.DecimalField(max_digits=5,decimal_places=2)
    # 数量
    count=models.IntegerField()


