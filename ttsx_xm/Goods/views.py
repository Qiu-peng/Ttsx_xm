from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, JsonResponse
from random import randint


# Create your views here.
# 首页视图
def index(request):
    """按新添加推荐商品3个，按点击量过滤展示商品图片4张"""
    # 获取新添加的三个水果，和点击量最高的四个水果
    fruit = GoodsInfo.objects.filter(gtype=1).order_by("-id")[:3]
    fruit2 = GoodsInfo.objects.filter(gtype=1).order_by('-gclick')[:4]

    # 获取新添加的三个海鲜水产，和点击量最高的四个海鲜水产
    fish = GoodsInfo.objects.filter(gtype=2).order_by("-id")[:3]
    fish2 = GoodsInfo.objects.filter(gtype=2).order_by('-gclick')[:4]

    # 获取新添加的三个肉类，和点击量 最高的四个肉类
    meal = GoodsInfo.objects.filter(gtype=3).order_by("-id")[:3]
    meal2 = GoodsInfo.objects.filter(gtype=3).order_by('-gclick')[:4]

    # 获取新添加的三个禽类蛋品，和点击量最高的四个禽类蛋品
    eggs = GoodsInfo.objects.filter(gtype=4).order_by("-id")[:3]
    eggs2 = GoodsInfo.objects.filter(gtype=4).order_by('-gclick')[:4]

    # 获取新添加的三个蔬菜，和点击量最高的四个蔬菜
    vege = GoodsInfo.objects.filter(gtype=5).order_by("-id")[:3]
    vege2 = GoodsInfo.objects.filter(gtype=5).order_by('-gclick')[:4]

    # 获取新添加的三个速冻食品，和点击量最高的四个速冻食品
    fastFrozen = GoodsInfo.objects.filter(gtype=6).order_by("-id")[:3]
    fastFrozen2 = GoodsInfo.objects.filter(gtype=6).order_by('-gclick')[:4]

    context = {
        'fruit': fruit, 'fruit2': fruit2,
        'fish': fish, 'fish2': fish2,
        'meal': meal, 'meal2': meal2,
        'eggs': eggs, 'eggs2': eggs2,
        'vege': vege, 'vege2': vege2,
        'fastFrozen': fastFrozen, 'fastFrozen2': fastFrozen2
    }
    return render(request, 'Goods/index.html', context)


# 定义一个全局列表，用来存最近浏览信息
goodsl = []


def detail(request, picid):
    # 根据传过来的id获取指定图片数据
    goods = GoodsInfo.objects.get(id=picid)
    # 获取同类型的三个新品
    goodslist = GoodsInfo.objects.filter(gtype=goods.gtype).order_by("-id")[:3]
    # 设置点击量+1
    goods.gclick += 1
    goods.save()
    # 传递上下文
    context = {'goods': goods, 'goodslist': goodslist}
    response = render(request, 'Goods/detail.html', context)
    # 引用全局定义的列表,将最近浏览的商品的id存入列表再将列表存入cookie
    global goodsl
    # 判断id是否重复，将图片id加入列表
    if goodsl.count(goods.id) >= 1:
        # 重复则删除旧的
        goodsl.remove(goods.id)
    # 加入列表最前
    goodsl.insert(0, goods.id)
    # 限制长度
    if len(goodsl) > 5:
        del goodsl[5]
    response.set_cookie('Rcently', goodsl, expires=24 * 60 * 60 * 30)
    print(goodsl)
    return response


def list(request, lid, sort):
    # 根据传过来的id获取这个商品同类的所有商品
    if int(sort) == 0:   # 默认排序
        goods = GoodsInfo.objects.filter(gtype=lid)
        # print("sort=0")
    elif int(sort) == 1:  # 价格从低到高排序
        goods = GoodsInfo.objects.filter(gtype=lid).order_by("gprice")
        # print("sort=1")
    elif int(sort) == 2:  # 按点击量从高到底排序
        goods = GoodsInfo.objects.filter(gtype=lid).order_by("-gclick")
        # print("sort=2")
    # 获取当前商品大类对象
    type = TypeInfo.objects.get(id=lid)
    # 获取当前商品的同类的三个新品
    goods2 = GoodsInfo.objects.filter(gtype=lid).order_by("-id")[:3]

    context = {'goods': goods, 'type': type, 'goods2': goods2,'sort':sort}

    return render(request, 'Goods/list.html', context)


# 从cookie拿到登录名,显示在用户名处
def getname(request):
    uname = request.COOKIES.get('uname')
    context = {'uname': uname}
    return JsonResponse(context)


# 退出登录,删除cookie
def delete(request):
    uname = request.COOKIES.get('uname')
    if uname:
        response = HttpResponseRedirect('/')
        response.set_cookie('uname', 1, expires=0)
        return response


