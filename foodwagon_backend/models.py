from django.db import models
from phone_field import PhoneField
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
