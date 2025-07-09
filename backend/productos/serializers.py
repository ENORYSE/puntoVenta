from rest_framework import serializers
from .models import Product, DeliveryNote

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity', 'tax', 'price')
        #read_only_fields = ('')

class DeliveryNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryNote
        fields = ('id', 'title', 'description', 'price', 'belongsTo', 'receivedBy')