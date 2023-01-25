
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"loginpage.html")

def result(request):
    x=int(request.GET['no1'])
    y=int(request.GET['no2'])
    res1=x+y
    res2=x-y
    res3=x*y
    res4=x/y
    return render(request,"result.html",{'ans1':res1,'ans2':res2,'ans3':res3,'ans4':res4})
