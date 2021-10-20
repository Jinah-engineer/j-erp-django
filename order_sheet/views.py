# ---------- 박진아 작업 ----------
import datetime
from django.http import JsonResponse, HttpResponse
import json
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from information.models import Product, Category, Order_type, Pay_type, Delivery, Size, Sheet, Filling, Boxing
from order_list.models import Order
from accounts.models import Member

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


# ====================== POST TEST
@csrf_exempt
def post_create(request):
    context = {}

    if request.method == "POST":
        bodydata = request.body.decode('utf-8')
        bodyjson = json.loads(bodydata)
        size = bodyjson['size']

    print(size)
    context['size'] = size
    context['result_msg'] = '통신성공'

    return JsonResponse(context, content_type="application/json")

# ====================== 주문서 페이지 출력
'''
    자동입력값 js 처리
        1. employee_name - login된 user_name
        2. order_no - 'current date' + '-' + 'order type value(A/B/C/D)' + '-' + '순서(for문?)'
        3. order_date - current date
'''


def new_order(request):

    context = {}
    #  ///////////////////////마감전에 주석해제
    # # 사용자 권한 제어==========================================
    if request.session.has_key('member_no'):
        memberno = request.session['member_no']
        membername = request.session['member_name']
        memberauth = request.session['member_auth']
    else:
        return redirect('accounts:signin')

    context["member_no"] = memberno
    context["member_name"] = membername
    context["member_auth"] = memberauth
    # =============================================================
    '''
        만약 이게 오늘(today)의 첫번째 주문이면, 
        = orderlist 에서 주문번호(order_no) 앞 8자리가 20211011 로 시작하는 주문이 없다면

            0000 -> 0001
            1로 시작
            20211011_A_001
            %04d' % num

        근데 이게 1번째가 아닌 주문이라면, 
            1) 직전 주문의 주문번호를 확인 (orderlist 에 있는 가장 마지막 주문 번호를 확인)
            2) 마지막 주문의 주문번호 끝자리에 + 1

    '''

    member = Member.objects.all() # 주문접수자 조회
    order_type = Order_type.objects.all() # 주문 경로 조회
    delivery = Delivery.objects.all() # 배송정보
    products = Product.objects.all() # 상품
    categories = Category.objects.all() # 상품분류
    sheet = Sheet.objects.all() #시트
    filling = Filling.objects.all()
    boxing = Boxing.objects.all()
    pay_type = Pay_type.objects.all()

    context["member_table"] = member
    context["order_type_table"] = order_type
    context["delivery_table"] = delivery
    context["products_table"] = products
    context["categories_table"] = categories
    context["sheet_table"] = sheet
    context["sheet_first"] = sheet.first()
    context["filling_table"] = filling
    context["filling_first"] = filling.first()
    context["boxing_table"] = boxing
    context["boxing_first"] = boxing.first()
    context["pay_type_table"] = pay_type

    print(sheet.first().sheet_name)
    print(filling.first().filling_price)
    print(boxing.first())

    return render(request, 'sheet.html', context)


@csrf_exempt
def option_view(request):
    context = {}
    product_name = request.GET['product_name']

    # 옵션테이블 조회
    if Product.objects.filter(product_name=product_name).exists():
        product = Product.objects.get(product_name=product_name)
        size = Size.objects.filter(product_id_id=product.product_id)
        context["product_price"] = int(product.product_price)
        context["flag"] = 1
        if size.exists():
            context["size"] = list(size.values())
        else:
            context["size"] = ''
    else:
        context["flag"] = 0

    return JsonResponse(context, content_type="application/json")


# ====================== 금액 계산
'''
    1. 품목 금액
        1) 품목 이름에 해당하는 금액 value 가져오기 (product.product_price) 
        2) 해당 value X 수량(count)
    
    2. 옵션 금액 
        1) 옵션별로 해당 옵션에 해당하는 금액 value 가져오기
        2) size 옵션
'''


@csrf_exempt
def product_price(request):
    context = {}

    if request.method == "POST":
        bodydata = request.body.decode('utf-8')
        bodyjson = json.loads(bodydata)
        size = bodyjson['size']


    return JsonResponse(context, content_type="application/json")


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

    # order_no
    order_no = '20211011-A-001'

    employee_name = request.POST.get('employee_name')
    order_date = request.POST.get('order_date')
    order_type_name = request.POST.get('order_type_name') ### default: 전화
    customer = request.POST.get('customer')
    customer_phone = request.POST.get('customer_phone')
    delivery_option_name = request.POST.get('delivery_option_name') ### default: 일반택배
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
    pay_type_name = request.POST.get('pay_type_name') ### default: 카드
    recipient = request.POST.get('recipient')
    recipient_phone = request.POST.get('recipient_phone')
    address1 = request.POST.get('address1')
    address2 = request.POST.get('address2')
    memo = request.POST.get('memo')
    state = request.POST.get('state')
    product_name = request.POST.get('product_name')

    ### 상품마다 조건이 달라져야 할 수도 있음
    if employee_name and order_date and order_type_name and customer and customer_phone \
            and delivery_option_name and receipt_date and receipt_hour and product_name \
            and count and total_price and pay_check and pay_type_name and recipient and recipient_phone \
            and address1 and state and product_name != "":

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
                state=state,
                order_no=order_no

                # order_no - 'current date' + '-' + 'order type value(A/B/C/D)' + '-' + '순서(for문?)'

            )
            return redirect('list:orderlist')

        except Exception as exc:
            print("문제가 생겼다..", exc)

    else:
        return redirect('sheet:order_sheet')
