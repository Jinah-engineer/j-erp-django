from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *

# ajax
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def information(request):
    return render(request, 'information.html')


def employee_view(request):

    rsBoard = Employee.objects.all().order_by('-employee_id')

    if Employee.objects.first() is not None:
        last_id = Employee.objects.last().employee_id + 1
    else:
        last_id = 1

    context = {"last_id": last_id, "employee_table": rsBoard}

    return render(request, 'employee.html', context)


def emp_insert(request):
    emp_name = request.GET['emp_name']
    emp_rank = request.GET['emp_rank']
    emp_hire = request.GET['emp_hire']
    emp_auth = request.GET['emp_auth']
    if emp_name and emp_rank and emp_hire and emp_auth != "":
        rows = Employee.objects.create(employee_name=emp_name, employee_rank=emp_rank, employee_auth=emp_auth,
                                       hiredate=emp_hire)
        return redirect('information:emp_view')
    else:
        return redirect('information:emp_view')


# @csrf_exempt
# def emp_update(request):
#     emp_id = request.GET['employee_id']
#     emp_name = request.GET['emp_name']
#     emp_rank = request.GET['emp_rank']
#     emp_hire = request.GET['emp_hire']
#     emp_fire = request.GET['emp_fire']
#     emp_auth = request.GET['emp_auth']
#
#     try:
#         rows = Employee.objects.get(employee_id = emp_id)
#         if emp_name != "":
#             rows.employee_name = emp_name
#         if emp_rank != "":
#             rows.employee_rank = emp_rank
#         if emp_hire != "":
#             rows.hiredate = emp_hire
#


@csrf_exempt
def emp_delete(request):
    emp_id = request.GET['employee_id']
    print(emp_id)
    rows = Employee.objects.get(employee_id=emp_id).delete()

    data = {}
    data['result_msg'] = '삭제되었습니다'

    return JsonResponse(data, content_type="application/json")