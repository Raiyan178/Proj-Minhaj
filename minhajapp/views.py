from itertools import product
from tkinter.messagebox import RETRY
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *



# Create your views here.


def index(request):
    
    return render(request,'index.html')



def package(request):
    packages = Packages.objects.all()
    return render(request,'packges.html',{'packages':packages})


def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.info(request,"invalid credential")
                return redirect('/signin')
        return render(request,'signin.html')
    
        


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            username =request.POST['uname']
            email= request.POST['email']
            password = request.POST['pass']
            password2 = request.POST['cpass']
            if password == password2 :
                if User.objects.filter(username=username).exists():
                    messages.error(request,"Username is'nt available ")
                    return redirect('/signup')
                elif User.objects.filter(email=email).exists():
                    messages.error(request,"email already available")
                    return redirect('/signup')
                else:
                    user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
                    user.save()
                    signIn = authenticate(username=username,password=password)
                    login(request,signIn)
                    return redirect('/profilemap')

        return render(request,'regi.html')


def profile(request):
    if request.user.is_authenticated:
        profileobj = Profile.objects.get(user=request.user)
        ordernu = Order.objects.filter(customer = request.user.profile)
        ordernum = ordernu.count()
        print(ordernum)
        return render(request,'profile.html',{"profileobj":profileobj,'ordercount':ordernum})
    else:
        return redirect('/signin')


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/signin')


def profilemap(request): 
    if request.user.is_authenticated:
        if request.method == 'POST':
            image = request.FILES['image']
            phonenum = request.POST['phone']
            address1 = request.POST['address']            
            addresstwo = request.POST['address2']            
            zip = request.POST['zip']            
            city = request.POST['city']            
            state = request.POST['state'] 
            address = address1+', '+addresstwo+", "+zip+", "+city+", "+state


            profilecr = Profile.objects.create(profilePic=image,phone=phonenum,address=address,user=request.user)

            if profilecr:
                
                profilecr.save()
                return redirect('/')
                
            else:
                messages.error(request,'Profile did not created')
    
        return render(request,'profilemap.html')
    else:
        return redirect('signin')


def pak(request,slug):
    productsl = Packages.objects.get(slug=slug)
    return render(request,'pak.html',{'product':productsl})


def order(request,slug):
    if request.user.is_authenticated:
        pro = Packages.objects.get(slug=slug)
        name = request.user.username
        protitle = pro.title

        if request.method == 'POST':
            quan = request.POST['quan']
            quan = int(quan)
            orderIn = Order.objects.create(customer=request.user.profile,product=pro,quan=quan,status='Pending')
            if orderIn:
                orderIn.save()
                messages.info(request,'Order Pending and it cost'+ f" {quan*pro.price}$")
        context = {'name':name,'title':protitle,'slug':slug,'pro':pro}
        return render(request,'order.html',context)
    else:
        messages.info(request,'Create an Account and login')
        return redirect('/package')




def search(request):
    sterm = request.GET.get('search',None)
    if sterm == None:
        return redirect('/')
    else:
        pack = Packages.objects.filter(title__icontains = sterm)
        print(pack)
        contex = {'pack':pack}
    return render(request,'search.html',contex)