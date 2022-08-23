from telnetlib import LOGOUT
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import *
app_name='accounts'
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',logout,name='logout'),
    path('signup/',signup,name='signup'),
]
