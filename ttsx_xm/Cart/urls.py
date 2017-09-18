from django.conf.urls import url
from . import views

urlpatterns=[
    url('^cart/$',views.cart),
    url(r'^add/$',views.add),
    url(r'^edit/$',views.edit),
    url(r'^remove/$',views.remove),
]



