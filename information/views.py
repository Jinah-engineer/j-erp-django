from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def information(request):

    return render(request, 'information.html')


def employee_view(request):
    return render(request, 'employee.html')


def emp_insert(request):
    emp_name = request.GET['emp_name']
    emp_rank = request.GET['emp_rank']
    emp_hire = request.GET['emp_hire']
    emp_auth = request.GET['emp_auth']
    if emp_name and emp_rank and emp_hire and emp_auth != "":
        rows = Employee.objects.create(employee_name=emp_name, employee_rank=emp_rank, employee_auth=emp_auth, hiredate=emp_hire)
        return redirect('/employee')
    else:
        return redirect('/employee')
