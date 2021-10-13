# ---------- 박진아 작업 ----------
from django.urls import path

from order_list.views import *

app_name = "list"

urlpatterns = [
    path('orderlist/', order_list_view, name='orderlist'),
    path('orderdetail/', order_detail_view, name='orderdetail'),
]