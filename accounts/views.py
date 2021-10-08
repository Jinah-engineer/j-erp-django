# ---------- 고기우 작업 ----------
from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
# Create your views here.


def login_view(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        user_pw = request.POST["user_pw"]
        user = authenticate(username=user_id, password=user_pw)

        if user is not None:
            print("로그인 성공")
            login(request, user)
            return redirect("list:first")
        else:
            print("로그인 실패")

    return render(request, "login.html")

def logout_view(request):

    logout(request)

    return redirect("accounts:login")

def regist_view(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]

    return render(request, "regist.html")