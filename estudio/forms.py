from django import forms
from .models import Post, Servicio, Cliente

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'