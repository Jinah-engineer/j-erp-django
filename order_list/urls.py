from django.urls import path

from order_list.views import order_detail_view

app_name = "list"

urlpatterns = [
    path('orderlist/', order_detail_view, name='orderlist'),
]