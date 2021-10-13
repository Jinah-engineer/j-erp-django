# ---------- 박진아 작업 ----------
import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone

# from order_list.forms import ListCreationOrderForm
from information.models import Product, Delivery, Pay_type
from order_list.models import Order



'''
    구현 list

        1. 검색바 (search - module)
            1) 달력 API
            2) pagination 연동
            3) Ajax 화면 전환 버튼 (제작 대상, 출고 대상, 출고 완료 목록)
            4) 검색기능
        2. 주문 목록 인쇄 (PrintOrderList)
        3. Excel 주문 업로드 (UploadOrderList)
        4. Excel 주문 다운로드 (DownloadOrderList)
        5. 개별 주문장 출력 (PrintOrderSample)
        6. 주문 수정 (ModifyOrder)
        7. 주문 취소 (UndoOrder)
        8. 상태 변경 (ChangeOrderStatus)
            1) 주문 완료 (order_completed)
            2) 제작 완료 (produce_completed)
            3) 출고 완료 (release_completed)
        9. 정렬 (SortOrderList)
            1) 10개씩
            2) 50개씩
            3) 100개씩
        11. 페이지네이션 (pagination)
'''

    # print('---------here---------')
    #
    # pno = request.GET['pno']
    # print(pno)
    # print(type(pno))
    #
    # if request.is_ajax():
    #
    #     data = {
    #
    #         }
    #     print(data)
    #     print(type(data))
    #
    #     return JsonResponse(data)


# ====================== 전체 주문 목록
def order_list_view(request):

    orderDetail = Order.objects.all().order_by('-pno')
    delivery_table = Delivery.objects.all()
    pay_table = Pay_type.objects.all()

    context = {
        "orderDetail": orderDetail,
        "delivery_table": delivery_table,
        "pay_table": pay_table,

    }
    return render(request, "list.html", context)



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