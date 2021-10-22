from django.http import HttpResponse

def home(request):
    return HttpResponse("This is our Home page")

def about(request):
    data = ("Get all data from database.")
    return HttpResponse(data)

def contact(request):
    return HttpResponse("This is our contact page.")
