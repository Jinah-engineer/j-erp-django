from django.shortcuts import render

# Create your views here.

def first_test(request):
    return render(request, 'list.html')