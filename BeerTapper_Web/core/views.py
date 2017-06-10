from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_control

# Create your views here.

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def base(request):
    return render(request, "home.html")

def core(request):
    return HttpResponse("Hello, world. APP")

def index(request):
    return render(request, "index.html")
