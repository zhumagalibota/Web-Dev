from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    count = models.IntegerField()
    is_active = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
