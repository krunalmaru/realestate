from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Builder)
class BuilderAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','mobile','agencyname']


@admin.register(ImageUpload)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','scheam','image']


admin.site.register(ContactInquiry)
@admin.register(Scheam)
class ScheamAdmin(admin.ModelAdmin):
    list_display = ['id','name','scheamname','is_feature']

