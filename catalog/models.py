from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from seller.models import *


class Cart(models.Model):
    id = models.OneToOneField(Products, on_delete=models.CASCADE, primary_key=True)
    quantity = models.CharField(max_length=200)
    user = models.CharField(null = False ,max_length = 150) 