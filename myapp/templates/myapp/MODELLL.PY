from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy  as _
from multiselectfield import MultiSelectField
from django.contrib.auth.base_user import BaseUserManager
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


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email_address'), unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
   

    class Type(models.TextChoices):
        BUILDER="Builder","BUILDER"
        CUSTOMER = "Customer","CUSTOMER"

    default_type = Type.CUSTOMER

    type = MultiSelectField(choices = Type.choices, default = [], null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = BaseUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.id:
            self.type.append(self.default_type)

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    

class NewBuilder(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15) 
    agencyname = models.CharField(max_length=100) 

class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains= CustomUser.Type.CUSTOMER))


class NewBuilderManager(models.Manager):
    def get_queryset(self, *args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(Q(type__contains= CustomUser.Type.BUILDER))

class AddCustomer(CustomUser):
    default_type = CustomUser.Type.CUSTOMER
    objects = CustomerManager() 
    class Meta:
        proxy = True

    @property
    def Customer(self):
        return self.Customer

class AddBuilder(CustomUser):
    default_type = CustomUser.Type.BUILDER
    objects = NewBuilderManager()
    class Meta:
        proxy = True

    @property
    def NewBuilder(self):
        return self.NewBuilder


class Builder(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='') 
    mobile = models.CharField(max_length=15) 
    agencyname = models.CharField(max_length=100)   
    
    def __str__(self):
        return self.name


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

