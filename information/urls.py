# ---------- 고기우 작업 ----------
from django.urls import path

from information import views

app_name = "information"

urlpatterns = [
    path('product', views.product_view, name='product_view'),
    path('size', views.size_view, name='size_view'),
    path('sheets', views.sheets_view, name='sheets_view'),
    path('filling', views.filling_view, name='filling_view'),
    path('order_type', views.order_type_view, name='order_type_view'),
    path('pay_type', views.pay_type_view, name='pay_type_view'),
    path('delivery', views.delivery_view, name='delivery_view'),
    path('boxing', views.boxing_view, name='boxing_view'),

    path('emp', views.employee_view, name='emp_view'),
    path('emp_get', views.emp_get, name='emp_get'),
    path('emp_insert', views.emp_insert, name='emp_insert'),
    path('emp_update', views.emp_update, name='emp_update'),
    path('emp_delete', views.emp_delete, name='emp_delete'),
]
