from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Mensaje


@login_required
def inbox(request):
    mensajes = Mensaje.objects.filter(
        destinatario=request.user
    ).order_by("-fecha")

    return render(request, "mensajes/inbox.html", {
        "mensajes": mensajes
    })


@login_required
def enviar_mensaje(request):
    usuarios = User.objects.exclude(id=request.user.id)

    if request.method == "POST":
        destinatario_id = request.POST.get("destinatario")
        contenido = request.POST.get("contenido")

        if destinatario_id and contenido:
            Mensaje.objects.create(
                remitente=request.user,
                destinatario_id=destinatario_id,
                contenido=contenido
            )
            return redirect("/mensajes/")

    return render(request, "mensajes/enviar.html", {
        "usuarios": usuarios
    })