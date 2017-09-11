from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse


# 显示登录页面
def login(request):
    return render(request, 'User/login.html')


def toLogin(request):
    dict = request.POST
    uname = dict.get('username')
    upsd = dict.get('pwd')
    # the_user = UserInfo.objects.get(userName=uname)
    # verifycode = the_user.userPsw

    verifyname = 'sunhh'
    verifycode = '123'
    if (upsd == verifycode) and (uname == verifyname):
        return render(request, 'Goods/index.html')
        # return JsonResponse({'verify': True})
    else:
        return JsonResponse({'verify': False})
        # return render(request, 'User/login.html', {'aaa': 111})

    # list = [verifyname, verifycode]
    # return JsonResponse({'verify': list})

# 显示注册页面
def register(request):
    return render(request, 'User/register.html')

# 处理用户填入的注册信息
def regist(request):
    dict = request.POST
    uname = dict.get('user_name')
    upsw = dict.get('pwd')
    uemail = dict.get('email')

    add = UserInfo.users.create(uname, upsw, uemail)
    add.save()
    return redirect('/User/login/')


# 判断注册用户的用户名是否存在,存在就不存入不注册
def ishere(request):
    uname = request.GET.get('name')
    getit = UserInfo.users.filter(userName=uname).exists()

    return JsonResponse({'it': getit})

def center(request):
    return render(request, 'User/user_center_info.html')