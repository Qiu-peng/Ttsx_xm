from django.conf.urls import url
from . import views

urlpatterns =[

    url(r'^register/$', views.register),  # 显示注册页
    url(r'^regist/$', views.regist),  # 处理注册信息
    url(r'^ishere/$', views.ishere),  # 判断用户名是否存在

    url('^login/$', views.login),  # 显示登录页

    url('^toLogin/$', views.toLogin),  # 处理密码匹配
    url('^toindex/$', views.toindex),  # 记录并返回用户名
    url('^cook_get/$', views.cook_get),
    url('^readName/$', views.readName),
    url('^remember/$', views.remember),
    url('^clearSession/$', views.clearSession),

    url(r'^user_center/$', views.center),  # 跳转用户中心
    url(r'^user_order/$', views.center_order),
    url(r'^user_site/$', views.center_site),
]