from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def information(request):
    return render(request, 'information.html')