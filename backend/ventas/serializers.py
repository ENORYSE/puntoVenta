from rest_framework import serializers
from .models import Remito 

class RemitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remito
        fields = ['id', 'numero', 'descripcion', 'total_estimado', 'pertenece_a', 'recibido_por', 'fecha',]
        read_only_fields = ['fecha']
