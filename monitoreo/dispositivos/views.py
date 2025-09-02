from django.shortcuts import render
from .models import Dispositivo

def inicio(request):
    dispositivos = Dispositivo.objects.select_related("categoria")

    return render(request, "dispositivos/inicio.html", {"dispositivos": dispositivos})

def dispositivo(request, dispositivo_id);
    dispositivo = Dispositivo.objects.
    get(id=dispositivo_id)

    return render (request,)