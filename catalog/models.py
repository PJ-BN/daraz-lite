from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="images/" )
    review = models.FloatField()
    quantity = models.IntegerField()
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Cart(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="cart/" )
    quantity = models.IntegerField()
    slug = models.SlugField()
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)    