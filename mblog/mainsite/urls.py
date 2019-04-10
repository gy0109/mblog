from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^homepage/$', views.homepage),
    # url(r'^$', mainsite)
]