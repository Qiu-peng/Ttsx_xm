# usr/bin/python3
# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),  # 调用首页视图
    url(r'^(\d+)/$', views.detail),
    url(r'^list(\d+)/$', views.list),

    url(r'^getname/$', views.getname),  # 从cookie获取用户名
    url(r'^delete/$', views.delete),  # 退出登录,删除cookie

]
