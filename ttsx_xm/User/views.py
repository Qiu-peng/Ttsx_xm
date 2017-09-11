from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse


# 显示登录页面
def login(request):
    return render(request, 'User/login.html')


def toLogin(request):
    uname = request.POST.get('name')
    the_user = UserInfo.users.get(userName=uname)
    upwd = the_user.userPsw
    return JsonResponse({'pwd':upwd})

def toindex(request):
    uname = request.GET.get('name')
    context={'uname':uname}
    # print(context)
    return render(request, 'Goods/index.html', context)
    # return redirect('Goods/index.html')

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

def ishere(request):
    uname = request.POST.get('user_name')
    getit = UserInfo.objects.filter(userName=uname).exists()
    return JsonResponse({'it': getit})

def center(request):
    return render(request, 'User/user_center_info.html')