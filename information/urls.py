# ---------- 고기우 작업 ----------
from django.urls import path
from information.views import views
from information.views import emp_views

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
