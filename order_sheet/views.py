from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from order_list.models import Order
from order_sheet.forms import SheetCreationOrder, SheetCreationOrderItem


def first_test(request):
    return render(request, 'sheet.html')


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


class OrderSheetCreation(CreateView):
    model = Order
    form_class = SheetCreationOrder, SheetCreationOrderItem
    context_object_name = 'order_sheet'
    template_name = 'sheet/first/sheet.html'

    # def form_valid(self, form):
    #     temp_order = form.save(commit=False)
    #     temp_order.writer = self.request.user
    #     temp_order.save()
    #     return super().form_valid(form)
    #
    # def get_success_url(self):
    #     return reverse('articleapp:detail', kwargs={'pk': self.object.pk})