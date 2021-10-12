# ---------- 고기우 작업 ----------
from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('member_idcheck', views.member_idcheck, name='member_idcheck'),
    path('member_insert', views.member_insert, name='member_insert'),
]