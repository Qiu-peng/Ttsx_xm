from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse


# 显示登录页面
def login(request):
    return render(request, 'User/login.html')


def toLogin(request):
    uname = request.POST.get('name')
    f_login = open('static/txt/user_lock.txt', 'r+')
    user_list = f_login.read().split(",")
    if uname in user_list:
        return JsonResponse({'pwd':''})
    the_user = UserInfo.users.filter(userName=uname)
    if len(the_user)==0:
        return JsonResponse({'pwd':''})
    else:
        upwd = the_user[0].userPsw
        response = JsonResponse({'pwd':upwd})
        response.set_cookie('uname', uname, expires=7 * 24 * 60 * 60)  # 7天后过期
        return response
def cook_get(request):
    lname = request.COOKIES.get('uname') #[{},{}...]
    return JsonResponse({'list':lname})

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


# 判断注册用户的用户名是否存在,存在就不存入不注册
def ishere(request):
    uname = request.GET.get('name')
    getit = UserInfo.users.filter(userName=uname).exists()

    return JsonResponse({'it': getit})

def center(request):
    return render(request, 'User/user_center_info.html')

def saveName(request):
    sname = request.GET.get('name')
    f_login = open('static/txt/user.txt', 'r+')
    user_list = f_login.read().split(",")
    if sname in user_list:
        return
    else:
        user_save = open('static/txt/user.txt', 'a+')
        user_save.write('%s,'%sname)
        user_save.close()

def readName(request):
    f_login = open('static/txt/user.txt', 'r+')
    user_list = f_login.read().split(",")
    list =[]
    for i in user_list:
        if i != '':
            list.append(i)
    return JsonResponse({'lname': list})

def lockPwd(request):
    f_login = open('static/txt/user_lock.txt', 'r+')
    user_list = f_login.read().split(",")

    return JsonResponse({'lock': list})