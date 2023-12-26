from django.contrib import admin

from .models import *

# Register your models here.

class Logindisplay(admin.ModelAdmin):
    list_display = (  "id", "address")
    
class Sellerdisplay(admin.ModelAdmin):
    list_display = (  "id", "address")

admin.site.register(Loginids, Logindisplay)
admin.site.register(Sellerids, Sellerdisplay)


