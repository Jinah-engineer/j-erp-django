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
def new_order(request):
    return render(request, 'sheet.html')

# 새로운 주문서 작성
# def create_new_order(request):
    # 주문 접수자 - employee_name
    # 주문 No. _ order_no
    # 주문일자 - order_date
    # 주문 경로 - order_type_name
    # 고객명 - customer
    # 연락처 - customer_phone
    # 수령방법 - delivery_option_name
    # 납품일자 - receipt_date
    # 도착시간 - receipt_hour
    # 품목이름 - product_name
    # 사이즈옵션 - size_option_name
    # 필링옵션 - filling_option_name
    # 시트옵션 - sheet_option_name
    # 포장옵션 - boxing_option_name
    # 문구옵션 - phrase
    # 수량 - count
    # 결제 금액 - total_price
    # 결제 여부 - pay_check
    # 결제 방법 - pay_type_name
    # 수령인명 - recipient
    # 수령인 연락처 - recipient_phone
    # 수령인 주소 - address1
    # 수령인 상세주소 - address2
    # 주문메모 - memo
    # 상태 - status


    # return redirect('/list')

