from .models import Product
from actividades.models import Actividad
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        producto = serializer.save()
        Actividad.objects.create(
            usuario=self.request.user,
            accion='Creación de producto',
            detalle=f"Producto: {producto.name}, Precio: {producto.price}, Stock: {producto.quantity}"
        )

class ProductViewSet(viewsets.ModelViewSet): #pustete
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
