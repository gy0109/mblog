from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^homepage/$', views.homepage),
    url(r'^homepagetem/$', views.homepage_tem),
    url(r'^post/(\w+)$', views.show_post),
]