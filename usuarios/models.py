from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    class Rol(models.TextChoices):
        EMPLEADO = "EMPLEADO", "Empleado"
        ADMIN = "ADMIN", "Administrador"

    rol = models.CharField(
        max_length=10,
        choices=Rol.choices,
        default=Rol.EMPLEADO,
        verbose_name="Rol del usuario",
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
