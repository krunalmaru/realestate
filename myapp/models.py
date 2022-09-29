from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models import Q
from django.utils import timezone
from django import forms
import datetime
# from django_resized import ResizedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# from sorl.thumbnail import ImageField, get_thumbnail
# Create your models here.

class MyaccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User have must have email address")
        if not username:
            raise ValueError("User have must username")
        
        user = self.model(
                email = self.normalize_email(email),
                username = username,
            )

        user.set_password(password)
        user.save(using=self._db)   
        return user
    
    def create_superuser(self, email,username, password):
        user = self.create_user(
                email = self.normalize_email(email),
                username = username,
                password = password
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=70, unique=True)
    username = models.CharField(max_length=255, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined' , auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    mobile = models.IntegerField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyaccountManager()

    def __str__(self):
        return self.email + "," + self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, label):
        return True
   

class Customer(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.IntegerField(null=True) 
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
class Builder(models.Model):
    username = None
    buildername = models.CharField(max_length=100)
    email = models.EmailField(default='') 
    mobile = models.CharField(max_length=15) 
    agencyname = models.CharField(max_length=100)   
    
    def __str__(self):
        return self.buildername


class profile(models.Model):
    buildername = models.ForeignKey(Builder, on_delete=models.CASCADE)
    profileimg = models.ImageField(upload_to='image/profile',blank = True, null = True)
    profileimg_thumbnail = ImageSpecField(source='profileimg',processors=[ResizeToFill(50,50)],format='JPEG',options={'quality':80})
    profileimg_size = ImageSpecField(source='profileimg',processors=[ResizeToFill(200,200)],format='JPEG',options={'quality':80})
    address = models.CharField(max_length=1000,default='')
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()


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

    def __str__(self):
        return self.name

