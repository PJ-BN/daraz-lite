from django.db import models

# Create your models here.

class SellerAccount(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(primary_key=True)
    address = models.CharField(max_length=200)
    phone = models.CharField()
    
    
