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

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            request, username=username, password=password
        )

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, "login.html", {
                'error': 'Username or Password is incorrect.',
            })
    else:
        return render(request, "login.html")