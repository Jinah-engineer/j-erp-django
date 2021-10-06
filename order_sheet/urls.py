from django.urls import path

from order_sheet.views import new_order

app_name = "sheet"

urlpatterns = [
    path('order_sheet/', new_order, name='order_sheet'),
]