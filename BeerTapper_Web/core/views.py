from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def base(request):
    return HttpResponse("HOME")

def core(request):
    return HttpResponse("Hello, world. APP")

def index(request):
    return render(request, "index.html")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



