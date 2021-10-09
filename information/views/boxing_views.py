from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
# ajax
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from ..models import Employee


# boxing

# modal view
@csrf_exempt
def boxing_get(request):
    emp_id = request.GET['employee_id']
    emp = Employee.objects.get(employee_id = emp_id)
    data = model_to_dict(emp)
    print(data)

    return JsonResponse(data, content_type="application/json")


# page view
def boxing_view(request):

    rsBoard = Employee.objects.all().order_by('-employee_id')

    if Employee.objects.first() is not None:
        last_id = Employee.objects.last().employee_id + 1
    else:
        last_id = 1

    context = {"last_id": last_id, "employee_table": rsBoard}

    return render(request, 'employee.html', context)


# boxing insert
def boxing_insert(request):
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


# boxing update
def boxing_update(request):
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


# boxing delete
def boxing_delete(request):
    emp_id = request.GET['employee_id']
    rows = Employee.objects.get(employee_id=emp_id).delete()

    return redirect('information:emp_view')