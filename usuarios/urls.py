
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "usuarios"

urlpatterns = [
    path("registro/", views.registro_empleado, name="registro"),
    path("login/", views.iniciar_sesion, name="login"),
    path("inicio/", views.inicio, name="inicio"),
    path("logout/", views.cerrar_sesion, name="logout"),

    path(
        "recuperar-password/",
        auth_views.PasswordResetView.as_view(
            template_name="usuarios/recuperar_password.html",
            email_template_name="usuarios/recuperar_password_email.html",
            subject_template_name="usuarios/recuperar_password_asunto.txt",
            success_url="/usuarios/recuperar-password/enviado/",
        ),
        name="password_reset",
    ),
    path(
        "recuperar-password/enviado/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="usuarios/recuperar_password_enviado.html",
        ),
        name="password_reset_done",
    ),
    path(
        "restablecer-password/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="usuarios/restablecer_password.html",
            success_url="/usuarios/restablecer-password/completo/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "restablecer-password/completo/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="usuarios/restablecer_password_completo.html",
        ),
        name="password_reset_complete",
    ),
]
