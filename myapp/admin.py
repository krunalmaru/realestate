from django.contrib import admin
from .models import Builder,ImageUpload,Scheam,ContactInquiry

# Register your models here.
@admin.register(Builder)
class BuilderAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','mobile','agencyname','profileimg']


@admin.register(ImageUpload)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','scheam','image']


@admin.register(Scheam)
class ScheamAdmin(admin.ModelAdmin):
    list_display = ['id','name','scheamname','is_feature','amenites','builtyear','date','image','description']
   
admin.site.register(ContactInquiry)
