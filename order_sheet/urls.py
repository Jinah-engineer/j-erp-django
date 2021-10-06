from django.urls import path

from order_sheet.views import new_order

app_name = "sheet"

urlpatterns = [
    path('first/', new_order, name='first'),
]