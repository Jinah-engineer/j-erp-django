# ---------- 고기우 작업 ----------
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from information.models import *

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
