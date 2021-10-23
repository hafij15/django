from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def employee(request):
    return HttpResponse("This is employee app page.")


def profile(request):
    #return HttpResponse("This is employee profile page.")
    emp_details = {
        'name' : "Hafijur Rahman",
        'email' : "hafij.sabuj@gmail.com",
        'phone' : 1736706699, 
        'age' : 29,
        'address' : "Vill: Shukchar, Post: Chartarapur, P.S: Pabna Sadar, Dist: Pabna",
    }
    return render(request, 'employee/profile.html', emp_details)