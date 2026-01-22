from django.urls import path
from . import views

app_name = "mensajes"

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("enviar/", views.enviar_mensaje, name="enviar"),
]