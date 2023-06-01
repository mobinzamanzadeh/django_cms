from django.contrib import admin
from django.urls import path
from blog.views import post_list, post_detail

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
]

