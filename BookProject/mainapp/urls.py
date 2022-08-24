from django.contrib import admin
from django.urls import path,include
from .views import *
app_name='mainapp'
urlpatterns = [
    path('',home,name='home'),
    path('posts',posts,name='posts'),
    path('posts/<int:pk>',posting, name="posting"),
]


