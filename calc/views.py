from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Adrija'})
    
def calculate(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    operator = request.POST['operator']
    if operator=='add':
        res = val1 + val2
    elif operator=='subtract':
        res = val1 - val2
    elif operator=='multiply':
        res = val1 * val2
    elif operator=='divide':
        res = val1/val2
    return render(request, 'result.html',{'result':res})