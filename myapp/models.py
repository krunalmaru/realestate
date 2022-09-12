from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django import forms
import datetime
# Create your models here.

class Builder(models.Model):
    profileimg = models.ImageField(upload_to='image/profile')
    name = models.CharField(max_length=100)
    email = models.EmailField(default='') 
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=1000,default='')
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    agencyname = models.CharField(max_length=100)   
    
    def __str__(self):
        return self.name
  

class Scheam(models.Model):
    CHOICE = (
        ('Residential','Residential'),
        ('Commercial','Commercial'),
        ('Appartment','Appartment'),
        ('Industrial','Industrial'),
        ('Office','Office'),

    )

    image = models.ImageField(upload_to='image')
    name = models.ForeignKey(Builder, on_delete=models.CASCADE)
    scheamname =models.CharField(max_length=100)
    location = models.CharField(max_length=200,default='') 
    price = models.CharField(max_length=100)
    propertytype = models.CharField(choices= CHOICE,max_length=100,default='')
    size = models.CharField(max_length=500)
    storeroom = models.IntegerField(blank=True,null=True,default='')
    bedrooms = models.IntegerField(blank=True,null=True)
    bathroom = models.IntegerField(blank=True, null=True, default='')
    amenites = models.CharField(max_length=100)
    builtyear = models.DateField()
    propertystatus = models.CharField(max_length=100,default='')
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    is_feature = models.BooleanField(default=False, )


    def __str__(self):
        return self.scheamname


class ImageUpload(models.Model):
    scheam = models.ForeignKey(Scheam, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'image/scheam' )
    # floorplan = models.ImageField(upload_to = 'image/scheam/floorplan')

    def __str__(self):
        return self.scheam.scheamname
    

class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

