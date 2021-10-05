from django.urls import path

from . import views

app_name = "information"

urlpatterns = [
    path('regist', views.information, name='information'),
]