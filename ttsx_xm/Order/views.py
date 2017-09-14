from django.shortcuts import render, redirect
from Cart.models import *
from .models import *
from django.db import transaction
from datetime import datetime
import time


def showorder(request):
    # 获取url中的商品id
    goodsid = request.GET.getlist('goodsid')
    # 立即购买的数量
    goodnum = request.GET.get('num')
    # 保存购物车对象
    cart = []
    for gid in goodsid:
        # filter返回列表，若获取不到购物车对象即返回空列表 立即购买时，cart即为空列表
        clist = CartInfo.objects.filter(goods_id=gid)
        # 获取到购物车对象
        if clist:
            cart.append(clist[0])

    # 获取立即购买的商品对象，只有1个商品
    good = GoodsInfo.objects.get(pk = goodsid[0])

    context = {'cart': cart,'goodnum':goodnum,'good':good}
    print(good)
    return render(request, 'Order/place_order.html', context)


@transaction.atomic()
def handle_order(request):
    #  设置回退点
    rollback_point = transaction.savepoint()
    try:
        now = datetime.now()

        order = OrderInfo()
        # 订单编号
        order.oid = int(now.strftime('%Y%m%d%H%M%S') + str(int(time.time() * 1000)))
        # 订单日期
        order.odate = now

        order.user_id = 1
        order.oIsPay = False
        order.ototal = 1000
        order.oaddress = '深圳'
        # 查询购物车商品
        cart = CartInfo.objects.all()
        for c in cart:
            detail = OrderDetailInfo()
            detail.order = order
            good = c.goods
            # 库存大于购买数量
            if good.gkucun >= c.count:
                good.gkucun = good.gkucun - c.count
                good.save()
                # 详单信息
                detail.goods_id = good.id
                detail.price = good.gprice
                detail.count = c.count
                detail.save()
            # 库存小于购买量，事务回滚，回到购物车
            else:
                transaction.savepoint_rollback(rollback_point)
                return redirect('/Cart/cart/')
        # 提交事务
        transaction.savepoint_commit(rollback_point)
    # 有异常回滚
    except Exception:
        transaction.savepoint_rollback(rollback_point)

    return render(request, '/User/user_center_order.html/')
