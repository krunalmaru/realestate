from django.contrib import admin
from .models import Builder,ImageUpload,Scheam,ContactInquiry,profile,Customer,Account

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','is_admin','is_active','is_staff','is_superuser','password']

@admin.register(Builder)
class BuilderAdmin(admin.ModelAdmin):
    list_display = ['id','buildername','email','mobile','agencyname']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','mobile','password']


@admin.register(ImageUpload)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','scheam','image']


@admin.register(Scheam)
class ScheamAdmin(admin.ModelAdmin):
    list_display = ['id','name','scheamname','is_feature','amenites','builtyear','date','image','description']
   
admin.site.register(ContactInquiry)

@admin.register(profile)
class BuilderProfile(admin.ModelAdmin):
    list_display = ['id','profileimg','buildername','address','city','zipcode']