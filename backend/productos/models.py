from django.db import models

class Producto(models.Model):
    codigo_barra = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.IntegerField(default=0,)
    stock_minimo = models.IntegerField(default=0,)
    unidad_medida = models.CharField(max_length=50, default='unidad')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.codigo_barra} - {self.nombre}"

    @property
    def necesita_restock(self):
        return self.stock_actual <= self.stock_minimo
