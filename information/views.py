from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
import information


def first_test(request):
    return render(request, 'information.html')