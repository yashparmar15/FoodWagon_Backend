from django.shortcuts import render

from django.http import HttpResponse

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
    return render(request,'FoodWagon/venue.html')

def foodtruck(request):
    return render(request,'FoodWagon/foodtruck.html')

def login(request):
    return render(request,'FoodWagon/login.html')

def register(request):
    return render(request,'FoodWagon/register.html')


