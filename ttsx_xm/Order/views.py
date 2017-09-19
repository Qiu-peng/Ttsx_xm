from django.shortcuts import render, redirect
from Cart.models import *
from User.models import *
from .models import *
from django.db import transaction
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
import qrcode
from io import BytesIO


def showorder(request):
    # 获取url中的商品id
    goodsid = request.GET.getlist('goodsid')
    # 立即购买的数量
    goodnum = request.GET.get('num')
    # 保存购物车对象
    cart = []
    # 保存购买商品对象
    good = None
    if goodnum:
        # 获取立即购买的商品对象，只有1个商品
        good = GoodsInfo.objects.get(pk=goodsid[0])

    else:
        for gid in goodsid:
            # filter返回列表，若获取不到购物车对象即返回空列表 立即购买时，cart即为空列表
            clist = CartInfo.objects.filter(goods=gid)
            # 获取到购物车对象
            if clist:
                cart.append(clist[0])
    context = {'cart': cart, 'goodnum': goodnum, 'good': good}
    return render(request, 'Order/place_order.html', context)


# 创建订单
def createorder(request):
    order = OrderInfo()
    order.oid = datetime.now().strftime('%Y%m%d%H%M%S')
    # 获取缓存的用户名
    # uname = request.COOKIES.get('uname')
    # 获取用户对象
    # user = UserInfo.objects.get(userName=uname)
    # 用户id
    order.user_id = 1  # user.id
    order.ototal = 0
    # 用户地址
    order.oaddress = '深圳'  # UserAddressInfo.objects.get(user=user).uAddress
    # 保存修改
    order.save()
    return order


# 创建详单
def createdetail(goods, order):
    detail = OrderDetailInfo()
    detail.goods = goods
    detail.order = order
    detail.price = goods.gprice
    detail.count = 0
    detail.save()
    return detail


# 生成二维码
def code(request):
    qcode = qrcode.make('http://www.alipay.com')
    buf = BytesIO()
    qcode.save(buf, 'png')
    response = HttpResponse(buf.getvalue(), 'image/png')
    return response

# 提交订单处理
@transaction.atomic
def handle_order(request):
    # 接收请求参数
    cid = request.POST.getlist('cid')  # 购物车id
    gid = request.POST.get('gid')  # 立即购买商品id str类型
    gcount = request.POST.get('count')  # 立即购买商品数量 str类型

    # 开启事务
    trans_id = transaction.savepoint()

    # 立即购买的订单处理
    if gid:
        # 创建订单
        order = createorder(request)
        # 查询立即购买的商品
        goods = GoodsInfo.objects.get(id=gid)
        # 库存足够
        gcount = int(gcount)
        if goods.gkucun >= gcount:
            # 保存总金额
            order.ototal = gcount * goods.gprice
            order.save()
            # 减少库存量
            goods.gkucun -= gcount
            goods.save()

            # 创建详单
            detail = createdetail(goods, order)
            detail.save()

            # 提交事务
            transaction.savepoint_commit(trans_id)
            total = order.ototal
            context = {'status': '1', 'total': total}
            return render(request, 'Order/submitorder.html', context)
        # 库存不足
        else:
            # 回滚事务
            transaction.savepoint_rollback(trans_id)

            # 回到立即购买页面
            context = {'status': '2'}
            return render(request, 'Order/submitorder.html', context)

    # 购物车订单处理
    else:
        # 创建订单  django负责维护的订单日期  比本地早8小时
        orders = createorder(request)
        # 查询选中的购物车信息，逐个遍历
        clist = CartInfo.objects.filter(id__in=cid)
        # 判断提交事务 或回滚事务
        isOK = True
        for cart in clist:
            goods = cart.goods
            # 库存足够
            if goods.gkucun >= cart.count:
                # 计算总金额
                orders.ototal += cart.count * goods.gprice
                orders.save()
                # 减少库存量
                goods.gkucun -= cart.count
                goods.save()
                # 创建详单
                det = createdetail(goods, orders)
                det.count = cart.count
                det.save()
                # 删除购物车对象
                cart.delete()
            # 库存不足
            else:
                isOK = False
                break
        if isOK:
            # 提交事务
            transaction.savepoint_commit(trans_id)
            total = orders.ototal
            context = {'status': '1', 'total': total}
            return render(request, 'Order/submitorder.html', context)

        else:
            # 回滚事务
            transaction.savepoint_rollback(trans_id)
            # 回到购物车
            context = {'status': '3'}
            return render(request, 'Order/submitorder.html', context)

