from .models import Product, DeliveryNote 
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, DeliveryNoteSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

class DeliveryNoteViewSet(viewsets.ModelViewSet):
    queryset = DeliveryNote.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = DeliveryNoteSerializer