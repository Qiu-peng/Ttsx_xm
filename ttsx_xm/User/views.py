from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


# 显示登录页面
def login(request):
    return render(request, 'User/login.html')


# 登陆页匹配用户密码处理
def toLogin(request):
    uname = request.POST.get('name')
    f_login = open('static/txt/user_lock.txt', 'r+')
    user_list = f_login.read().split(",")
    if uname in user_list:
        return JsonResponse({'pwd': False})
    the_user = UserInfo.users.filter(userName=uname)
    if the_user.exists():
        upwd = the_user[0].userPsw
        response = JsonResponse({'pwd': upwd})
        response.set_cookie('uname', uname, expires=7 * 24 * 60 * 60)  # 7天后过期
        return response
    else:
        return JsonResponse({'pwd': False})


def cook_get(request):
    lname = request.COOKIES.get('uname') #[{},{}...]
    return JsonResponse({'list':lname})


def toLogin111(request):
    dict = request.POST
    uname = dict.get('username')
    upwd = dict.get('pwd')
    the_user = UserInfo.users.get(userName=uname)
    verify_pwd = the_user.userPsw
    if verify_pwd == upwd:
        print(uname)
        response = HttpResponseRedirect('/')
        response.set_cookie('uname', uname)
        print('ok')
        return response
    else:
        print('错误')
        # return HttpResponseRedirect('/User/login/')
        return render(request, 'User/login.html', {'display': 'block'})


# 返回用户名
def toindex(request):
    uname = request.GET.get('name')  # 读取用户名
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


# 用户中心订单页面
def center_order(request, uname):
    context = {'uname': uname}
    return render(request, 'User/user_center_order.html', context)


# 用户中心地址页面
def center_site(request, uname):
    context = {'uname': uname}
    return render(request, 'User/user_center_site.html', context)



