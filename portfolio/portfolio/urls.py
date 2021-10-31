from django.contrib import admin
from django.urls import path,include #here define the include for link child app. 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('aboutus/', views.about, name='about'),
    path('contactus/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-details/', views.portfolioDetails, name='portfolio-details'),
    path('pricing/', views.pricing, name='pricing'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blogDetails, name='blog-details'),
    path('employee/', include('employee.urls')), # using this include connect with the main app portfolio.
]
