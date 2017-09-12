from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse


# 显示登录页面
def login(request):
    return render(request, 'User/login.html')


def toLogin(request):
    uname = request.POST.get('name')
    the_user = UserInfo.users.filter(userName=uname)
<<<<<<< HEAD
    print(the_user.exists())
    # aaa = the_user.exists()
    if the_user.exists():
        upwd = the_user.userPsw
        print(upwd)
        return JsonResponse({'pwd': upwd})
    else:
        print('ccc')
        return JsonResponse({'sss': 'nonono'})

=======
    if len(the_user)==0:
        return JsonResponse({'pwd':''})
    else:
        upwd = the_user[0].userPsw
        request.session['name'] = uname
        return JsonResponse({'pwd':upwd})

def session_get(request):
    name = request.session.get('name')
    return JsonResponse({'name':name})
>>>>>>> 5704a4ce988ddc557cfa0afc9c9898b74d3072ab

def toindex(request):
    uname = request.GET.get('name')
    context={'uname': uname}
    print(context)
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