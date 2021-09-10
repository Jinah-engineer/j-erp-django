from django.urls import path

import account.views
from account.views import *

app_name = "account"

urlpatterns = [
    path('index/', account.views.index, name='index')
]