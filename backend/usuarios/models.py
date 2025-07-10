from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('empleado', 'Empleado'),
        ('encargado', 'Encargado'),
        ('jefe', 'Jefe'),
    )
    rol = models.CharField(max_length=20, choices=ROLES, default='empleado')

    def __str__(self):
        return f"{self.username} ({self.rol})"
