from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    tax = models.FloatField()
    price = models.FloatField()