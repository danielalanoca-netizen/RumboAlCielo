
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario, PerfilEmpleado


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "rol",
        "is_active",
    )

    list_filter = ("rol", "is_active", "is_staff")

    fieldsets = UserAdmin.fieldsets + (
        ("Información del sistema", {"fields": ("rol",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Información del sistema", {"fields": ("rol",)}),
    )


@admin.register(PerfilEmpleado)
class PerfilEmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        "carnet_identidad",
        "usuario",
        "telefono",
        "cargo",
        "activo",
    )

    search_fields = (
        "carnet_identidad",
        "usuario__username",
        "usuario__first_name",
        "usuario__last_name",
    )

    list_filter = ("activo",)
