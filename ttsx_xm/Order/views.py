from django.shortcuts import render
from Cart.models import CartInfo
from User.models import UserInfo,UserAddressInfo
from Goods.models import GoodsInfo
def order(request):
    # 获取购物车对象

    # 显示订单页面
    return render(request,'Order/place_order.html',)
