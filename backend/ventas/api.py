from rest_framework import viewsets, permissions
from .models import DeliveryNote
from .serializers import DeliveryNoteSerializer

class DeliveryNoteViewSet(viewsets.ModelViewSet):
    queryset = DeliveryNote.objects.all()
    serializer_class = DeliveryNoteSerializer
    permission_classes = [permissions.AllowAny]
