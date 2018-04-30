#!/usr/bin/python3
from django.urls import path
from . import views

app_name = 'comment'
urlpatterns = [
    path('comment/post/(?A<pk>[0-9]+)/', views.article_comment, name = 'article_comment')
]
