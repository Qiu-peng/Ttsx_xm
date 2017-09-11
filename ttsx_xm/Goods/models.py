from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class TypeInfo(models.Model):
    """生鲜大类"""
    # 类名
    ttile = models.CharField(max_length=20)
    # 是否逻辑删除,默认没有
    isDelete = models.BooleanField(default=False)

    # 对象打印显示
    def __str__(self):
        return self.ttile


class GoodsInfo(models.Model):
    """商品信息"""
    # 商品名称
    gtitle = models.CharField(max_length=20)
    # 上传图片路径为static/media/goods
    gpic = models.ImageField(upload_to='goods')
    # 单价,总位数5位，小数位数2位
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    # 是否逻辑删除
    idDelete = models.BooleanField(default=False)
    # 单位
    gunit = models.CharField(max_length=20, default='500g')
    # 点击量
    gclick = models.IntegerField()
    # 简介
    gjianjie = models.CharField(max_length=200)
    # 库存量
    gkucun = models.IntegerField()
    # 描述
    gcontent = HTMLField()
    # 类型
    gtype = models.ForeignKey(TypeInfo)

    # 类对象的打印信息
    def __str__(self):
        return self.gtitle
