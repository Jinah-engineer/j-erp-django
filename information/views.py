from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
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

# modal view
@csrf_exempt
def emp_get(request):
    emp_id = request.GET['employee_id']
    emp = Employee.objects.get(employee_id = emp_id)
    data = model_to_dict(emp)
    print(data)

    return JsonResponse(data, content_type="application/json")

# page view
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
    if emp_name and emp_rank and emp_hire and emp_auth != "" and emp_auth != '==선택==':
        rows = Employee.objects.create(employee_name=emp_name, employee_rank=emp_rank, employee_auth=emp_auth,
                                       hiredate=emp_hire)
        return redirect('information:emp_view')
    else:
        return redirect('information:emp_view')


def emp_update(request):
    emp_id = request.GET['employee_id']
    emp_name = request.GET['employee_name']
    emp_rank = request.GET['employee_rank']
    emp_hire = request.GET['employee_hire']
    emp_fire = request.GET['employee_fire']
    emp_auth = request.GET['employee_auth']

    try:
        emp = Employee.objects.get(employee_id = emp_id)
        if emp_name != "":
            emp.employee_name = emp_name
        if emp_rank != "":
            emp.employee_rank = emp_rank
        if emp_hire != "":
            emp.hiredate = emp_hire
        if emp_fire != "":
            emp.firedate = emp_fire
        if emp_auth != "" and emp_auth != "==선택==":
            emp.employee_auth = emp_auth

        try:
            emp.save()
            return redirect('information:emp_view')
        except ValueError:
            return HttpResponse({"success": False, "msg":"에러가 발생했습니다"})

    except ObjectDoesNotExist:
        return HttpResponse({"success": False, "msg": "직원 정보가 존재하지 않습니다"})



@csrf_exempt
def emp_delete(request):
    emp_id = request.GET['employee_id']
    print(emp_id)
    rows = Employee.objects.get(employee_id=emp_id).delete()

    data = {}
    data['result_msg'] = '삭제되었습니다'

    return JsonResponse(data, content_type="application/json")