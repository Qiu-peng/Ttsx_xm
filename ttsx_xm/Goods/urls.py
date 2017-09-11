# usr/bin/python3
# coding=utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),  # 调用首页视图
    url(r'^(\d+)/$',views.detail),
]



