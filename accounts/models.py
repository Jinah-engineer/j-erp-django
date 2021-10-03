from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class User(AbstractUser):
    fullName = models.CharField(max_length=20)
    address = models.TextField(max_length=255)
    phone = models.CharField(max_length=11)
    hiredate = models.DateTimeField(default=datetime.now, blank=True)