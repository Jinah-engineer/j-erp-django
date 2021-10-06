from django.shortcuts import render, redirect
from django.utils import timezone
from requests import request

# from order_list.forms import ListCreationOrderForm
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
        10. 주문 목록 보여주기 (ReadOrderList)
            1) 주문 No. (model - order_id)
            2) 주문일자
            3) 진행상태
            4) 고객명
            5) 품목
            6) 사이즈
            7) 시트
            8) 필링
            9) 문구
            10) 수량
            11) 금액
            12) 주문경로
            13) 결제방법
            14) 결제여부
            15) 수령인
            16) 연락처
            17) 수령방법
            18) 수령주소
            19) 납품일자
            20) 주문메모
        11. 페이지네이션 (pagination)
'''

# def order_list_creation(request):
#     # create_list_order = ListCreationOrderForm(request.POST or None)
#     # create_list_order_item = ListCreationOrderItemForm(request.POST or None)
#
#     order = get_object_or_404(Order, pk=pk_no)
#
#     if request.method == 'POST':
#         order_list_form = ListCreationOrderForm(request.POST)
#         order_list_item_form = ListCreationOrderItemForm(request.POST)
#
#             if order_list_form.is_valid():
#                 order = form.save(commit=False)
#                 order.order_no = '20211006_A_001'
#                 order.order_date = timezone.now()
#                 order.save()
#                 return render(request, 'room.html')
#
#
#             elif order_list_item_form.is_valid():
#                 order = form.save(commit=False)
#                 order.order_no = '20211006_A_001'
#                 order.order_date = timezone.now()
#                 order.save()
#                 return render(request, 'room.html')
#
#     else:
#
#
#     context = {'order_list_form': order_list_form,
#                'order_list_item_form': order_list_item_form}
#
#     return render(request, 'index.html', context)

'''
    주문서 작성
'''
# def create_order(request):
#     pass
#     if request.method == 'POST':
#         form = ListCreationOrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.order_date = timezone.now()
#             order.save()
#             return redirect('list:list')
#
#     else:
#         form = ListCreationOrderForm()
#
#     context = {'form': form}
#     return render(request, 'list/first/list.html', context)

'''
    주문서 상세
'''
def order_detail_view(request):
    # pno = request.POST['pno']
    order_detail = Order.objects.all()

    return render(request, "list.html", {'order_detail': order_detail})