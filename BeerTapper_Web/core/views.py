from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import never_cache

# Create your views here.

@never_cache
def base(request):
    return render(request, "home.html")

def core(request):
    return HttpResponse("Hello, world. APP")

def index(request):
    return render(request, "index.html")
