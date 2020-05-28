from django.db import models
from phone_field import PhoneField
from django.contrib.postgres.fields import ArrayField
class Venues(models.Model):
    Venue_Name = models.CharField(max_length = 50 , null = False , blank = False)
    Maximum_Guest = models.IntegerField(null = False , blank = False)
    Price_per_Day = models.IntegerField(null = False, blank = False)
    Address = models.CharField(max_length = 255 , null = False , blank = False)
    City = models.CharField(max_length = 50 , null = False , blank = False)
    Phone = models.CharField(blank=False, help_text='Contact phone number',default=0,max_length=15)
    image1 = models.ImageField(upload_to='picture/', max_length=255,null = True,blank = True)
    image2 = models.ImageField(upload_to='picture/', max_length=255,null = True,blank = True)
    image3 = models.ImageField(upload_to='picture/', max_length=255,null = True,blank = True)
    image4 = models.ImageField(upload_to='picture/', max_length=255,null = True,blank = True)
    image5 = models.ImageField(upload_to='picture/', max_length=255,null = True,blank = True)
    def __str__(self):
        return str(self.Venue_Name)

class Trucks(models.Model):
    Model_Name = models.CharField(max_length = 50 , null = False , blank = False)
    Price = models.IntegerField(null = False, blank = False)
    Description = models.CharField(max_length = 255 , null = False , blank = False)
    image1 = models.ImageField(upload_to='picture/', max_length=255,null = True,blank = True)
    image2 = models.ImageField(upload_to='picture/', max_length=255,null = True,blank = True)
    image3 = models.ImageField(upload_to='picture/', max_length=255,null = True,blank = True)
    image4 = models.ImageField(upload_to='picture/', max_length=255,null = True,blank = True)
    image5 = models.ImageField(upload_to='picture/', max_length=255,null = True,blank = True)
    def __str__(self):
        return str(self.Model_Name)

class Chef(models.Model):
    Work_As = ArrayField(ArrayField(models.CharField(max_length = 200 , null = False , blank = False)))
    Name = models.CharField(max_length = 50 , null = False , blank = False)
    Phone = models.CharField(max_length = 15 , null = False , blank = False)
    Email = models.EmailField(max_length = 50 , null = True , blank = True)
    Stipend = models.IntegerField(null = True , blank = True)
    Country = models.CharField(null = False , max_length = 50 , blank = False , default = "India")
    State = models.CharField(max_length = 100 , null = False , blank = False)
    City = models.CharField(max_length = 100 , null = False , blank = False)
    Area = models.CharField(max_length = 250 , null = False , blank = False)
    Address = models.CharField(max_length = 255 , null = False , blank = False)
    Speciality = ArrayField(ArrayField(models.CharField(max_length = 250 , null = False , blank = False)))
    Type = models.CharField(max_length = 15 , null = False , blank = False)
    ExpertIn = models.CharField(max_length = 100 , null = False , blank = False)
    License = models.CharField(max_length = 5 , null = False , blank = False)
    Base = models.CharField(max_length = 100 ,null = True , blank = True)
    EmployeeID = models.CharField(max_length = 100,null = True , blank = True)
    Image = models.ImageField(upload_to='picture/', max_length=255,null = True,blank = True)
    def __str__(self):
        return str(self.Name)
    

