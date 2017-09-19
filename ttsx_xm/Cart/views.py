
from django.shortcuts import render,redirect
from .models import *
from Goods.models import *
from django.http import JsonResponse
# Create your views here.


def cart(request):
    #可以用关联查询
    # uid = request.session['user_id']
    # 查询uid的用户的全部购物车的商品
    carts = CartInfo.objects.filter(user_id = 1)
    context= {'carts':carts}
    return render(request,'Cart/cart.html',context)


# 给购物车添加商品
def add(request):
    uid = request.session['user_id']
    dict=request.GET
    gs_count=dict.get('count')
    gs_id=dict.get('goodsid')
    carts = CartInfo.objects.filter(goods_id=gs_id,user_id=uid)
    #判断购物车是否为空
    if len(carts)>=1:
        # 取出一个对象
        cart = carts[0]
        # 数量
        cart.count = cart.count+gs_count
    else:
        cart = CartInfo()
        cart.user_id=uid
        cart.goods_id=gs_id
        cart.count=gs_count
    cart.save()
    count = CartInfo.objects.filter(user_id=request.session['user_id']).count
    return JsonResponse({'count': count})


# 向已存在的购物车中添加物品
def edit(request):
    dict=request.GET
    cart_id=dict.get('cartid')
    count=dict.get('counts')
    # 获得id为cart_id的购物车
    cart=CartInfo.objects.get(id=int(cart_id))
    count=cart.count=int(count)
    cart.save()
    return JsonResponse({'count':count})


# 删除
def remove(request):
    cart_id=request.GET.get('cart')
    cart = CartInfo.objects.filter(id=int(cart_id))
    cart.delete()
    return JsonResponse({'ok':1})

