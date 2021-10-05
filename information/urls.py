from django.urls import path

from . import views

app_name = "information"

urlpatterns = [
    path('', views.information, name='information'),
    path('emp', views.emp, name='emp'),
]