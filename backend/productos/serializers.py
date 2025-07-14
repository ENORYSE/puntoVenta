from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    necesita_restock = serializers.ReadOnlyField()  # Para incluir la propiedad
    
    class Meta:
        model = Producto
        fields = [
            'id',
            'codigo_barra', 
            'nombre',
            'descripcion',
            'precio_venta',
            'precio_costo', 
            'stock_actual',
            'stock_minimo',
            'unidad_medida',
            'activo',
            'fecha_creacion',
            'fecha_actualizacion',
            'necesita_restock'  
        ]
        read_only_fields = ['fecha_creacion', 'fecha_actualizacion']