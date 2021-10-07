from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

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

'''
def board_write(request):

    # form = CreateBoard()

    return render(request, "board_write.html")

def board_insert(request):
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    if btitle != "":
        rows = Board.objects.create(b_title=btitle, b_note=bnote, b_writer=bwriter)
        return redirect('/board')

    else:
        return redirect('/board_write')
'''
# 주문서 페이지 출력
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


    return render(request, 'sheet.html')

# 새로운 주문서 작성
def create_new_order(request):

    employee_name = request.GET['employee_name']
    order_date = request.GET['order_date']
    order_type_name = request.GET['order_type_name'] ### default: 전화
    customer = request.GET['customer']
    customer_phone = request.GET['customer_phone']
    delivery_option_name = request.GET['delivery_option_name'] ### default: 일반택배
    receipt_date = request.GET['receipt_date']
    receipt_hour = request.GET['receipt_hour']
    product_name = request.GET['product_name']
    size_option_name = request.GET['size_option_name']
    filling_option_name = request.GET['filling_option_name']
    sheet_option_name = request.GET['sheet_option_name']
    boxing_option_name = request.GET['boxing_option_name']
    phrase = request.GET['phrase']
    count = request.GET['count']
    total_price = request.GET['total_price']
    pay_check = request.GET['pay_check']
    pay_type_name = request.GET['pay_type_name'] ### default: 카드
    recipient = request.GET['recipient']
    recipient_phone = request.GET['recipient_phone']
    address1 = request.GET['address1']
    address2 = request.GET['address2']
    memo = request.GET['memo']
    status = request.GET['status']

    if employee_name & order_date & order_type_name & customer & customer_phone \
            & delivery_option_name & receipt_date & receipt_hour & product_name \
            & size_option_name & filling_option_name & sheet_option_name & boxing_option_name \
            & phrase & count & total_price & pay_check & pay_type_name & recipient & recipient_phone \
            & address1 & memo & status != "":

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
                status=status
        )
        return redirect('/list')

    else:
        return redirect('/order_sheet')


