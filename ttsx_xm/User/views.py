from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from hashlib import sha1


# 显示登录页面
def login(request):
    return render(request, 'User/login.html')


# 登陆页匹配用户密码处理
def toLogin(request):
    uname = request.POST.get('name')
    the_user = UserInfo.users.filter(userName=uname)  # 获取用户名对应的对象
    if the_user.exists():  # 判断用户是否存在
        if the_user[0].isValid:  # 判断用户是否可用
            if the_user[0].isActive:  # 判断是否激活
                upwd = the_user[0].userPsw
                response = JsonResponse({'pwd': upwd})
                response.set_cookie('uname', uname, expires=7 * 24 * 60 * 60)  # 7天后过期
                return response
            else:
                uid = the_user[0].id
                return JsonResponse({'pwd': 'notActive', "uid": uid})
        else:
            return JsonResponse({'pwd': 'notValid'})
    else:
        return JsonResponse({'pwd': 'notExists'})


# 返回用户名
def toindex(request):
    uname = request.GET.get('name')  # 读取用户名
    # 保存到txt中
    f_login = open('static/txt/user.txt', 'r+')
    user_list = f_login.read().split(",")
    if uname not in user_list:
        user_save = open('static/txt/user.txt', 'a+')
        user_save.write('%s,' % uname)
        user_save.close()
    # 记住密码选项
    ischeck = request.GET.get('ischeck')
    the_user = UserInfo.users.filter(userName=uname)
    list = [the_user[0].userName, the_user[0].userPsw]
    if ischeck:
        request.session['repwd'] = list  # 存对象
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
    # 密码sha1加密
    sh1 = sha1()
    sh1.update(upsw.encode('utf-8'))
    upsw_sh1 = sh1.hexdigest()
    # 添加进数据库表中
    add = UserInfo.users.create(uname, upsw_sh1, uemail)
    add.save()
    # 发送激活邮件
    msg = '<br/><a href="http://127.0.0.1:8000/User/active%s/">点击激活</a>' % add.id
    send_mail('天天生鲜用户注册激活', '', settings.EMAIL_FROM, [uemail], html_message=msg)
    return HttpResponse('激活邮件已发送,请移步邮箱激活!<br/><br/><a href="https://mail.qq.com/">点击登录qq邮箱</a>')


# 判断注册用户的用户名是否存在,存在就不存入不注册
def ishere(request):
    uname = request.GET.get('name')
    getit = UserInfo.users.filter(userName=uname).exists()

    return JsonResponse({'it': getit})


# 跳转用户中心
def center(request, uname):
    context = {'uname': uname}
    return render(request, 'User/user_center_info.html', context)


# 读账号
def readName(request):
    f_login = open('static/txt/user.txt', 'r+')
    user_list = f_login.read().split(",")
    list =[]
    for i in user_list:
        if i != '':
            list.append(i)
    return JsonResponse({'lname': list})


def remember(request):
    name = request.POST.get('name')
    the_user = UserInfo.users.filter(userName=name)
    pwd = the_user[0].userPsw
    list = request.session.get('repwd')
    uname = list[0]
    if uname == name:
        return JsonResponse({'repwd': pwd})
    else:
        return JsonResponse({'repwd': False})


# 清空session
def clearSession(request):
    llen = request.session.get('repwd')
    if llen!= None:
        request.session.flush()
        flag = 0
    else:
        flag = 1
    return JsonResponse({'type': flag})


# 跳转用户中心
def center(request):
    uname = request.COOKIES.get('uname')
    context = {'uname': uname}
    return render(request, 'User/user_center_info.html', context)


# 用户中心订单页面
def center_order(request):
    uname = request.COOKIES.get('uname')
    context = {'uname': uname}
    return render(request, 'User/user_center_order.html', context)


# 用户中心地址页面
def center_site(request):
    uname = request.COOKIES.get('uname')
    context = {'uname': uname}
    return render(request, 'User/user_center_site.html', context)


def send(request, uid):
    the_user = UserInfo.users.get(id=uid)
    uid = the_user.id
    uemail = the_user.userEmail
    msg = '<a href="http://127.0.0.1:8000/User/active%s/">点击激活</a>' % uid
    send_mail('天天生鲜用户注册激活', '', settings.EMAIL_FROM,
              [uemail],
              html_message=msg)
    return HttpResponse('激活邮件已发送,请移步邮箱激活!')


# 激活用户
def active(request, uid):
    active_user = UserInfo.users.get(id=uid)
    active_user.isActive = True
    active_user.save()
    return HttpResponse('用户已激活, <a href="/User/login/">点击登录</a>')
