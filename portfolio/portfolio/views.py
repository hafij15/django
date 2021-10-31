from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("This is our Home page")
    return render(request, 'index.html')

def about(request):
    return render(request, '../templates/pages/about.html')

def contact(request):
    return render (request, '../templates/pages/contact.html')

def team(request): 
    return render (request, '../templates/pages/team.html')

def testimonial(request): 
    return render (request, '../templates/pages/testimonial.html')

def services(request): 
    return render(request, '../templates/pages/services.html')

def portfolio(request): 
    return render(request, '../templates/pages/portfolio.html')

def portfolioDetails(request): 
    return render(request, '../templates/pages/portfolio-details.html')

def pricing(request): 
    return render(request, '../templates/pages/pricing.html')

def blog(request): 
    return render(request, '../templates/pages/blog.html')

def blogDetails(request): 
    return render(request, '../templates/pages/blog-details.html')