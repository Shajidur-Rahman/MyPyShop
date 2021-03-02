from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stoke = models.IntegerField()
    image_urls = models.CharField(max_length=2000)