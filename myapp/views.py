from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import ContactInquiry,Builder,Scheam
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .forms import BuilderForm, AddscheamForm
from  django.views import View
from django.core.paginator import Paginator
# makeCreate your views here.


def home(request):
    obj = Scheam.objects.filter(is_feature = True).order_by('id')
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


def builderlist(request):
    obj = Scheam.objects.filter(is_feature = True).order_by('-id')
    builder = Builder.objects.all().order_by('id')
    paginator = Paginator(builder, 1)
    page_number = request.GET.get('page')
    bui = paginator.get_page(page_number)
    context = {'builder':bui,'obj':obj}
    return render(request, 'myapp/builderlist.html',context)


def builderdetail(request,id):
    bui = Builder.objects.get(id=id)
    print(bui)
    sc = Scheam.objects.filter(name=bui).filter(propertytype='Residential')
    com = Scheam.objects.filter(name=bui).filter(propertytype='Commercial')
    off = Scheam.objects.filter(name=bui).filter(propertytype='Office')
    ind = Scheam.objects.filter(name=bui).filter(propertytype='Industrial')
    app = Scheam.objects.filter(name=bui).filter(propertytype='Appartment')

    context = {'bui':bui,'sc':sc,'com':com,'off':off,'ind':ind,'app':app}
    return render (request, 'myapp/builderdetail.html',context)


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
    def get(self, request,id ):
        pr = Scheam.objects.get(id=id)
        print(pr)
        aj = Scheam.objects.all()       
        context = {'pr':pr,'aj':aj}
        return render(request,'myapp/propertydetail.html',context)


def propertylist(request):
    scheam = Scheam.objects.all().order_by('id')
    paginator = Paginator(scheam, 1, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)    
    context = {'page_obj':page_obj}

    return render(request,'myapp/propertylist.html',context)

def addscheam(request):
    if request.method == 'POST':
        form = AddscheamForm(request.POST, request.FILES)
        print(type(request.POST))
        print(request.POST.keys())
        print(request.POST)
        if form.is_valid():
            form.save() 
        
            messages.success(request, 'Data Save successfully!!')
            form = AddscheamForm()
            return redirect('/addscheam')
           
        else:
            print('form error',form.errors)
   
        print('this is post ')
        # return redirect('/')
    else:
        form = AddscheamForm()
        print("this is get")
    return render(request, 'myapp/addscheam.html',{'form':form})
  
