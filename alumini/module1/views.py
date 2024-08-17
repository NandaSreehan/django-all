from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
#from module1.models import lists
def home(request):
    return render(request,'home.html')


def register(request):
    return render(request,'register.html')

def loginview(request):
    return render(request,'login.html')

@login_required(login_url='loginpage')
def profile(request):
    return render(request,'profile.html')

def aboutview(request):
    return render(request,'about.html')

def delete(request,rid):
    return redirect('staffpage')

def update(request,rid):
    return (request,'update.html')

def contact(request):
    return render(request,'contact.html')

def logoutv(request):
    return redirect('loginpage')


def staff(request):
    return render(request,'staff.html')


def moreview(request):
    return render(request,'more.html')

def dedicatedview(request,rid):
    return render(request,'dedicated,html')

def about(request):
    return render(request,'about.html')
def alumini(request):
    return render(request,'home.html')