from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("crear-post/", crear_post),
    path("crear-servicio/", crear_servicio),
    path("crear-cliente/", crear_cliente),
    path("buscar-post/", buscar_post),
]