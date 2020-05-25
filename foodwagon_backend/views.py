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
    if request.method == "POST":
        print(request.POST['city'])
        print(request.POST['sort'])
    venue_list = Venues.objects.all()
    venue_lis = Venues.objects.all()
    if request.method == "POST":
        city = request.POST['city']
        Sor = request.POST['sort']
        if city != "None":
            if Sor == "lowtohigh":
                venue_list = Venues.objects.filter(City= city).order_by('Price_per_Day')
            else:
                venue_list = Venues.objects.filter(City= city).order_by('Price_per_Day').reverse()
        else:
            if Sor == "lowtohigh":
                venue_list = Venues.objects.order_by('Price_per_Day')
            else:
                venue_list = Venues.objects.order_by('Price_per_Day').reverse()
    else:
        venue_list = Venues.objects.all()
    paginator = Paginator(venue_list, 3) 
    if request.method == "POST":
        page = request.POST.get('page')
    else:
        page = request.GET.get('page')
    try:
        venues = paginator.page(page)
    except PageNotAnInteger:
        venues = paginator.page(1)
    except EmptyPage:
        venues = paginator.page(paginator.num_pages)
    venue_dict = {
        'venues':venues,'venues_list':venue_lis
    }
    return render(request,'FoodWagon/venue.html',context = venue_dict)


def foodtruck(request):
    truck_list = Trucks.objects.all()
    paginator = Paginator(truck_list, 3) 
    page = request.GET.get('page')
    try:
        trucks = paginator.page(page)
    except PageNotAnInteger:
        trucks = paginator.page(1)
    except EmptyPage:
        trucks = paginator.page(paginator.num_pages)
    truck_dict = {
        'trucks':trucks,
    }
    return render(request,'FoodWagon/foodtruck.html',context = truck_dict)

def login(request):
    return render(request,'FoodWagon/login.html')

def register(request):
    return render(request,'FoodWagon/register.html')


