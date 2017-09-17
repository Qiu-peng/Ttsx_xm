from django.shortcuts import render
from .models import *
from PIL import Image, ImageDraw, ImageFont
from django.http import JsonResponse, HttpResponse
from hashlib import sha1
from . import task
import time
from django.core.paginator import Paginator
from Goods.models import *
from Order.models import *
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
    uname = request.POST.get('name')  # 读取用户名
    # 保存到txt中
    f_login = open('static/txt/user.txt', 'r+')
    user_list = f_login.read().split(",")
    if uname not in user_list:
        user_save = open('static/txt/user.txt', 'a+')
        user_save.write('%s,' % uname)
        user_save.close()
    # 记住密码选项
    ischeck = request.POST.get('ischeck')
    pwd = request.POST.get('pwd')
    list_u = [uname, pwd]
    if ischeck:
        request.session['repwd'] = list_u  # 存对象
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
    # 任务加入celery中
    task.send.delay(add.id, uemail)
    return HttpResponse('激活邮件已发送,请移步邮箱激活!<br/><br/><a href="https://mail.qq.com/">点击登录qq邮箱</a>')


# 判断注册用户的用户名是否存在,存在就不存入不注册
def ishere(request):
    uname = request.GET.get('name')
    getit = UserInfo.users.filter(userName=uname).exists()

    return JsonResponse({'it': getit})


# 读账号
def readName(request):
    f_login = open('static/txt/user.txt', 'r+')
    user_list = f_login.read().split(",")
    list = []
    for i in user_list:
        if i != '':
            list.append(i)
    return JsonResponse({'lname': list})


# 记住密码
def remember(request):
    name = request.POST.get('name')
    list_u = request.session.get('repwd')
    uname = list_u[0]
    pwd = list_u[1]
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
    li = request.COOKIES.get(uname).split(',')
    the_li = []
    for item in li:
        if item != '':
            it = GoodsInfo.objects.get(id=item)
            the_li.append(it)
    context = {'uname': uname, 'list': the_li}
    return render(request, 'User/user_center_info.html', context)


# 用户中心订单页面
def center_order(request, pIndex):
    uname = request.COOKIES.get('uname')
    # 订单信息
    uid = UserInfo.users.get(userName=uname).id
    the_order = OrderInfo.objects.filter(user_id=uid)  # 订单列表
    ali = []
    if the_order != []:
        # 订单详情
        for item in the_order:
            oid = item.oid
            the_detail = OrderDetailInfo.objects.filter(order_id=oid)  # oid筛选出订单里的商品
            the_list = []
            for detail in the_detail:
                goods = GoodsInfo.objects.get(id=detail.goods_id)  # 订单id筛选出商品
                the_list.append({'detail': detail, 'goods': goods})
            ali.append({"order": item, "the_list": the_list})
    context = {'uname': uname, 'list': ali}  # [{'order': order对象, "list": {goods对象, detail对象} }, {},....]
    return render(request, 'User/user_center_order.html', context)


# 用户中心地址页面
def center_site(request):
    uname = request.COOKIES.get('uname')
    context ={'uname': uname}
    return render(request, 'User/user_center_site.html', context)


# 验证码
def verify_code(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 100)
    width = 100
    height = 34
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 32)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str

    # 内存文件操作(python3)
    from io import BytesIO
    buf = BytesIO()

    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


# 提交验证码
def yzm(request):
    """验证码的验证"""
    # 1.获取post请求当中的输入验证码的内容
    verify = request.POST.get('yzm')
    # 小写转大写
    ver =verify.upper()
    # 2.获取浏览器请求当中的session中的值
    verifycode = request.session.get('verifycode')
    # 3.判断两个验证码是否相同
    if ver == verifycode:
        return JsonResponse({'ret': True})
    else:
        return JsonResponse({'ret': False})


# 登录时,判断出未激活,发送邮件
def send(request, uid):
    the_user = UserInfo.users.get(id=uid)
    uid = the_user.id
    uemail = the_user.userEmail
    time.sleep(3)  # 延迟3s发送邮件,让用户看见未激活提示
    # 任务加入celery中
    task.send.delay(uid, uemail)
    return HttpResponse('激活邮件已发送,请移步邮箱激活!<br/><br/><a href="https://mail.qq.com/">点击登录qq邮箱</a>')


# 激活用户
def active(request, uid):
    active_user = UserInfo.users.get(id=uid)
    active_user.isActive = True
    active_user.save()
    return HttpResponse('用户已激活, <a href="/User/login/">点击登录</a>')


# 保存收货信息
def sendAddr(request):
    sendname = request.POST.get('sendname')
    addr = request.POST.get('site_area')
    iphone = request.POST.get('iphone')
    name = request.POST.get('name')
    user = UserInfo.users.filter(userName=name)
    uid = user[0].id
    userAdd = UserAddressInfo.address.create(sendname, addr, iphone, uid , 0)
    userAdd.save()
    return JsonResponse({'type': True})

# 显示收货地址
def showAdd(request):
    theAdd = UserAddressInfo.address.filter(uNow=True);
    tid = theAdd[0].id
    tname = theAdd[0].uName
    tadd = theAdd[0].uAddress
    tphone = theAdd[0].uPhone
    tp =tphone[3:7]
    tpx=tphone.replace(tp, '****')
    thead = {'tid':tid,'tname':tname,'tadd': tadd,'tphone':tpx}
    theAdd0 = UserAddressInfo.address.filter(uNow=0)
    list =[]
    for s in theAdd0:
        tphone =s.uPhone
        tp = tphone[3:7]
        tpx = tphone.replace(tp, '****')
        list.append({'tid': s.id, 'tname': s.uName, 'tadd': s.uAddress, 'tphone': tpx})
    context = {'thead':thead, 'list':list}
    return JsonResponse({'value':context})

# 修改当前收货地址
def upAdd(request):
    aid =request.GET.get('id')
    UserAddressInfo.address.update(aid, True)
    return JsonResponse({'ok':True})


# 显示重置密码页面
def forget(request):
    return render(request, 'User/forget.html')


# 发送重置密码邮件
def reset_send(request):
    name = request.POST.get('userName')
    the_user = UserInfo.users.filter(userName=name)
    uid = the_user[0].id
    uemail = the_user[0].userEmail

    # 任务加入celery中
    task.send_reset.delay(uid, uemail)
    return HttpResponse('重置密码邮件已发送至注册时的邮箱,请移步邮箱重置密码!<br/><br/><a href="https://mail.qq.com/">点击登录qq邮箱</a>')


# 新密码填写页面
def reset_show(request, uid):
    the_user = UserInfo.users.filter(id=uid)
    uname = the_user[0].userName
    return render(request, 'User/reset.html', {'uname': uname})


# 用新密码重写数据表
def reset_pwd(request):
    name = request.POST.get('uname')
    new_pwd = request.POST.get('user_pwd')
    # 密码sha1加密
    sh1 = sha1()
    sh1.update(new_pwd.encode('utf-8'))
    newpsw_sh1 = sh1.hexdigest()
    # 获取用户
    reset_user = UserInfo.users.get(userName=name)
    reset_user.userPsw = newpsw_sh1
    reset_user.save()
    return HttpResponse('用户密码已重置, <a href="/User/login/">点击登录</a>')

