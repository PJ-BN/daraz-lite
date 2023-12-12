from django.db import models
from django.utils.text import slugify
from seller.models import *


class Cart(models.Model):
    id = models.ForeignKey(Products, on_delete=models.CASCADE, primary_key=True)
    # name = models.CharField(max_length=200)
    # description = models.TextField()
    # price = models.CharField(max_length=200)
    # image = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    # slug = models.SlugField()
        
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super().save(*args, **kwargs)    