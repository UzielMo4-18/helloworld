from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def CommentsView(request):
    return render(request,'comments.html',{})