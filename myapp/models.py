from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime
# Create your models here.


class Builder(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='') 
    mobile = models.CharField(max_length=15)
    agencyname = models.CharField(max_length=100)   
    description = models.TextField()

    def __str__(self):
        return self.name

class Scheam(models.Model):
    image = models.ImageField(upload_to='image')
    name = models.ForeignKey(Builder, on_delete=models.CASCADE)
    scheamname =models.CharField(max_length=100) 
    price = models.CharField(max_length=100, default='')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.scheamname

class Property(models.Model):
    CHOICE = (
        ('Residential','Residential'),
        ('Commercial','Commercial'),
        ('Appartment','Appartment'),
        ('Industrial','Industrial'),
        ('Office','Office'),

    )
    name = models.ForeignKey(Builder, on_delete=models.CASCADE, default='')
    image = models.ImageField(upload_to = 'image')
    scheamname = models.ManyToManyField(Scheam)
    price =models.CharField(max_length=100)
    propertytype = models.CharField(choices= CHOICE,max_length=100)
    size = models.CharField(max_length=500)
    rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    bathroom = models.IntegerField()
    builtyear = models.DateField(auto_now_add=True)
    properystatus = models.CharField(max_length=100)

    def __str__(self):
        return self.propertytype
    
  
class UsercreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email',error_messages={'exists':'This Email Already Exists'})

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UsercreateForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

    def save(self, commit=True):
        user = super(UsercreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']

class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

