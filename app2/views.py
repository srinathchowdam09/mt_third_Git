from django.shortcuts import render

from django.http import HttpResponse

def sri(request):
    return HttpResponse('This is app2 first view')

def nath(request):
    return HttpResponse('This is app2 second view')

# Create your views here.
