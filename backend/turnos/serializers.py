from rest_framework import serializers
from .models import TipoTurno, TurnoAsignado
from django.contrib.auth import get_user_model

User = get_user_model()

class TipoTurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTurno
        fields = '__all__'


class TurnoAsignadoSerializer(serializers.ModelSerializer):
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = TurnoAsignado
        fields = ['id', 'usuario', 'usuario_username', 'tipo_turno', 'fecha']
