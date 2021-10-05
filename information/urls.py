from django.urls import path

from . import views

app_name = "information"

urlpatterns = [
    path('', views.information, name='information'),
    path('emp_view', views.employee_view, name='emp_view'),
    path('emp_insert', views.emp_insert, name='emp_insert'),
]