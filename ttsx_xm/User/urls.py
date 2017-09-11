from django.conf.urls import url
from . import views

urlpatterns =[

    url(r'^register/$', views.register),

    url('^login/$', views.login),

    url('^toLogin/$', views.toLogin),
    url('^toindex/$', views.toindex),

    url(r'^user_center_info/$', views.center)

]