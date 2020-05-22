from django.shortcuts import render

from django.http import HttpResponse
from foodwagon_backend.models import Venues
def index(request):
    return render(request,'FoodWagon/index.html')

def adminlogin(request):
    return render(request,'FoodWagon/adminlogin.html')

def chef(request):
    return render(request,'FoodWagon/formcatering.html')

def catering(request):
    return render(request,'FoodWagon/catering.html')

def restaurent(request):
    return render(request,'FoodWagon/restaurent.html')

def venue(request):
    venue_list = Venues.objects.order_by('Venue_Name')
    venue_dict = {'venue_records':venue_list}
    return render(request,'FoodWagon/venue.html',context = venue_dict)

def foodtruck(request):
    return render(request,'FoodWagon/foodtruck.html')

def login(request):
    return render(request,'FoodWagon/login.html')

def register(request):
    return render(request,'FoodWagon/register.html')


