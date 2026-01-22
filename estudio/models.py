from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150, blank=True)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titulo


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre