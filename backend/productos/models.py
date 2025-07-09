from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    tax = models.FloatField()
    price = models.FloatField()

class DeliveryNote(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    belongsTo = models.CharField(max_length=200)
    receivedBy = models.CharField(max_length=200)