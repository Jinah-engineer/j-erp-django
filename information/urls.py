from django.urls import path

from . import views

app_name = "information"

urlpatterns = [
    path('', views.information, name='information'),
    path('employee_register', views.employee_register, name='employee_register'),
]