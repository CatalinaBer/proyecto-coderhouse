from django.shortcuts import render

def home(request):
    return render(request, "estudio/index.html")