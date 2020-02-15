from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    restaurant = models.CharField(max_length=512)
    category = models.CharField(max_length=128)
