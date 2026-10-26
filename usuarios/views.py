
from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect, render

from .forms import RegistroEmpleadoForm
from .models import PerfilEmpleado, Usuario

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

@transaction.atomic
def registro_empleado(request):
 if request.user.is_authenticated:
    return redirect("usuarios:inicio")

    if request.method == "POST":
        form = RegistroEmpleadoForm(request.POST)

        if form.is_valid():
            usuario = form.save(commit=False)

            # El registro público nunca puede asignar el rol ADMIN.
            usuario.rol = Usuario.Rol.EMPLEADO
            usuario.email = form.cleaned_data["email"].strip()
            usuario.save()

            PerfilEmpleado.objects.create(
                usuario=usuario,
                carnet_identidad=form.cleaned_data["carnet_identidad"],
                telefono=form.cleaned_data["telefono"],
                cargo=form.cleaned_data["cargo"],
            )

            messages.success(
                request,
                "Tu cuenta fue creada correctamente. "
                "Ya puedes iniciar sesión.",
            )
            return redirect("usuarios:login")
    else:
        form = RegistroEmpleadoForm()

    return render(
        request,
        "usuarios/registro.html",
        {"form": form},
    )




def iniciar_sesion(request):
    if request.user.is_authenticated:
        if request.user.rol == Usuario.Rol.ADMIN:
            return redirect("/admin/")

        return redirect("usuarios:inicio")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)

            if usuario.rol == Usuario.Rol.ADMIN:
                return redirect("/admin/")

            return redirect("usuarios:inicio")
    else:
        form = AuthenticationForm(request)

    return render(
        request,
        "usuarios/login.html",
        {"form": form},
    )




@login_required
def inicio(request):
    if request.user.rol == Usuario.Rol.ADMIN:
        return redirect("/admin/")

    return render(
        request,
        "usuarios/inicio.html",
    )



def cerrar_sesion(request):
    if request.method == "POST":
        logout(request)
        return redirect("usuarios:login")

    return redirect("usuarios:inicio")
