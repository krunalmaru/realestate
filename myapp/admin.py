from django.contrib import admin
from .models import Builder,ImageUpload,Scheam,ContactInquiry,profile,Customer, Customerpro,Builderpro
from django.contrib.auth.admin import UserAdmin

from .forms import CustomeUserChangeform, CustomeUserSignupform
from .models import CustomUser

# Register your models here.

class CustomeUserAdmin(UserAdmin):
    add_form = CustomeUserSignupform
    form = CustomeUserChangeform
    model = CustomUser
    list_display = ('email','name','is_staff','is_active',)
    list_filter = ('email','is_staff','is_active',)
    fieldsets = (
        (None, {"fields": ('email','name','type','password')}),
        ('permissions', {'fields':('is_staff','is_active')}),
    )
    add_fieldsets = (
         (None,{
            'classes' : ('wide',),
            'fields':('email','password1','password2','is_staff','is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomeUserAdmin)   



@admin.register(Builder)
class BuilderAdmin(admin.ModelAdmin):
    list_display = ['id','buildername','email','mobile','agencyname']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user','address']
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

admin.site.register(Customerpro)
admin.site.register(Builderpro)