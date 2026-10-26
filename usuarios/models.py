
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


class PerfilEmpleado(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name="perfil",
        verbose_name="Usuario",
    )

    carnet_identidad = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Carnet de identidad",
    )

    telefono = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Teléfono",
    )

    cargo = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Cargo laboral",
    )

    activo = models.BooleanField(
        default=True,
        verbose_name="Empleado activo",
    )

    class Meta:
        verbose_name = "Perfil de empleado"
        verbose_name_plural = "Perfiles de empleados"

    def __str__(self):
        return f"{self.usuario.get_full_name()} - CI: {self.carnet_identidad}"
