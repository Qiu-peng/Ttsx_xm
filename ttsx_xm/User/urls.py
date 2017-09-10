from django.conf.urls import url
from . import views

urlpatterns =[
    url('^login/$', views.login ),
    url('^register/$', views.register),

]