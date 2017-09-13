from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse


# 显示登录页面
def login(request):
    return render(request, 'User/login.html')


# 登陆页匹配用户密码处理
def toLogin(request):
    uname = request.POST.get('name')
    the_user = UserInfo.users.filter(userName=uname)
    if the_user.exists():
        upwd = the_user[0].userPsw
        return JsonResponse({'pwd': upwd})
    else:
        return JsonResponse({'pwd': False})

def session_get(request):
    name = request.session.get('name')
    return JsonResponse({'name':name})


def session_get(request):
    name = request.session.get('name')
    return JsonResponse({'name': name})


# 返回用户名,并将用户名session存储
def toindex(request):
    uname = request.GET.get('name')  # 读取用户名
    request.session['name'] = uname  # 将用户名用session存储
    context = {'uname': uname}
    return JsonResponse(context)


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


# 跳转用户中心
def center(request, uname):
    context = {'uname': uname}
    return render(request, 'User/user_center_info.html', context)