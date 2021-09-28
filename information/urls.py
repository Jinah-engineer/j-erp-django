from django.urls import path

from . import views

app_name = "information"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.information, name='information'),
]