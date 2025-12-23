from django import forms
from .models import Post, Servicio, Cliente

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '_all_'


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '_all_'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '_all_'