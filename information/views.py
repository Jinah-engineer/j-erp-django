from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.


def information(request):

    form = EmployeeForm(request.POST)

    return render(request, 'information.html', {'form': form})

