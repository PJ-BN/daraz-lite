from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
import os
import json
from  seller.models import *
from .models import *
from login.models import Loginids
from django.contrib.auth.models import User


def home(request):
    print(request.POST)
    
    if request.method == "POST":
        print("done")
        
    product_data = Products.objects.all()
    seller_data = SellerAccount.objects.all()
    
    for product in product_data:
        print(f"{product.email.name}")
           
  
    
    context = {
        "data": product_data,
        'sellers': seller_data
    }
    return render(request, 'home.html', context)

def profile(request):
    if request.method =='GET':
        us = request.user.username
        id = User.objects.get(username= us)
        
        data = Loginids.objects.get(id_id = id.id)
        
        context = {
        'data' : data,
        
        "order": ["1234"], 
        "time":["01/01/2000"],
        "items": ["a.png"],
        "total": ["2000"],
        
            }
        return render(request, 'profile.html', context)
    
        
   
def search(request):
    if request.method == "POST":
        
        search = request.POST.get("search") 
        print(search)
        
        product_data = Products.objects.filter(name= search.capitalize())
        context = {
            "data": product_data
        }
        # return JsonResponse({'success' :'sucess'})
        return render(request, 'home.html', context)
    
    
    
        
    
def update_cart(request):
    data = json.loads(request.body.decode('utf-8'))
    
    quantity = data.get('key1')
    id = data.get('key2')
    
    
    
    user = request.user.username
    if user:
        ca = Cart(id = Products.objects.get(id = id) , quantity = quantity, user = user)
        ca.save()
    
        
    

    return JsonResponse({'success' :'sucess'})
    


def cart(request):
    if request.method == "GET":
        user = request.user.username
        
        data = Cart.objects.filter(user = user)
        selle = set([i.id.email.name for i in data ])
        
        
        context = {
        'request': request,
        'data' : data,
        'seller': selle
        }
        
        return render(request, "cart.html", context=context)
  
        

        
    
        
 
def product(request, slug):
    identify_slug = get_object_or_404(Products, slug = slug)
    
    data = Products.objects.get(slug= slug)
    context = {
        'request': request,
        'post' : identify_slug,
        'data' : data,
    }
    return render(request, "product.html",context)

def added_to_cart(request):
    if request.method == "POST":
        print('done')
        


def update_data(request):
    data = json.loads(request.body)
    id = data.get('names')  # Assuming you send the ID of the instance to update
    new_quantity = data.get('new_quantity')  # Assuming you send the new name

    try:
        # instance = Cart.objects.get(id=instance_name)
        # instance_all = Cart.objects.all()
        # a = [i.id.id for i in instance_all if i.id.name == instance_name]
        instance = Cart.objects.get(id = id)
        instance.quantity = new_quantity
        instance.save()
        return JsonResponse({'success': True})
    except Cart.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Instance not found'})
    

def delete_data(request):
    data = json.loads(request.body)
    id = data.get('id') 

    try:
        instance = Cart.objects.get(id = id)
        instance.delete()
        return JsonResponse({'success': True})
    
    except:
        return JsonResponse({'success': False})
        
    
def buy_now(request):
    if request.body:
        data = json.loads(request.body.decode('utf-8'))
        
        price = data.get("key1")
        print(price)
    return render(request, "buynow.html")
    
