from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import ContactInquiry,Builder,Scheam
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .forms import BuilderForm
from  django.views import View
# makeCreate your views here.


def home(request):
    obj = Scheam.objects.all()   
    context = {'obj':obj }       
    return render(request ,'myapp/home.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpass = request.POST.get('confirmpass')

        if password == confirmpass:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User Already exist')               
                return redirect('signup')
            else:
                myuser = User.objects.create_user(username=username, email=email, password=password)   
                myuser.set_password(password)     
                myuser.save()
                messages.success(request,'your account created successfully')
                return redirect('login')
    else:
        print('this is Post')

    return render(request, 'myapp/signup.html')

def buidersignup(request):
    if request.method == 'POST':
        fm = BuilderForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/home')
    else:
        fm = BuilderForm()    
    return render(request,'myapp/builder.html',{'form':fm})

def userlogin(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'invalid credential')
            return redirect('login')
    else:     
        return render(request,'myapp/login.html')


def buiderlogin(request):
    return render(request, 'myapp/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def contactus(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        data = ContactInquiry(name=name, email=email,phone=phone,message=message)
        data.save()
        return redirect('contact')
    
    return render(request,'myapp/contact.html')

class PropertyDetailView(View):
    def get(self, request,id  ):
        pr = Scheam.objects.get(id=id)
        return render(request,'myapp/propertydetail.html',{'pr':pr})


def propertylist(request):
    sc = Scheam.objects.all()
    context = {'sc':sc}

    return render(request,'myapp/propertylist.html',context)
       
# def propertydetail(request):
#     obj = Scheam.objects.get(id=id)
#     return render(request,'myapp/propertydetail.html',{'jj':obj})

