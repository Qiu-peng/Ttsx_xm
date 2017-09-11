"""ttsx_xm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',include('Goods.urls')),  # 主页跳转
    url('^Goods/', include('Goods.urls')),  # 商品模块跳转
    url('^User/', include('User.urls')),    # 用户模块跳转
    url('^Order/', include('Order.urls')),  # 订单模块跳转
    url('^Cart/', include('Cart.urls')),  # 购物车模块跳转

]
