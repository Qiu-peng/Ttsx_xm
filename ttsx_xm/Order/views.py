from django.shortcuts import render


def order(request):
    # 显示订单页面
    return render(request, 'Order/place_order.html',)
