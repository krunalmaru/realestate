from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import ContactInquiry,Builder,Scheam
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .forms import BuilderForm, AddscheamForm,UserSignupform
from  django.views import View 
from django.db.models import Q
from django.core.paginator import Paginator
# makeCreate your views here.


def home(request):
    ourbui = Builder.objects.all()   
    obj = Scheam.objects.filter(is_feature = True).order_by('id')
    ab = Scheam.objects.values_list('propertytype', flat=True).order_by('propertytype').distinct()
    lo = Scheam.objects.values_list('location', flat=True).order_by('location').distinct()
    context = {'obj':obj ,'ourbui':ourbui, 'ab':ab, 'lo':lo}       
    return render(request ,'myapp/home.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserSignupform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'your account created successfully')
            form = UserSignupform()
            return redirect('login')

        # username = request.POST.get('username')
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # confirmpass = request.POST.get('confirmpass')

        # if password == confirmpass:
        #     if User.objects.filter(username=username).exists():
        #         messages.error(request, 'User Already exist')               
        #         return redirect('signup')
        #     else:
        #         myuser = User.objects.create_user(username=username, email=email, password=password)   
        #         myuser.set_password(password)     
        #         myuser.save()
        #         messages.success(request,'your account created successfully')
    else:
        form = UserSignupform()

    return render(request, 'myapp/signup.html',{'form':form})

def buidersignup(request):
    if request.method == 'POST':
        fm = BuilderForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'your account created successfully')
            return HttpResponseRedirect('/')
    else:
        fm = BuilderForm()    
    return render(request,'myapp/buildersignup.html',{'fm':fm})

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
    paginator = Paginator(builder, 2)
    page_number = request.GET.get('page')
    builder = paginator.get_page(page_number)
    context = {'builder':builder,'obj':obj}
    return render(request, 'myapp/builderlist.html',context)


def builderdetail(request,id):
    bui = Builder.objects.get(id=id)
    new = Scheam.objects.filter(is_feature = True).order_by('id')
    sc = Scheam.objects.filter(name=bui).filter(propertytype='Residential')
    com = Scheam.objects.filter(name=bui).filter(propertytype='Commercial')
    off = Scheam.objects.filter(name=bui).filter(propertytype='Office')
    ind = Scheam.objects.filter(name=bui).filter(propertytype='Industrial')
    app = Scheam.objects.filter(name=bui).filter(propertytype='Appartment')

    context = {'bui':bui,'sc':sc,'com':com,'off':off,'ind':ind,'app':app,'new':new}
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
        aj = Scheam.objects.all()       
        context = {'pr':pr,'aj':aj}
        return render(request,'myapp/propertydetail.html',context)


def propertylist(request):
    scheam = Scheam.objects.all().order_by('id')
    di = Scheam.objects.values_list('propertytype', flat=True).order_by('propertytype').distinct()
    loc = Scheam.objects.values_list('location', flat=True).order_by('location').distinct()
    # loc = Scheam.objects.all()
    paginator = Paginator(scheam, 3, orphans=1)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)    
    context = {'page_obj':page_obj,'di':di,'loc':loc}

    return render(request,'myapp/propertylist.html',context)

def addscheam(request):
    if request.method == 'POST':
        form = AddscheamForm(request.POST, request.FILES)
        # print(type(request.POST))
        # print(request.POST.keys())
        # print(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Data Save successfully!!')
            form = AddscheamForm()
            return redirect('/addscheam')
           
        else:
            print('form error',form.errors)

    else:
        form = AddscheamForm()
    return render(request, 'myapp/addscheam.html',{'form':form})
  
def search(request):
    query = request.GET['search']
    new = Scheam.objects.all()
    if query is not None:
        look = Q(propertytype__icontains = query)
        new = Scheam.objects.filter(look).distinct()
    context = {'new':new}
    return render(request,'myapp/search.html', context)