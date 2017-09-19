from django.conf.urls import url
from . import views

urlpatterns =[

    url(r'^register/$', views.register),  # 显示注册页
    url(r'^regist/$', views.regist),  # 处理注册信息
    url(r'^ishere/$', views.ishere),  # 判断用户名是否存在

    url('^login/$', views.login),  # 显示登录页

    url('^toLogin/$', views.toLogin),  # 处理密码匹配
    url('^login_out/$', views.login_out),  # 退出登录

    url('^toindex/$', views.toindex),  # 记录并返回用户名
    url('^readName/$', views.readName),  # 读用户名
    url('^remember/$', views.remember),
    url('^clearSession/$', views.clearSession),

    url(r'^user_center/$', views.center),  # 跳转用户中心
    url(r'^user_order/$', views.center_order),
    url(r'^user_site/$', views.center_site),

    url(r'^verify_code/$', views.verify_code),  # 验证码
    url(r'^yzm/$', views.yzm),

    url(r'^send(\d+)/$', views.send),  # 发送邮件
    url(r'^active(\d+)/$', views.active),  # 激活用户

    url('^sendAddr/$', views.sendAddr),  # 收货地址
    url('^showAdd/$', views.showAdd),  # 显示收货地址
    url('^upAdd/$', views.upAdd),  # 修改当前收货地址
    url('^delAdd/$', views.delAdd),  # 删除收货地址
    url('^updateAdd/$', views.updateAdd),  # 自动填写地址
    url('^uptoAddr/$', views.uptoAddr),  # 修改收货地址

    url(r'^forget/$', views.forget),  # 忘记密码页显示
    url(r'^reset_send/$', views.reset_send),  # 给用户发送重置邮件
    url(r'^reset_show(\d+)/$', views.reset_show),  # 用户填写新密码
    url(r'^reset_pwd/$', views.reset_pwd),   # 将用户新密码填入数据库

]


