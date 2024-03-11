from django.shortcuts import render

from .models import Iris
from .form import IrisForm

def predection(request):
    form = IrisForm()
    return render(request , 'iris.html',{'form':form})

