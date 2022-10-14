
from django.urls import path,include 
from django.conf.urls.static import static
from django.conf import settings
from myapp import views
urlpatterns = [

    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('buildersignup/', views.buidersignup, name='buildersignup'),
    path('login/', views.userlogin, name='login'),
    path('accounts/builderlogin/', views.buiderlogin, name='builderlogin'),
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contactus, name='contact'), 
    path('builderdetail/<int:id>/', views.builderdetail, name='builderdetail'),
    path('property/<int:id>/', views.PropertyDetailView.as_view(), name='propertydetail'),
    path('addscheam/', views.addscheam, name='addscheam'),
    path('propertylist/', views.propertylist, name='propertylist'),
    path('builderlist/' , views.builderlist, name='builderlist'),
    path('search/', views.search, name='search'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
