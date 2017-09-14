from django.shortcuts import render
from django.http import HttpResponseRedirect

def order(request):
    # 显示订单页面
    return render(request, 'Order/place_order.html',)


# 退出登录,删除cookie
def delete(request):
    uname = request.COOKIES.get('uname')
    if uname:
        response = HttpResponseRedirect('/Order/')
        response.set_cookie('uname', 1, expires=0)
        return response

