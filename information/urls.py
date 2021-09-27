from django.urls import path

from .views import first_test

app_name = "information"

urlpatterns = [
    path('first/', first_test, name='first'),
]