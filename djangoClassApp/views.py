from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# @login_required(login_url='login')
def home(request):
    students = Students.objects.all()
    about_us = Detail.objects.all()
    services = Service.objects.all()
    context = {
        'students': students,
        'about_us': about_us,
        'services': services,
    }
    return render(request, 'index.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Login Details Not Valid, Enter Correctly.')
            return redirect('login')
    else:
        return render(request, 'login.html')    
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already in Use')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already in Use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email, password=password1)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password Do Not Match')
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def signout(request):
    auth.logout(request)
    return redirect('home')

def blog(request):
    return render(request, 'blog.html')

def services(request):
    return render(request, 'services-details.html')

def portfolioDetails(request):
    return render(request, 'portfolio-details.html')

def blogDetails(request):
    return render(request, 'blog-details.html')

