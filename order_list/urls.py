from django.urls import path

from order_list.views import first_test

app_name = "list"

urlpatterns = [
    path('first/', first_test, name='first'),
]