from django.shortcuts import render
from .models import *
from random import randint


# Create your views here.
# 首页视图
def index(request):
    """按新添加推荐商品3个，按点击量过滤展示商品图片4张"""
    global goodsl
    goodsl=[]
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

goodsl=[]
def detail(request, picid):
    # 根据传过来的id获取指定图片数据
    goods = GoodsInfo.objects.get(id=picid)
    # 获取同类型的三个新品
    goodslist = GoodsInfo.objects.filter(gtype=goods.gtype).order_by("-id")[:3]
    goods.gclick += 1
    print(goods.gclick)
    context = {'goods': goods, 'goodslist': goodslist}
    response = render(request, 'Goods/detail.html', context)
    global goodsl
    goodsl.append(goods.id)
    response.set_cookie('good',goodsl)
    return response


def list(request, lid):
    # 根据传过来的id获取这个商品同类的所有商品
    goods = GoodsInfo.objects.filter(gtype=lid)
    # 获取当前商品大类对象
    type = TypeInfo.objects.get(id=lid)
    # 获取当前商品的同类的三个新品
    goods2 = GoodsInfo.objects.filter(gtype=lid).order_by("-id")[:3]
    context = {'goods': goods, 'type': type, 'goods2': goods2}
    return render(request, 'Goods/list.html', context)


# 登录页跳转过来的首页显示,并记录用户名
def login(request, uname):
    context = {'uname': uname}
    print(context)
    return render(request, 'Goods/index.html', context)
