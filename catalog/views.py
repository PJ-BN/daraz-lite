from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
import os
import json
from .models import *
from login.models import Loginid


def home(request):
    print(request.POST)
    
    if request.method == "POST":
        print("done")
        
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
    elif request.method =="POST":
        print("done")
    
    
def update_cart(request):
    data = json.loads(request.body.decode('utf-8'))
    name = data.get('key1')
    price = data.get('key2')
    image = data.get('key3')
    quantity = data.get('key4')
    description = data.get('key5')
    try:
        a = Cart.objects.get(name = name)
    except:
        ca = Cart(name = name , description = description, price = price , image = image, quantity = quantity , slug = name)
        ca.save()
        print("success")
        
    

    return JsonResponse({'success' :'sucess'})
    


def cart(request):
    if request.method == "GET":
        
        data = Cart.objects.all()
        
        context = {
        'request': request,
        'data' : data,
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

def added_to_cart(request):
    if request.method == "POST":
        print('done')