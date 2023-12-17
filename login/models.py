from django.db import models

# Create your models here.

class Loginid(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(primary_key=True)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length = 100)
    
    