# ---------- 고기우 작업 ----------
from django.urls import path
from information.views import views, emp_views, boxing_views, delivery_views, filling_views

app_name = "information"

urlpatterns = [
    path('product', views.product_view, name='product_view'),
    path('size', views.size_view, name='size_view'),
    path('sheets', views.sheets_view, name='sheets_view'),
    path('order_type', views.order_type_view, name='order_type_view'),
    path('pay_type', views.pay_type_view, name='pay_type_view'),

    path('filling', filling_views.filling_view, name='filling_view'),
    path('filling_get', filling_views.filling_get, name='fillingy_get'),
    path('filling_insert', filling_views.filling_insert, name='filling_insert'),
    path('filling_update', filling_views.filling_update, name='filling_update'),
    path('filling_delete', filling_views.filling_delete, name='filling_delete'),

    path('delivery', delivery_views.delivery_view, name='delivery_view'),
    path('delivery_get', delivery_views.delivery_get, name='delivery_get'),
    path('delivery_insert', delivery_views.delivery_insert, name='delivery_insert'),
    path('delivery_update', delivery_views.delivery_update, name='delivery_update'),
    path('delivery_delete', delivery_views.delivery_delete, name='delivery_delete'),

    path('emp', emp_views.employee_view, name='emp_view'),
    path('emp_get', emp_views.emp_get, name='emp_get'),
    path('emp_insert', emp_views.emp_insert, name='emp_insert'),
    path('emp_update', emp_views.emp_update, name='emp_update'),
    path('emp_delete', emp_views.emp_delete, name='emp_delete'),

    path('boxing', boxing_views.boxing_view, name='boxing_view'),
    path('boxing_get', boxing_views.boxing_get, name='boxing_get'),
    path('boxing_insert', boxing_views.boxing_insert, name='boxing_insert'),
    path('boxing_update', boxing_views.boxing_update, name='boxing_update'),
    path('boxing_delete', boxing_views.boxing_delete, name='boxing_delete'),
]
