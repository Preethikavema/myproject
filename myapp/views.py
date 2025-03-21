from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home(request):
    return HttpResponse("Hello! Welcome to home page")
def firstpage(request):
    return HttpResponse("Hello! Welcome to first page")
def secondpage(request):
    return HttpResponse("Hello! Welcome to second page")
def thirdpage(request):
    return HttpResponse("Hello! Welcome to third page")
def html(request):
    template=loader.get_template('student.html')
    return HttpResponse(template.render())

# Create your views here.
