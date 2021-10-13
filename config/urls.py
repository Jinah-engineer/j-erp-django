# ---------- 고기우, 박진아 공동 작업 ----------
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('order_list.urls')),

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('sheet/', include('order_sheet.urls')),
    path('list/', include('order_list.urls')),
    path('information/', include('information.urls')),
]
