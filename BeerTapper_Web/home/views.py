from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_control

# Create your views here.

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def home(request):
<<<<<<< HEAD
    return render(request, "home.html")
=======
    '''Returns Basic HTML Webpage. This is my playground'''
    return render(request, "home.html")
# Create your views here.
>>>>>>> b2f138e... Added doctring to home view
