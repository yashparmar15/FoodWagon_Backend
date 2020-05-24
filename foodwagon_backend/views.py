from django.shortcuts import render

from django.http import HttpResponse
from foodwagon_backend.models import Venues,Trucks
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def venuebyid(request,id):
    venue_list = Venues.objects.get(id = id)
    venue_dict = {'venue':venue_list}
    return render(request,'FoodWagon/venuebyid.html',context = venue_dict)

def truckbyid(request,id):
    truck_list = Trucks.objects.get(id = id)
    truck_dict = {'truck':truck_list}
    return render(request,'FoodWagon/truckbyid.html',context = truck_dict)


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
    venue_list = Venues.objects.all()
    paginator = Paginator(venue_list, 3) 
    page = request.GET.get('page')
    try:
        venues = paginator.page(page)
    except PageNotAnInteger:
        venues = paginator.page(1)
    except EmptyPage:
        venues = paginator.page(paginator.num_pages)
    venue_dict = {
        'venues':venues,
    }
    return render(request,'FoodWagon/venue.html',context = venue_dict)


def foodtruck(request):
    truck_list = Trucks.objects.order_by()
    truck_dict = {'trucks':truck_list}
    return render(request,'FoodWagon/foodtruck.html',context = truck_dict)

def login(request):
    return render(request,'FoodWagon/login.html')

def register(request):
    return render(request,'FoodWagon/register.html')


