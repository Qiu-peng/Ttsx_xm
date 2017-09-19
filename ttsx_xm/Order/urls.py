from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.showorder),  # 订单页面显示
    url(r'^handle_order/$', views.handle_order),  # 提交订单处理
    url(r'^code/$', views.code),  # 生成二维码

]

