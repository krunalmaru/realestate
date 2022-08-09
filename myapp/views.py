from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import Property, UsercreateForm, ContactInquiry,Builder
# makeCreate your views here.


def home(request):
    obj = Builder.objects.all()
    
    
    
    return render(request ,'myapp/home.html')

def signup(request):
    if request.method =='POST':
        form = UsercreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request,new_user)
            return redirect('home')
    else:
        form = UsercreateForm()
    context = {'form':form}
    return render(request, 'registration/signup.html',context)

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