from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse("ON The Home Page")

def about(request):
    return HttpResponse("ON The about")

def contact(request):
    return HttpResponse("ON The contact")


