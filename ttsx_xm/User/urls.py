#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register/$', views.register),
]