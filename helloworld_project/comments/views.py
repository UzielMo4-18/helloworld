from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView_C(request):
    return HttpResponse('For second time, Hello, World!')