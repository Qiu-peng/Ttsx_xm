# usr/bin/python3
# coding=utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),  # 调用首页视图
    url(r'^(\d+)/$', views.detail),

    url(r'^name=(\w{6,20})/$', views.login),  # 登录页跳转过来的首页显示

]



