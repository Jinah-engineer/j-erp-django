from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *

# ajax
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# product
def product_view(request):

    product = Product.objects.all().order_by('-product_id')
    category = Category.objects.all().order_by('category_id')

    if Product.objects.first() is not None:
        last_id = Product.objects.last().product_id + 1
    else:
        last_id = 1

    context = {"last_id": last_id, "product_table": product, "category_table": category}

    return render(request, 'product.html', context)


# size
def size_view(request):
    size = Size.objects.all().order_by('-size_id')
    if Size.objects.first() is not None:
        last_id = Size.objects.last().size_id + 1
    else:
        last_id = 1
    context = {"last_id": last_id, "size_table": size}

    return render(request, 'size.html', context)


# sheet
def sheets_view(request):
    sheets = Sheet.objects.all().order_by('-sheet_id')
    if Sheet.objects.first() is not None:
        last_id = Sheet.objects.last().sheet_id + 1
    else:
        last_id = 1
    context = {"last_id": last_id, "sheet_table": sheets}

    return render(request, 'sheets.html', context)


# filling
def filling_view(request):
    filling = Filling.objects.all().order_by('-filling_id')
    if Filling.objects.first() is not None:
        last_id = Filling.objects.last().filling_id + 1
    else:
        last_id = 1
    context = {"last_id": last_id, "filling_table": filling}

    return render(request, 'filling.html', context)


# order_type
def order_type_view(request):
    order_type = Order_type.objects.all().order_by('-order_type_id')
    if Order_type.objects.first() is not None:
        last_id = Order_type.objects.last().order_type_id + 1
    else:
        last_id = 1
    context = {"last_id": last_id, "order_type_table": order_type}

    return render(request, 'order_type.html', context)


# pay_type
def pay_type_view(request):
    pay_type = Pay_type.objects.all().order_by('-pay_type_id')
    if Pay_type.objects.first() is not None:
        last_id = Pay_type.objects.last().pay_type_id + 1
    else:
        last_id = 1
    context = {"last_id": last_id, "pay_type_table": pay_type}

    return render(request, 'pay_type.html', context)


# delivery
def delivery_view(request):
    delivery = Delivery.objects.all().order_by('-delivery_id')
    if Delivery.objects.first() is not None:
        last_id = Delivery.objects.last().delivery_id + 1
    else:
        last_id = 1
    context = {"last_id": last_id, "delivery_table": delivery}

    return render(request, 'delivery.html', context)


# boxing
def boxing_view(request):
    boxing = Boxing.objects.all().order_by('-boxing_id')
    if Boxing.objects.first() is not None:
        last_id = Boxing.objects.last().boxing_id + 1
    else:
        last_id = 1
    context = {"last_id": last_id, "boxing_table": boxing}

    return render(request, 'boxing.html', context)


# employee
def emp_get(request):
    emp_id = request.GET['employee_id']
    emp = Employee.objects.get(employee_id = emp_id)
    data = {"emp": emp}

    return JsonResponse(data, content_type="application/json")


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
def emp_update(request):
    return redirect('information:emp_view')
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



@csrf_exempt
def emp_delete(request):
    emp_id = request.GET['employee_id']
    print(emp_id)
    rows = Employee.objects.get(employee_id=emp_id).delete()

    data = {}
    data['result_msg'] = '삭제되었습니다'

    return JsonResponse(data, content_type="application/json")