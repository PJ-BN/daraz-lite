from django.shortcuts import render , redirect
from .models import *
from catalog.views import home

# Create your views here.
from django.http import HttpResponse 


def page(request):
    return render(request,'login/index.html')
    
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
        return redirect(page)
            
            
        
        
        
    
def signup(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('pswd')
        name = request.POST.get("name")
        quer = Loginid.objects.values_list("email")
        quer = [i[0] for i in quer]
        id = len(quer) + 1 
        print(quer)
        if username not in quer:
            l = Loginid()
            l.name = name
            l.email = username
            l.password = password
            l.id = id
            l.save()
            return redirect("page")
        return HttpResponse("this username already exisis")