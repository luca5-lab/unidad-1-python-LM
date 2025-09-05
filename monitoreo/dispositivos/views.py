from django.shortcuts import render, redirect
from .models import Dispositivo
from .forms import DispositivoForm

def inicio(request):
    dispositivos = Dispositivo.objects.select_related("categoria")

    return render(request, "dispositivos/inicio.html", {"dispositivos": dispositivos})

def dispositivo(request, dispositivo_id):
    dispositivo = Dispositivo.objects.get(id=dispositivo_id)

def crear_dispositivo(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_dispositivos')
    else:
        form = DispositivoForm()
    

    return render (request, 'dispositivos/crear.html', {'form': form})