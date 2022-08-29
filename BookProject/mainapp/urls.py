from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
app_name='mainapp'
urlpatterns = [
    path('',home,name='home'),
    path('posts',posts,name='posts'),
    path('post/<int:pk>',posting,name='posting'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


