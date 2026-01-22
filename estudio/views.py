from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm, ServicioForm, ClienteForm


# -------------------------
# VISTAS FUNCIONALES
# -------------------------

def home(request):
    posts = Post.objects.all().order_by("-fecha")
    return render(request, "estudio/home.html", {"posts": posts})


def about(request):
    return render(request, "estudio/about.html")


@login_required
def crear_post(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.autor = request.user
        post.save()

        messages.success(request, "Post creado correctamente")
        return redirect("pages")

    return render(request, "estudio/crear_post.html", {"form": form})


@login_required
def crear_servicio(request):
    form = ServicioForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Servicio creado correctamente")
        return redirect("home")

    return render(request, "estudio/crear_servicio.html", {"form": form})


@login_required
def crear_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Cliente creado correctamente")
        return redirect("home")

    return render(request, "estudio/crear_cliente.html", {"form": form})


def buscar_post(request):
    posts = []

    if request.GET.get("titulo"):
        posts = Post.objects.filter(titulo__icontains=request.GET["titulo"])

    return render(request, "estudio/buscar_post.html", {"posts": posts})


# -------------------------
# CLASS BASED VIEWS (CBV)
# -------------------------

class PostListView(ListView):
    model = Post
    template_name = "estudio/pages.html"
    context_object_name = "posts"
    ordering = ["-fecha"]


class PostDetailView(DetailView):
    model = Post
    template_name = "estudio/post_detail.html"
    context_object_name = "post"


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["titulo", "subtitulo", "contenido", "imagen"]
    template_name = "estudio/post_form.html"
    success_url = reverse_lazy("pages")


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "estudio/post_confirm_delete.html"
    success_url = reverse_lazy("pages")