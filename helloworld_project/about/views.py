from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageView_A(request):
    return HttpResponse('And once again... Hello, World!')