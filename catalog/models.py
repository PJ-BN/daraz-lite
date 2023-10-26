from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="images/" )
    review = models.FloatField()
    quantity = models.IntegerField()
    slug = models.SlugField()
    