from django.shortcuts import render , redirect
from .models import *
from catalog.views import home
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login

from django.contrib import messages

  
def login(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('pswd')
        user = authenticate(request, username= username, password=password)
        try:
            auth_login( request, user)
            
        except:
            return render(request, "login\index.html", {"data": "Incorect username and password"})
            
        return redirect(home)
    elif request.method =="GET":
        return render(request, "login\index.html")
     
    
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pswd')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        address = request.POST.get("address")
        email  = request.POST.get("email")
        
        user = User.objects.create_user(username=username, password=password , first_name = first_name, last_name = last_name, email= email )
        
        if user is not None:
            user.save()
            us = authenticate(request, username= username, password=password)
            auth_login(request, us)
        
            return redirect(home)
        
    else:
        return render(request, "register\index.html")