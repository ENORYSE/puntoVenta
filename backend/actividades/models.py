from django.db import models
from django.conf import settings

class Actividad(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    accion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    detalle = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.accion} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"
