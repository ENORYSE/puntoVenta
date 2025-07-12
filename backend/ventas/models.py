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


#aca pongo todo lo nuevo

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    cuit = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=300, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


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


class MovimientoStock(models.Model):
    class Tipo(models.TextChoices):
        ENTRADA = 'entrada', 'Entrada'
        SALIDA = 'salida', 'Salida'
        AJUSTE = 'ajuste', 'Ajuste'

    producto = models.ForeignKey( Producto, on_delete=models.CASCADE, related_name='movimientos_stock')
    cantidad = models.IntegerField()
    tipo = models.CharField( max_length=20, choices=Tipo.choices)
    fecha = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True)
    origen = models.CharField(max_length=100, blank=True)
    documento_ref = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Movimiento de Stock"
        verbose_name_plural = "Movimientos de Stock"
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.producto.nombre} - {self.get_tipo_display()} - {self.cantidad}"


class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='compras')
    fecha = models.DateField()
    total = models.DecimalField(max_digits=12, decimal_places=2)
    numero_factura = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ['-fecha']

    def __str__(self):
        return f"Compra {self.numero_factura} - {self.proveedor.nombre}"


class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='detalles_compra')
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Detalle de Compra"
        verbose_name_plural = "Detalles de Compra"
        unique_together = ['compra', 'producto']

    def __str__(self):
        return f"{self.compra.numero_factura} - {self.producto.nombre}"

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario


class Venta(models.Model):

    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12,decimal_places=2)
    tipo_comprobante = models.CharField(max_length=20)
    numero_comprobante = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['-fecha']

    def __str__(self):
        return f"Venta {self.numero_comprobante} - ${self.total}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='detalles_venta')
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Venta"
        unique_together = ['venta', 'producto']

    def __str__(self):
        return f"{self.venta.numero_comprobante} - {self.producto.nombre}"

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario