from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Actividad(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    accion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    detalle = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.accion} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"

class User(AbstractUser):
    ROLES = (
        ('empleado', 'Empleado'),
        ('encargado', 'Encargado'),
        ('jefe', 'Jefe'),
    )
    rol = models.CharField(max_length=20, choices=ROLES, default='empleado')

    def __str__(self):
        return f"{self.username} ({self.rol})"
    
class TipoTurno(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.nombre} ({self.hora_inicio} - {self.hora_fin})"


class TurnoAsignado(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='turnos')
    tipo_turno = models.ForeignKey(TipoTurno, on_delete=models.CASCADE)
    fecha = models.DateField()

    class Meta:
        unique_together = ('usuario', 'fecha')   # Evita turnos duplicados el mismo día

    def __str__(self):
        return f"{self.usuario.username} - {self.tipo_turno.nombre} el {self.fecha}"

