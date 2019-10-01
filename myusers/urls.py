from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from . import views
urlpatterns = [
      url(r'^users/$', views.displayUsers, name='users'),
      url(r'^users/(?P<id>\d+)/$', views.displayDetails, name='details'),
      #re_path('^$', views.displayUsers, name = 'users'),
]
