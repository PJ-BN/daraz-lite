from django.contrib import admin

from .models import *


# Register your models here.

class Sellerdisplay(admin.ModelAdmin):
    list_display = (  "name", "email", "address")
    
class ProductDisplay(admin.ModelAdmin):
    list_display= ("name", "price", "review", "quantity")

admin.site.register(SellerAccount, Sellerdisplay)
admin.site.register(Products, ProductDisplay)

