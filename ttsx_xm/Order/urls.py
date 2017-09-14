from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$',views.showorder),
    url(r'^handle_order/$',views.handle_order),
]

