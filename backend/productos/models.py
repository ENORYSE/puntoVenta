from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    barcode = models.CharField(max_length=50, unique=True, blank=True, null=True)
    tax = models.FloatField()
    price = models.FloatField()
