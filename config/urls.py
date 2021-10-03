from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('sheet/', include('order_sheet.urls')),
    path('list/', include('order_list.urls')),
    path('information/', include('information.urls')),
]
