from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django import forms
import datetime
# from django_resized import ResizedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# from sorl.thumbnail import ImageField, get_thumbnail
# Create your models here.

class Builder(models.Model):
    profileimg = models.ImageField(upload_to='image/profile')
    profileimg_thumbnail = ImageSpecField(source='profileimg',processors=[ResizeToFill(50,50)],format='JPEG',options={'quality':80})
    profileimg_size = ImageSpecField(source='profileimg',processors=[ResizeToFill(200,200)],format='JPEG',options={'quality':80})
    name = models.CharField(max_length=100)
    email = models.EmailField(default='') 
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=1000,default='')
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    agencyname = models.CharField(max_length=100)   
    
    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs): 
    #     if self.profileimg:
    #         self.profileimg = get_thumbnail(self.profileimg, '500x600', quality=99, format='JPEG')
    #     super(Builder, self).save(*args, **kwargs)


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
    address = models.CharField(max_length=1000,default='')
    state = models.CharField(max_length=50, default='') 
    zipcode = models.IntegerField()
    price = models.FloatField(max_length=100)
    propertytype = models.CharField(choices= CHOICE,max_length=100,default='')
    size = models.IntegerField()
    storeroom = models.IntegerField(blank=True,null=True,default='')
    bedrooms = models.IntegerField(blank=True,null=True)
    bathroom = models.IntegerField(blank=True, null=True, default='')
    amenites = models.CharField(max_length=100, blank=False)
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

