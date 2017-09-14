from django.conf.urls import url
from . import views



urlpatterns=[

    url('^cart/$', views.cart),

    url(r'^delete/$', views.delete),  # 退出登录,删除cookie
]


