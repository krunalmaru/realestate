from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,User
from django.core.validators import RegexValidator

from django.utils.translation import gettext_lazy as _

from django.utils import timezone
from multiselectfield import MultiSelectField
from django.db.models import Q
from .manager import CustomUserManager
# from django_resized import ResizedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=255)
    is_staff =models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    class Types(models.TextChoices):
        BUILDER = "Builder" , "BUILDER"
        CUSTOMER = "Customer", "CUSTOMER"
    
    default_type = Types.CUSTOMER

    type = MultiSelectField(choices=Types.choices, default=[default_type], null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args,**kwargs):
        if not self.id:
            self.type.append(self.default_type)
        return super().save(*args, **kwargs)
    
class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)


class Builder(models.Model):
    buildername = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
    mobile = models.BigIntegerField(null=True) 
    agencyname = models.CharField(max_length=100)  
   
    def __str__(self):
        return self.buildername.name

    
class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains = CustomUser.Types.CUSTOMER))

class BuilderManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains = CustomUser.Types.BUILDER))

class Customerpro(CustomUser):
    default_type = CustomUser.Types.CUSTOMER
    objects = CustomerManager()
    class Meta:
        proxy = True

    def buy(self):
        print('buy property')

    @property
    def showadditional(self):
        return self.Customer
    
class Builderpro(CustomUser):
    default_type = CustomUser.Types.BUILDER
    objects = BuilderManager()
    class Meta:
        proxy = True

    def sell(self):
        print('sell property')

    @property
    def showadditional(self):
        return self.Builder
    


class profile(models.Model):
    buildername = models.OneToOneField(Builder, on_delete=models.CASCADE)
    profileimg = models.ImageField(upload_to='image/profile',blank = True, null = True)
    profileimg_thumbnail = ImageSpecField(source='profileimg',processors=[ResizeToFill(50,50)],format='JPEG',options={'quality':80})
    profileimg_size = ImageSpecField(source='profileimg',processors=[ResizeToFill(200,200)],format='JPEG',options={'quality':80})
    address = models.CharField(max_length=100,default='')
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
    
    class Amenities(models.TextChoices):
        LIFT = "Lift" ,"LIFT"
        SECURITY = "Security","SECURITY"
        GARDEN = "Garden", "GARDEN"
        RESERVPARKING = "Reserv Parking","RESERVPARKING"
        SWIMMINGPULL = "Swimming Pull", "SWIMMINGPULL"
        GYM = "Gym","GYM"
        POWERBACKUP = "PowerBackup",'POWERBACKUP'



    image = models.ImageField(upload_to='image')
    name = models.ForeignKey(Builder, on_delete=models.CASCADE)
    scheamname =models.CharField(max_length=100)
    location = models.CharField(max_length=200,default='')
    address = models.CharField(max_length=1000,default='')
    state = models.CharField(max_length=50, default='') 
    zipcode = models.IntegerField(null = True)
    price = models.FloatField(max_length=100)
    propertytype = models.CharField(choices= CHOICE,max_length=100,default='')
    size = models.IntegerField()
    storeroom = models.IntegerField(blank=True,null=True,default='')
    bedrooms = models.IntegerField(blank=True,null=True)
    bathroom = models.IntegerField(blank=True, null=True, default='')
    amenites = MultiSelectField(choices=Amenities.choices, default=[], null=True, blank=True)
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

