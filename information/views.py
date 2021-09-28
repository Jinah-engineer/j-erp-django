from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
import information


def home(request):
    return render(request, 'home.html')