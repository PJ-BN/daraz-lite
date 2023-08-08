from django.shortcuts import render , redirect
from .models import *
from catalog.views import home
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


# def page(request):
#     return render(request,'login/index.html')
    
def login(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('pswd')
        quer = Loginid.objects.all().values()
        for i in quer:
            if i["email"] == username:
                if i["password"] == password:
                    request.session['username']= username
                    request.session.save()
                    return redirect(home)
                
        return HttpResponse("Incorrect")
    elif request.method =="GET":
        return render(request, "login\index.html")
            
            
        
        
        
    
def signup(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('pswd')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        
        # quer = Loginid.objects.values_list("email")
        # quer = [i[0] for i in quer]
        # id = len(quer) + 1 
        # print(quer)
        # if username not in quer:
        #     l = Loginid()
        #     l.name = name
        #     l.email = username
        #     l.password = password
        #     l.id = id
        #     l.save()
        #     return redirect("page")
        # return HttpResponse("this username already exisis")
        
        user = User.objects.create_user(username=username, password=password , first_name = first_name, last_name = last_name )
        
        if user is not None:
            user.save()
            us = authenticate(username= username, password=password)
            login(request, us)
            messages.success("succees")
        
            return redirect(home)
        
    else:
        return render(request, "register\index.html")