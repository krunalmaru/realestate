from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm 
from .models import Scheam,Builder,CustomUser, Builderpro
import datetime


class CustomeUserSignupform(UserCreationForm):    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','name','password1','password2')

class CustomeUserChangeform(UserChangeForm)  :
    class Meta:
        model = CustomUser
        fields = ('email',)
        
        
class RegistrationForm(UserCreationForm):
    agencyname = forms.CharField(max_length=255)
    class Meta:
        model = Builderpro
        fields =  ('email','name','password1','password2','agencyname')

class BuilderForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpass =forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = Builder
        fields = '__all__'
        error_messages = {'buildername':{'required':'Name is required'},}

CHOICES = [
        ('AirConditioning','AirConditioning'),
        ('Lift','Lift'),
        ('SwimmingPool','SwimmingPool'),
        ('Security','Security'),
        ('ReservedParking','ReservedParking'),
        ('Garden','Garden'),
        ('24/7 Water Supply','24/7 Water Supply'),
        ('Gym','Gym'),
        ('Power Backup','Power Backup'),
        
]


class AddscheamForm(forms.ModelForm):
    builtyear = forms.DateField(initial=datetime.date.today)
    class Meta:
        model = Scheam
        fields = ('image','name','scheamname','location','price','propertytype','size','amenites','storeroom','zipcode','bedrooms','bathroom','builtyear','propertystatus','description','is_feature')
         