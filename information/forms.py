from django.forms import ModelForm
from django import forms
from .models import *


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name', 'employee_rank', 'hiredate', 'employee_auth']


class empForm(forms.Form):
    emp_name = forms.CharField(label='emp_name')
    emp_rank = forms.CharField(label='emp_rank')
    emp_hire = forms.DateTimeField(label='emp_hire')
    emp_auth = forms.CharField(label='emp_auth')

