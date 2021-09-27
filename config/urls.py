
from django.contrib import admin
from django.urls import path, include

from account import views
from order_sheet import views
from order_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('account/', include('account.urls')),
    path('sheet/', include('order_sheet.urls')),
    path('list/', include('order_list.urls')),
    path('information/', include('information.urls')),
]
