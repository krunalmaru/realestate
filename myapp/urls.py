
from django.urls import path,include 
from django.conf.urls.static import static
from django.conf import settings
from myapp import views
urlpatterns = [

    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('buidersignup/', views.buidersignup, name='buidersignup'),
    path('login/', views.userlogin, name='login'),
    path('buiderlogin/', views.buiderlogin, name='builderlogin'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contactus, name='contact'), 

    path('property/<int:id>/', views.PropertyDetailView.as_view(), name='propertydetail'),
    
    path('propertylist/', views.propertylist, name='propertylist'),
    path('buiderlist/' , views.builderdetail, name='builderlist'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
