from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("This is our Home page")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render (request, 'contact.html')
