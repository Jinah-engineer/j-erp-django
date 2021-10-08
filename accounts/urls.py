# ---------- 고기우 작업 ----------
from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('regist', views.regist_view, name='regist'),
]