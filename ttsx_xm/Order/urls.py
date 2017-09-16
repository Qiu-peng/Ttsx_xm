from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$',views.showorder),
    url(r'^handle_order/$',views.handle_order),
    url(r'^code/$',views.code),
    url(r'^delete/$', views.delete),  # 退出登录,删除cookie

]

