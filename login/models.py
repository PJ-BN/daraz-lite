from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Loginids(models.Model):
    id = models.OneToOneField(User ,on_delete = models.CASCADE, primary_key = True )
    address = models.CharField(max_length=100)
    
class Sellerids(models.Model):
    id = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)  
    address = models.CharField(max_length=100)
    