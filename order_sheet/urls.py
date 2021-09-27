from django.urls import path

from order_sheet.views import first_test

app_name = "sheet"

urlpatterns = [
    path('first/', first_test, name='first'),
]