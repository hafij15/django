from django.contrib import admin
from django.urls import path,include #here define the include for link child app. 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('aboutus/', views.about, name='about'),
    path('contactus/', views.contact, name='contact'),
    path('employee/', include('employee.urls')), # using this include connect with the main app portfolio.
]
