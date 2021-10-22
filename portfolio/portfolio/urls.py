from django.contrib import admin
from django.urls import path,include #here define the include for link child app. 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('aboutus/', views.about),
    path('contactus/', views.contact),
    path('employee/', include('employee.urls')), # using this include connect with the main app portfolio.
]
