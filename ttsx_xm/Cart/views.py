from django.shortcuts import render
from django.http import HttpResponseRedirect


def cart(request):
    return render(request, 'Cart/cart.html')


# 退出登录,删除cookie
def delete(request):
    uname = request.COOKIES.get('uname')
    if uname:
        response = HttpResponseRedirect("/Cart/cart/")
        response.set_cookie('uname', 1, expires=0)
        return response