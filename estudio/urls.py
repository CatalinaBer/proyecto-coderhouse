from django.urls import path
from .views import (
    home,
    about,
    crear_post,
    crear_servicio,
    crear_cliente,
    buscar_post,
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),

    # Pages / Blog
    path("pages/", PostListView.as_view(), name="pages"),
    path("pages/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("pages/<int:pk>/editar/", PostUpdateView.as_view(), name="post_update"),
    path("pages/<int:pk>/eliminar/", PostDeleteView.as_view(), name="post_delete"),

    # Formularios
    path("crear-post/", crear_post, name="crear_post"),
    path("crear-servicio/", crear_servicio, name="crear_servicio"),
    path("crear-cliente/", crear_cliente, name="crear_cliente"),

    # Búsqueda
    path("buscar-post/", buscar_post, name="buscar_post"),
]