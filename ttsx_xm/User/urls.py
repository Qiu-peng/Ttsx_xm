from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^register/$', views.register),

    url('^login/$', views.login),
    url(r'^toLogin/$', views.toLogin),

    url(r'^user_center_info/$', views.center)

]