from django.shortcuts import render, redirect
from django.http import JsonResponse
from Cart.models import *
from .models import *
from django.db import transaction
from datetime import datetime

def showorder(request):
    # 获取url中的商品id
    goodsid = request.GET.getlist('goodsid')
    # 立即购买的数量
    goodnum = request.GET.get('num')
    # 保存购物车对象
    cart = []
    for gid in goodsid:
        # filter返回列表，若获取不到购物车对象即返回空列表 立即购买时，cart即为空列表
        clist = CartInfo.objects.filter(goods=gid)
        # 获取到购物车对象
        if clist:
            cart.append(clist[0])

    # 获取立即购买的商品对象，只有1个商品
    good = GoodsInfo.objects.get(pk = goodsid[0])

    context = {'cart': cart,'goodnum':goodnum,'good':good}

    return render(request, 'Order/place_order.html', context)


# 创建订单主表
# 查询选中的购物车信息，逐个遍历
# 判断商品库存是否满足当前购买数量
# 如果库存量不足，则事务回滚，转到购物车页面
# 如果库存量足够，则减少库存量，创建详单对象，删除购物车对象
# 计算总金额，循环结束后存储

@transaction.atomic
def handle_order(request):
    # 接收请求参数
    cid = request.POST.getlist('cid') # 购物车id
    gid = request.POST.get('gid') #立即购买商品id str类型
    gcount = request.POST.get('count') #立即购买商品数量 str类型

    # 开启事务
    trans_id = transaction.savepoint()

    def createorder():
        # 创建订单主表
        order = OrderInfo()
        order.oid = datetime.now().strftime('%Y%m%d%H%M%S')
        # 获取用户 request.session['uid']
        order.user_id = 1
        order.ototal = 0
        order.oaddress = '深圳'
        # 保存修改
        order.save()
        return order

    # 此函数调用出错
    def createdetail(goods,order):
        # 创建详单对象
        detail = OrderDetailInfo()
        detail.goods = goods
        detail.order = order
        detail.price = goods.gprice
        detail.save()
        return detail

    # 立即购买的订单处理
    if gid:
        # 创建订单
        # print('---------7')
        # print(createorder)
        # print('---------8')
        order = createorder()
        # print('---------9')
        # print(order)
        # print('---------10')


        # 查询立即购买的商品
        goods = GoodsInfo.objects.get(id=gid)
        # 库存足够
        gcount = int(gcount)
        if goods.gkucun>=gcount:
            # 保存总金额
            order.ototal = gcount*goods.gprice
            order.save()
            # 减少库存量
            goods.gkucun -= gcount
            goods.save()

            # 创建详单对象
            # print('--------1')
            detail = OrderDetailInfo()
            # print(detail)
            # print('--------2')
            detail.goods = goods
            detail.order = order
            detail.count = gcount
            detail.price = goods.gprice
            detail.save()

            # 创建详单  函数调用出错
            # print('-----------3')
            # print(createdetail)
            # print('-----------4')
            # detail = createdetail(goods,order)
            # print('-----------5')
            # print(detail)
            # print('-----------6')
            # detail.count = gcount
            # detail.save()

            # 提交事务
            transaction.savepoint_commit(trans_id)
            # return redirect('/')

            # return render(request,'/Goods/index.html/')
        # 库存不足
        else:
            # 回滚事务
            transaction.savepoint_rollback(trans_id)
            # 回到立即购买页面
            return redirect('/Cart/cart')




    # 购物车订单处理
    else:
        # 创建订单  django负责维护的订单日期  比本地早8小时
        order = createorder()

        # 查询选中的购物车信息，逐个遍历
        clist = CartInfo.objects.filter(id__in=cid)
        # 判断提交事务 或回滚事务
        isOK = True
        for cart in clist:
            goods = cart.goods

            # 库存足够
            if goods.gkucun >= cart.count:
                # 计算总金额
                order.ototal += cart.count * goods.gprice
                order.save()
                # 减少库存量
                goods.gkucun -= cart.count
                goods.save()


                # 创建详单对象
                detail = OrderDetailInfo()
                detail.goods = goods
                detail.order = order
                detail.count = cart.count
                detail.price = goods.gprice
                detail.save()


                # 创建详单
                # det=createdetail(goods,order) # 此处错误
                # print(det)
                # print(cart.count)
                # det.count = cart.count
                # det.save()

                # 删除购物车对象
                cart.delete()
            # 库存不足
            else:
                isOK = False
                break
        if isOK:
            # 提交事务
            transaction.savepoint_commit(trans_id)
            return redirect('/')

        else:
            # 回滚事务
            transaction.savepoint_rollback(trans_id)
            # 回到购物车

            return redirect('/Cart/cart')

