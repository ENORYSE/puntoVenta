from rest_framework import viewsets, permissions
from .models import Remito
from .serializers import RemitoSerializer

class RemitoViewSet(viewsets.ModelViewSet):
    queryset = Remito.objects.all()
    serializer_class = RemitoSerializer
    permission_classes = [permissions.AllowAny]
