
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import PerfilEmpleado, Usuario


class RegistroEmpleadoForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nombre",
        max_length=150,
        required=True,
    )
    last_name = forms.CharField(
        label="Apellido",
        max_length=150,
        required=True,
    )
    email = forms.EmailField(
        label="Correo electrónico",
        required=True,
    )
    carnet_identidad = forms.CharField(
        label="Carnet de identidad",
        max_length=20,
        required=True,
    )
    telefono = forms.CharField(
        label="Teléfono",
        max_length=20,
        required=False,
    )
    cargo = forms.CharField(
        label="Cargo laboral",
        max_length=100,
        required=False,
    )

    class Meta:
        model = Usuario
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "carnet_identidad",
            "telefono",
            "cargo",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": field.label,
            })

        self.fields["username"].label = "Nombre de usuario"
        self.fields["username"].help_text = (
            "Utiliza un nombre de usuario único."
        )
        self.fields["password1"].label = "Contraseña"
        self.fields["password2"].label = "Confirmar contraseña"

    def clean_carnet_identidad(self):
        carnet = self.cleaned_data["carnet_identidad"].strip()

        if PerfilEmpleado.objects.filter(
            carnet_identidad__iexact=carnet
        ).exists():
            raise forms.ValidationError(
                "Ya existe un empleado con ese carnet."
            )

        return carnet
