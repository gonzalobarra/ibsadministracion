# -*- encoding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.applogin, name='login'),
    url(r'^login_process/$', views.login_process, name='login_process'),
    url(r'^logout/$', views.applogout, name='logout'),
    url(r'^resumen/$', views.resumen, name='resumen'),
]