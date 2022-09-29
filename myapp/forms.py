from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Scheam,Builder,Customer, Account
import datetime


class UserSignupform(UserCreationForm):    
    class Meta:
        model = Account
        fields = ('username','email','password1','password2')
     

class BuilderForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpass =forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = Builder
        fields = ( 'buildername','email', 'mobile','agencyname','password','confirmpass')
    

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
    amenites = forms.MultipleChoiceField(label="Amenities",choices=CHOICES, widget=forms.CheckboxSelectMultiple)
    builtyear = forms.DateField(initial=datetime.date.today)
    class Meta:
        model = Scheam
        fields = ('image','name','scheamname','location','price','propertytype','size','amenites','storeroom','bedrooms','bathroom','builtyear','propertystatus','description','is_feature')
        