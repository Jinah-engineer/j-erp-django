# ---------- 박진아 작업 ----------
from django.urls import path

from order_sheet.views import create_order, new_order

app_name = "sheet"

urlpatterns = [
    path('order_sheet/', new_order, name='order_sheet'),
    path('create_order/', create_order, name='create_order'),

]