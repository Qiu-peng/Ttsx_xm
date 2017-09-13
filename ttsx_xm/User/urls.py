from django.conf.urls import url
from . import views

urlpatterns =[

    url(r'^register/$', views.register),
    url(r'^regist/$', views.regist),
    url(r'^ishere/$', views.ishere),

    url('^login/$', views.login),

    url('^toLogin/$', views.toLogin),
    url('^toindex/$', views.toindex),
    url('^cook_get/$', views.cook_get),
    url('^saveName/$', views.saveName),
    url('^readName/$', views.readName),
    url('^lockPwd/$', views.lockPwd),

    url(r'^user_center_info/$', views.center)

]