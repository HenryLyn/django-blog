#!/usr/bin/python

from django.urls import path
from . import views

# add app name space
app_name = 'blog'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('article/?A<pk>[0-9]+/', views.detail, name = 'detail'), # add special url configuration
    path('archives/?A<year>[0-9]{4}/?A<month>{1, 2}/', views.archives, name = 'archives'), # add archives url
    path('category/?A<pk>[0-9]+/', views.category, name = 'category'), # add category url
]
