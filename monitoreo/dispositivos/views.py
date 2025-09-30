from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.utils import timezone
from .models import Categoria, Zona, Dispositivo, Medicion, Alerta
from .forms import DispositivoForm
from .forms import MedicionForm

# -----------------------------
# Vista principal (antes "inicio")
# -----------------------------
def inicio(request):
    # Conteo de dispositivos por categoría y zona
    categories = Categoria.objects.annotate(device_count=Count('dispositivo'))
    zones = Zona.objects.annotate(device_count=Count('dispositivo'))

    # Filtrado según GET
    dispositivos = Dispositivo.objects.select_related("categoria", "zona")
    categoria_id = request.GET.get('categoria')
    zona_id = request.GET.get('zona')

    if categoria_id:
        dispositivos = dispositivos.filter(categoria_id=categoria_id)
        # Filtrar zonas solo relacionadas con la categoría seleccionada
        zones = zones.filter(dispositivo__categoria_id=categoria_id).distinct()

    if zona_id:
        dispositivos = dispositivos.filter(zona_id=zona_id)

    # Alertas de la semana
    alerts = {
        'grave': Alerta.objects.filter(nivel='GRAVE').count(),
        'alta': Alerta.objects.filter(nivel='ALTA').count(),
        'media': Alerta.objects.filter(nivel='MEDIA').count(),
    }

    recent_alerts = Alerta.objects.select_related('dispositivo').order_by('-fecha')[:2]

    # Últimas 10 mediciones
    measurements = Medicion.objects.select_related('dispositivo').order_by('-fecha')[:10]

    context = {
        'categories': categories,
        'zones': zones,
        'alerts': alerts,
        'recent_alerts': recent_alerts,
        'measurements': measurements,
        'dispositivos': dispositivos,
    }

    return render(request, 'dispositivos/inicio.html', context)

# -----------------------------
# Detalle de un dispositivo
# -----------------------------
def dispositivo(request, dispositivo_id):
    dispositivo_obj = get_object_or_404(Dispositivo, id=dispositivo_id)
    return render(request, 'dispositivos/dispositivo.html', {'dispositivo': dispositivo_obj})



def crear_medicion(request):
    if request.method == 'POST':
        form = MedicionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige a tu página principal
    else:
        form = MedicionForm()
        # Filtrar dispositivos activos (opcional)
        form.fields['dispositivo'].queryset = Dispositivo.objects.filter(estado='ACTIVO')

    return render(request, 'dispositivos/crear_medicion.html', {'form': form})


# -----------------------------
# Crear un dispositivo
# -----------------------------
def crear_dispositivo(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = DispositivoForm()
    return render(request, 'dispositivos/crear.html', {'form': form})

# -----------------------------
# Editar un dispositivo
# -----------------------------
def editar_dispositivo(request, dispositivo_id):
    dispositivo_obj = get_object_or_404(Dispositivo, id=dispositivo_id)
    if request.method == 'POST':
        form = DispositivoForm(request.POST,request.FILES, instance=dispositivo_obj)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = DispositivoForm(instance=dispositivo_obj)
    return render(request, 'dispositivos/editar.html', {'form': form, 'dispositivo': dispositivo})

# -----------------------------
# Eliminar un dispositivo
# -----------------------------
def eliminar_dispositivo(request, dispositivo_id):
    dispositivo_obj = get_object_or_404(Dispositivo, id=dispositivo_id)
    if request.method == 'POST':
        dispositivo_obj.delete()
        return redirect('inicio')
    return render(request, 'dispositivos/eliminar.html', {'dispositivo': dispositivo_obj})

def login_view(request):
    return render(request, 'dispositivos/iniciar_sesion.html')

def register_view(request):
    if request.method == 'POST':
        # contenido pa registro
        pass
    return render(request, 'dispositivos/registrarse.html')

def dashboard_view(request):
    return render(request, 'dispositivos/dashboard.html')

def password_reset_view(request):
    return render(request, 'dispositivos/recuperacion.html')

