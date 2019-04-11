from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^homepage/$', views.homepage),
    url(r'^homepagetem/$', views.homepage_tem),
    url(r'^post/(\w+)$', views.show_post),
    url(r'^about/$', views.about),
    url(r'^phone/', views.phone),
]


# Django架站的16堂课  -- 120