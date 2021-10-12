# ---------- 고기우 작업 ----------
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Member
from datetime import datetime
from django.shortcuts import redirect
# Create your views here.


def signup_view(request):

    return render(request, "signup.html")


def member_register(request):

    return render(request, "signup.html")


@csrf_exempt
def member_idcheck(request):
    context = {}
    mid = request.GET['member_id']

    rs = Member.objects.filter(member_id=mid)
    if (len(rs)) > 0 :
        context['flag'] = 1
        context['result_msg'] = '중복된 아이디입니다.'
    else:
        context['flag'] = 0
        context['result_msg'] = '사용 가능한 아이디입니다.'

    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def member_insert(request):
    context = {}
    member_id = request.GET['member_id']
    member_pw = request.GET['member_pw']
    member_name = request.GET['member_name']
    member_email = request.GET['member_email']

    rs = Member.objects.create(member_id=member_id,
                               member_pw=member_pw,
                               member_name=member_name,
                               member_email=member_email,
                               usage_flag='1',
                               registdate=datetime.now()
                               )

    context['result_msg'] = '회원가입이 완료되었습니다.'

    return JsonResponse(context, content_type="application/json")


def login_view(request):
    return render(request, "login.html")