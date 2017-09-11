from django.shortcuts import render
from Cart.models import *
from .models import *
from django.db import transaction
def order(request):
    # 获取购物车对象
    cart = CartInfo.objects.all()

    context = {'cart':cart}
    return render(request,'Order/place_order.html',context)


