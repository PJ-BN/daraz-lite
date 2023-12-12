from django.db import models
from django.utils.text import slugify


# Create your models here.

class SellerAccount(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(primary_key=True)
    address = models.CharField(max_length=200)
    phone = models.CharField()
    
    
class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="images/" )
    review = models.FloatField()
    quantity = models.IntegerField()
    slug = models.SlugField()
    seller = models.ForeignKey(SellerAccount, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)