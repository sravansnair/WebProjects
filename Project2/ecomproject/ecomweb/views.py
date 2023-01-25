from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import table1,table2

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid USERNAME or PASSWORD")
            return redirect('/login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def index(request):
    obj=table1.objects.all()
    obj1=table2.objects.all()
    return render(request,"index.html",{'result':obj,'team':obj1})
def regform(request):
    if request.method=='POST':
        fnm = request.POST['fname']
        lnm = request.POST['lname']
        email = request.POST['email']
        usrnm = request.POST['username']
        pswrd = request.POST['password']
        cpass = request.POST['cpassword']
        if pswrd==cpass:
            if User.objects.filter(username=usrnm).exists():
                messages.info(request,"Username already taken")
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('/register')
            else:
                user=User.objects.create_user(username=usrnm,password=pswrd,first_name=fnm,last_name=lnm,email=email)

                user.save()
            return redirect('/login')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('/register')

        return redirect('/')
    return render(request,"register.html")