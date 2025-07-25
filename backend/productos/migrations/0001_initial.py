# Generated by Django 5.2.4 on 2025-07-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barra', models.CharField(max_length=100, unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_actual', models.IntegerField(default=0)),
                ('stock_minimo', models.IntegerField(default=0)),
                ('unidad_medida', models.CharField(default='unidad', max_length=50)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nombre'],
            },
        ),
    ]
