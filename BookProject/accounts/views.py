from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from .forms import SignupForm
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('mainapp:home')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('mainapp:home')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})