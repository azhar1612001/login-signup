from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Detail
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        try:
            username=request.user.username
            temp=Detail.objects.get(username=username)
            return render(request,'home.html',{'status':'yes'})
        except:
            return render(request,'home.html',{'status':''})
    return render(request,'home.html')

@login_required(login_url='login')
def vdetail(request):
    username=request.user.username
    temp=Detail.objects.get(username=username)
    return render(request,'vdetail.html',{'data':temp})

@login_required(login_url='login')
def update(request):
    username=request.user.username
    temp=Detail.objects.get(username=username)
    if request.method=='POST':
        temp.add1=request.POST['add1']
        temp.add2=request.POST['add2']
        temp.city=request.POST['city']
        temp.state=request.POST['state']
        temp.country=request.POST['country']
        temp.pin=request.POST['pin']
        temp.occupation=request.POST['occup']
        temp.save()
        return redirect('/')
    return render(request,'update.html',{'data':temp})
@login_required(login_url='login')
def detail(request):
    if request.method=='POST':
        add1=request.POST['add1']
        add2=request.POST['add2']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        pin=request.POST['pin']
        response=render(request,'occupation.html')
        response.set_cookie('add1',add1)
        response.set_cookie('add2',add2)
        response.set_cookie('city',city)
        response.set_cookie('state',state)
        response.set_cookie('country',country)
        response.set_cookie('pin',pin)
        return response
    return render(request,'detail.html')

@login_required(login_url='login')
def occupation(request):
    if request.method=='POST':
        occup=request.POST['occup']
        add1=request.COOKIES.get('add1')
        add2=request.COOKIES.get('add2')
        city=request.COOKIES.get('city')
        state=request.COOKIES.get('state')
        country=request.COOKIES.get('country')
        pin=request.COOKIES.get('pin')
        username=request.user.username
        detail=Detail(username=username,add1=add1,add2=add2,city=city,state=state,country=country,pin=pin,occupation=occup)
        detail.save()
        return redirect('/')
    return render(request,'occupation.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        username=''
        try:
            temp=User.objects.get(email=email)
            username=temp.username
        except:
            msg='invalid email'
            return render(request,'login.html',{'msg':msg})
        user=auth.authenticate(username=username,email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            msg='invalid password'
            return render(request,'login.html',{'msg':msg})
    msg=''
    return render(request,'login.html',{'msg':msg})
def log_out(request):
    logout(request)
    return redirect('/')

def sinup(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        username=request.POST['uname']
        password=request.POST['password']
        repassword=request.POST['repassword']
        if password==repassword:
            if User.objects.filter(username=username).exists():
                msg='username taken'
                return render(request,'sinup.html',{'msg':msg})
            elif User.objects.filter(email=email).exists():
                msg='email exist'
                return render(request,'sinup.html',{'msg':msg})
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                user.save()
                msg='user created, Please Login'
                return render(request,'login.html',{'msg':msg})
        else:
            msg='password does not match'
            return render(request,'sinup.html',{'msg':msg})
        return redirect('/')
    msg=''
    return render(request,'sinup.html',{'msg':msg})
