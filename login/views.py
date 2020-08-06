from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.

def login(request):
    return render(request, 'login.html')

def my_logout(request):
    logout(request)
    return redirect('login')
