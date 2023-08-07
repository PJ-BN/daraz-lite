from django.shortcuts import render, redirect

# Create your views here.

def Username(request):
    if 'username' in request.session:
        username=request.session['username']
    else:
        username = "" 
    
    return username


def logout(request):
    del request.session["username"]
    
    return redirect(home)


def home(request):
    username = Username(request)
    
    
        
    context = {
        "data" : [1,2,3,4,5,6,7,8,9,10],
        "product": "Mouse",
        "price": 1000,
        "rating": 4,
        "username": username
    }
    return render(request, 'home.html', context)

def profile(request):
    if request.method =='GET':
        username = Username(request)
        
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
        "total": ["2000"],
        "username": username
        
            }
        return render(request, 'profile.html', context)
    
def cart(request):
    if request.method == "GET":
        username = Username(request)
        
        context = {
        "data" : [1,2,3,4,5,6,7,8,9,10],
        "f_name": "Prajwal",
        "l_name":"Bhandari",
        "email" : "prajwalbh25@gmail.com",
        "address":"Banbatika",
        "phone" : "9841615431" ,
        "username": username
        
        
            }
        return render(request, 'cart.html', context)