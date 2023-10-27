from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
import os
from .models import Product


def home(request):
    
    data = Product.objects.all()
           
  
    
    context = {
        "data": data
    }
    return render(request, 'home.html', context)

def profile(request):
    if request.method =='GET':
        us = request.user.username
        print(us)
        
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
        "phone" : "9841615431" ,
        
        
            }
        return render(request, "cart.html", context=context)
 
def product(request, slug):
    identify_slug = get_object_or_404(Product, slug = slug)
    data = Product.objects.get(slug= slug)
    context = {
        'request': request,
        'post' : identify_slug,
        'data' : data,
    }
    return render(request, "product.html",context)
