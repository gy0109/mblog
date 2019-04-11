from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^homepage/$', views.homepage),
    url(r'^homepagetem/$', views.homepage_tem),
    url(r'^post/(\w+)/$', views.show_post),
    url(r'^about/$', views.about),
    url(r'^abouttem/$', views.about_tem),
    url(r'^phone/$', views.phone),
    url(r'^phone/([0-9A-Za-z]+)/$', views.phone_sku),
]
