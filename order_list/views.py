# ---------- 박진아 작업 ----------
import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone

# from order_list.forms import ListCreationOrderForm
from information.models import Product, Delivery, Pay_type, Order_type
from order_list.models import Order

# ====================== 전체 주문 목록
def order_list_view(request):

    if request.session.has_key('member_no'):
        memberno = request.session['member_no']
        membername = request.session['member_name']
        memberauth = request.session['member_auth']
    else:
        return redirect('accounts:signin')

    orderDetail = Order.objects.all().order_by('-pno')
    delivery_table = Delivery.objects.all()
    pay_table = Pay_type.objects.all()
    order_type_table = Order_type.objects.all()

    order_completed = "주문완료"
    production_completed = "제작완료"
    release_completed = "출고완료"


    context = {
        "member_no" : memberno,
        "member_name" : membername,
        "member_auth" : memberauth,
        "orderDetail": orderDetail,
        "delivery_table": delivery_table,
        "pay_table": pay_table,
        "order_type_table": order_type_table,
        "order_completed": order_completed,
        "production_completed": production_completed,
        "release_completed": release_completed,
    }

    if request.method == 'POST':
        data = json.loads(request.body)
        context = {

        }
        return JsonResponse(context)


    return render(request, "list_test.html", context)


# ====================== 주문 상세
def order_detail_view(request):
    if request.method == 'GET':
        pno = request.GET['pno']
        print(pno)
        print(type(pno))
        data = {
            "pno": pno
        }
        print(data)
        print(type(data))

        return JsonResponse(data, content_type="application/json")


# ====================== 목록 변경
# def change_list_view(request):
#
#     order_completed_list = Order.object.all().filter(state="주문완료").order_by('-pno')
#     production_completed_list = Order.object.all().filter(state="제작완료").order_by('-pno')
#     release_completed_list = Order.object.all().filter(state="출고완료").order_by('-pno')
#
#     data = {
#         "order_completed_list": order_completed_list,
#         "production_completed_list": production_completed_list,
#         "release_completed_list": release_completed_list,
#     }
#
#     return JsonResponse(data, content_type="application/json")



# ====================== 주문 수정
def order_modify_view(request):
    # order_no
    order_no = '20211011-A-001'

    employee_name = request.GET.get('employee_name')
    order_date = request.GET.get('order_date')
    order_type_name = request.GET.get('order_type_name')  ### default: 전화
    customer = request.GET.get('customer')
    customer_phone = request.POST.get('customer_phone')
    delivery_option_name = request.POST.get('delivery_option_name')  ### default: 일반택배
    receipt_date = request.POST.get('receipt_date')
    receipt_hour = request.POST.get('receipt_hour')
    size_option_name = request.POST.get('size-result')
    filling_option_name = request.POST.get('filling-result')
    sheet_option_name = request.POST.get('sheet-result')
    boxing_option_name = request.POST.get('boxing-result')
    phrase = request.POST.get('phrase-result')
    count = request.POST.get('count')
    total_price = request.POST.get('total_price')
    pay_check = request.POST.get('radio-result')
    pay_type_name = request.POST.get('pay_type_name')  ### default: 카드
    recipient = request.POST.get('recipient')
    recipient_phone = request.POST.get('recipient_phone')
    address1 = request.POST.get('address1')
    address2 = request.POST.get('address2')
    memo = request.POST.get('memo')
    state = request.POST.get('state')
    product_name = request.POST.get('product_name')

    ### 상품마다 조건이 달라져야 할 수도 있음
    # if employee_name and order_date and order_type_name and customer and customer_phone \
    #         and delivery_option_name and receipt_date and receipt_hour and product_name \
    #         and count and total_price and pay_check and pay_type_name and recipient and recipient_phone \
    #         and address1 and state and product_name != "":

    print('='*20, '수정시작', '='*20)
    print(employee_name)
    print(order_date)
    print(order_type_name)
    print(customer)
    print(customer_phone)
    print(delivery_option_name)
    print(receipt_date)
    print(receipt_hour)
    print(product_name)
    print(size_option_name)
    print(sheet_option_name)
    print(filling_option_name)
    print(boxing_option_name)
    print(phrase)
    print(count)
    print(total_price)
    print(pay_check)
    print(type(pay_check))
    print(pay_check[0])
    print(pay_type_name)
    print(recipient)
    print(recipient_phone)
    print(address1)
    print(address2)
    print(memo)
    print(order_no)

    try:
        # match with db
        # db_order = Order.ob


        # save
        temp_modify_order = Order.objects.save()
        return redirect('list:orderlist')

    except Exception as exc:
        print("문제가 생겼다..", exc)

    # else:
    return redirect('sheet:order_sheet')