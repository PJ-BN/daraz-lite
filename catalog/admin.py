from django.contrib import admin
from .models import *

# Register your models here.

class ProductDisplay(admin.ModelAdmin):
    list_display= ("name", "price", "review", "quantity")
    
class CartDisplay(admin.ModelAdmin):
    list_display= ("name", "price",  "quantity")
    
admin.site.register(Product, ProductDisplay)
admin.site.register(Cart, CartDisplay)
