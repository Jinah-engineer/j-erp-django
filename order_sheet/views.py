# ---------- 박진아 작업 ----------
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from rest_framework.utils import json

from information.models import Product, Category
from order_list.models import Order

'''
    1. 주문 접수자
        - auto_created
        - icon 클릭 시 --> 주문 접수자 변경 가능하게 해야 함
    2. 주문 No.
        - auto_created
    3. 주문일자
        - auto_created
        - icon 클릭 시 --> 주문 일자 변경 가능하게 해야 함
    4. 주문 경로
        - 선택 시 --> value 넘겨주어야 함
    5. 고객명
        - 직접 입력
        - 한글/영어/숫자만 들어가게 해야 함
    6. 연락처
        - 01012341234
        - 010-1234-1234
    7. 수령방법
        - 선택 시 --> value 넘겨주어야 함
    8. 납품일자
        - icon 클릭하여 직접 선택
    9. 도착시간
        - icon 클릭하여 직접 선택
    10. 품목명
        - 첫 항목 기본 설정되어야 함
        - 상품 추가 시 품목 설정 항목 추가 되어야 함 (insert new row)
        - 품목이름 -> 자동 keyin
        - 옵션 추가 -> modal
        - 옵션 이름 -> modal 에서 받은 최종 value
        - 수량 -> 직접 입력
        - x 클릭 시 -> 항목 삭제 (alert 필요) + ajax
        - 금액 -> 수량까지 설정 후 --> auto_created

    11. 결제금액
        - default : 총 금액 value
        - but 변경 가능해야 함
        - 결과적으로 최종 value

    12. 결제버튼
        - 라디오 value 바꿔주기

    13. 결제방법
        - value 넘겨주어야 함

    14. 주문 고객과 동일인
        - 체크 시, 고객명, 고객 연락처 자동 입력됨

    15. 수령인 주소
        - 우편번호 검색 API 끌고 와야 함

    16. 주문메모
        - value 넘겨주어야 함

    17. 주문등록
        - list up 된 모든 value들 database 및 화면으로 최종적으로 넘겨주는 역할을 함
'''

# ====================== 주문서 페이지 출력
'''
    자동입력값 js 처리
        1. employee_name - login된 user_name
        2. order_no - 'current date' + '-' + 'order type value(A/B/C/D)' + '-' + '순서(for문?)'
        3. order_date - current date
'''
def new_order(request):
    # 주문 접수자 - employee_name (자동입력)
    # 주문 No. _ order_no (자동입력)
    # 주문일자 - order_date (default: 오늘날짜)

    products = Product.objects.all()
    categories = Category.objects.all()

    # products_name = Product.objects.values('product_name', 'product_name')
    # category_mid_Set = Category.objects.values('category_mid')
    # category_mid_Set_pick = Category.objects.values('category_mid').filter(category_mid='앙금플라워')
    # print(products_name)

    context = {
        "products": products,
        "categories": categories
    }

    return render(request, 'sheet.html', context)


# ====================== 품목 등록 / 자동 완성
def product_autocomplete(request):
    pass





# ====================== 품목 추가

'''
    1. 사용자가 품목명을 입력칸에 입력한다. 
    2. 입력된 값(자동완성 list 값)이 기존 데이터 (카테고리 이름, 품목 이름)과 일치하는지 확인한다.
    3. 카테고리 이름과 일치하는지 확인한다. 
    4. 카테고리 이름과 일치하면 category_id 를 갖게된다. 
    5. 이번에는 품목 이름과 가지고 있는 category_id가 일치하는지 확인한다.  
    6. 일치하면 품목 이름(product_name)을 입력값으로 확정한다. 
    
'''



# ====================== 새로운 주문서 작성
@csrf_exempt
def create_order(request):

    employee_name = request.POST.get('employee_name')
    order_date = request.POST.get('order_date')
    order_type_name = request.POST.get('order_type_name') ### default: 전화
    customer = request.POST.get('customer')
    customer_phone = request.POST.get('customer_phone')
    delivery_option_name = request.POST.get('delivery_option_name') ### default: 일반택배
    receipt_date = request.POST.get('receipt_date')
    receipt_hour = request.POST.get('receipt_hour')
    product_name = request.POST.get('product_name')
    size_option_name = request.POST.get('size-result')
    filling_option_name = request.POST.get('filling-result')
    sheet_option_name = request.POST.get('sheet-result')
    boxing_option_name = request.POST.get('boxing-result')
    phrase = request.POST.get('phrase-result')
    count = request.POST.get('count')
    total_price = request.POST.get('total_price')
    pay_check = request.POST.getlist('pay_check')
    pay_type_name = request.POST.get('pay_type_name') ### default: 카드
    recipient = request.POST.get('recipient')
    recipient_phone = request.POST.get('recipient_phone')
    address1 = request.POST.get('address1')
    address2 = request.POST.get('address2')
    memo = request.POST.get('memo')
    state = request.POST.get('state')



    if employee_name and order_date and order_type_name and customer and customer_phone \
            and delivery_option_name and receipt_date and receipt_hour and product_name \
            and size_option_name and filling_option_name and sheet_option_name and boxing_option_name \
            and phrase and count and total_price and pay_check and pay_type_name and recipient and recipient_phone \
            and address1 and state != "":

        rows = Order.objects.create(
            employee_name=employee_name,
            order_date=order_date,
            order_type_name=order_type_name,
            customer=customer,
            customer_phone=customer_phone,
            delivery_option_name=delivery_option_name,
            receipt_date=receipt_date,
            receipt_hour=receipt_hour,
            product_name=product_name,
            size_option_name=size_option_name,
            filling_option_name=filling_option_name,
            sheet_option_name=sheet_option_name,
            boxing_option_name=boxing_option_name,
            phrase=phrase,
            count=count,
            total_price=total_price,
            pay_check=pay_check,
            pay_type_name=pay_type_name,
            recipient=recipient,
            recipient_phone=recipient_phone,
            address1=address1,
            address2=address2,
            memo=memo,
            state=state
        )

        # 만약 사용자에게서 받아오는 product_name 과 DB 에서의 product_name 이 일치하면,
        #

        return redirect('list:orderlist')


    else:
        return redirect('sheet:order_sheet')


