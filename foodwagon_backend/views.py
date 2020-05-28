from django.shortcuts import render,redirect

from django.http import HttpResponse
from foodwagon_backend.models import Venues,Trucks,Chef
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail

def chefbyid(request,id):
    chef_list = Chef.objects.get(id = id)
    chef_dict = {'chef':chef_list}
    return render(request,'FoodWagon/chefbyid.html',context = chef_dict)
def venuebyid(request,id):
    venue_list = Venues.objects.get(id = id)
    venue_dict = {'venue':venue_list}
    return render(request,'FoodWagon/venuebyid.html',context = venue_dict)

def truckbyid(request,id):
    truck_list = Trucks.objects.get(id = id)
    truck_dict = {'truck':truck_list}
    return render(request,'FoodWagon/truckbyid.html',context = truck_dict)

def service(request):
    if request.method == "POST":
        city = request.POST['city']
        service = request.POST['service']
        if service == "None":
            return render(request,'FoodWagon/index.html')
        if service == "venue":
            if city == "None":
                venue_list = Venues.objects.all()
                return render(request,'FoodWagon/venue.html',{'venues':venue_list})
            venue_list = Venues.objects.filter(City = city)
            return render(request,'FoodWagon/venue.html',{'venues':venue_list})
        if service == "foodtruck":
            truck_list = Trucks.objects.all()
            return render(request,'FoodWagon/foodtruck.html',{'trucks':truck_list})
        if service == "restaurent":
            return render(request,'FoodWagon/restaurant.html')
        return render(request,'FoodWagon/catering.html')
    return redirect('/')
        

        





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
    venue_list = Venues.objects.all()
    truck_list = Trucks.objects.all()
    return render(request,'FoodWagon/index.html',{'venuess':venue_list , 'truckss' : truck_list})

def adminlogin(request):
    return render(request,'FoodWagon/adminlogin.html')

def chef(request):
    return render(request,'FoodWagon/formcatering.html')

def catering(request):
    if request.method == 'POST':
        work = request.POST.getlist('work[]')
        name = request.POST['full_name']
        mobile = request.POST['mobile_number']
        email = request.POST['email']
        stipend = request.POST['stipend']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        area = request.POST['area']
        address = request.POST['address']
        spe = request.POST.getlist('special[]')
        work_type = request.POST['work_type']
        expert = request.POST['food_type_id']
        lic = request.POST['is_license']
        customer = request.POST['customer_strength']
        employee = request.POST['employee_id']
        image = request.POST['image']
        if customer == '':
            customer = 0
        Data = Chef(Work_As = work , Name = name , Phone = mobile , Email = email , Stipend = stipend , Country = country , State = state , City = city , Area = area , Address = address , Speciality = spe , Type = work_type , ExpertIn = expert , License = lic , Base = customer , EmployeeID = employee , Image = image)
        Data.save()
        chefs = Chef.objects.all()
        return render(request,'FoodWagon/catering.html',{'chefs':chefs})
    chefs = Chef.objects.all()
    return render(request,'FoodWagon/catering.html',{'chefs':chefs})

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

    


