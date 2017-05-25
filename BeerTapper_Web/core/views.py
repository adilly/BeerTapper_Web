from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, "home.html")

def core(request):
    return HttpResponse("Hello, world. APP")

def index(request):
    return render(request, "index.html")
