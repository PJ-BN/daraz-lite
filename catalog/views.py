from django.shortcuts import render, redirect

# Create your views here.

def landing(request):
    context = {
        "data" : [1,2,3,4,5,6,7,8,9,10]
    }
    return render(request, 'landing.html', context)


def home(request):
    context = {
        "data" : [1,2,3,4,5,6,7,8,9,10]
    }
    return render(request, 'home.html', context)

def profile(request):
    if request.method =='GET':
        context = {
        "data" : [1,2,3,4,5,6,7,8,9,10],
        "f_name": "Prajwal",
        "l_name":"Bhandari",
        "email" : "prajwalbh25@gmail.com",
        "address":"Banbatika",
        "phone" : "9841615431",
        "order": ["1234"], 
        "time":["01/01/2000"],
        "items": ["a.png"],
        "total": ["2000"]
        
            }
        return render(request, 'profile.html', context)
    
def cart(request):
    if request.method == "GET":
        context = {
        "data" : [1,2,3,4,5,6,7,8,9,10],
        "f_name": "Prajwal",
        "l_name":"Bhandari",
        "email" : "prajwalbh25@gmail.com",
        "address":"Banbatika",
        "phone" : "9841615431" 
        
            }
        return render(request, 'cart.html', context)