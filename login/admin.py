from django.contrib import admin

from .models import *

# Register your models here.

class Logindisplay(admin.ModelAdmin):
    list_display = ( "id", "name", "email", "password")

admin.site.register(Loginid, Logindisplay)
