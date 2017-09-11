from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def login(request):
    return render(request, 'User/login.html')

def register(request):
    return render(request, 'User/register.html')


# 显示登录页面
def login(request):
    return render(request, 'User/login.html')

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
    return redirect('/login/')
