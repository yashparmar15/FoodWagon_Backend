from django.shortcuts import render

from django.http import HttpResponse
from foodwagon_backend.models import Venues,Trucks
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail

def venuebyid(request,id):
    venue_list = Venues.objects.get(id = id)
    venue_dict = {'venue':venue_list}
    return render(request,'FoodWagon/venuebyid.html',context = venue_dict)

def truckbyid(request,id):
    truck_list = Trucks.objects.get(id = id)
    truck_dict = {'truck':truck_list}
    return render(request,'FoodWagon/truckbyid.html',context = truck_dict)


def index(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        message = request.POST['message']
        body = "Name: " + first_name + " " + last_name + "\n" + "\nMessage: " + message
        send_mail(
            'Message from ' + first_name + " " + last_name,
            body,
            email,
            ["yashparmar157000@gmail.com"],
            fail_silently= False
        )
        return render(request, 'FoodWagon/index.html', {'name' : first_name + " " + last_name})
    return render(request,'FoodWagon/index.html')

def adminlogin(request):
    return render(request,'FoodWagon/adminlogin.html')

def chef(request):
    return render(request,'FoodWagon/formcatering.html')

def catering(request):
    return render(request,'FoodWagon/catering.html')

def restaurent(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        message = request.POST['message']
        body = "Name: " + first_name + " " + last_name + "\nPhone number: "+ phone_number + "\nMassage: " + message
        send_mail(
            'Message from ' + first_name + " " + last_name,
            body,
            email,
            ["yashparmar157000@gmail.com"],
            fail_silently= False
        )
        return render(request, 'FoodWagon/restaurent.html', {'name' : first_name + " " + last_name})
    return render(request,'FoodWagon/restaurent.html')
def venue(request):
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
        print(venue_list)
    else:
        venue_list = Venues.objects.all()
    print(venue_list)
    paginator = Paginator(venue_list, 3) 
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

    


