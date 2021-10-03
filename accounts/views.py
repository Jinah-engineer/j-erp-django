from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
# Create your views here.


def login_view(request):

    return render(request, "login.html")

def logout_view(request):

    return redirect("accounts:login")

def regist_view(request):

    return render(request, "regist.html")