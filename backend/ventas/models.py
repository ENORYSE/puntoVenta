from django.db import models

class Remito(models.Model):
    numero = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    total_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    pertenece_a = models.CharField(max_length=200)  # proveedor, empresa, etc.
    recibido_por = models.CharField(max_length=200)  # nombre del empleado
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Remito {self.numero} - {self.pertenece_a}"
