from rest_framework import viewsets, permissions
from .models import TipoTurno, TurnoAsignado
from .serializers import TipoTurnoSerializer, TurnoAsignadoSerializer

class TipoTurnoViewSet(viewsets.ModelViewSet):
    queryset = TipoTurno.objects.all()
    serializer_class = TipoTurnoSerializer
    permission_classes = [permissions.IsAuthenticated]


class TurnoAsignadoViewSet(viewsets.ModelViewSet):
    queryset = TurnoAsignado.objects.all()
    serializer_class = TurnoAsignadoSerializer
    permission_classes = [permissions.IsAuthenticated]
