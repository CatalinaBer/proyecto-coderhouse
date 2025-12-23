from django.shortcuts import render
from .models import Post
from .forms import PostForm, ServicioForm, ClienteForm

def home(request):
    return render(request, "estudio/index.html")


def crear_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "estudio/crear_post.html", {"form": form})


def crear_servicio(request):
    form = ServicioForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "estudio/crear_servicio.html", {"form": form})


def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "estudio/crear_cliente.html", {"form": form})


def buscar_post(request):
    if request.GET.get("titulo"):
        posts = Post.objects.filter(titulo__icontains=request.GET["titulo"])
        return render(request, "estudio/resultados.html", {"posts": posts})
    return render(request, "estudio/buscar_post.html")