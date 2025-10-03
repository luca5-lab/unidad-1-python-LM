from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.views.generic import TemplateView
from dispositivos import views
from dispositivos.views import (
    inicio, 
    dispositivo, 
    crear_dispositivo, 
    editar_dispositivo, 
    eliminar_dispositivo,
    dashboard_view
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dashboard', views.dashboard_view, name='dashboard'),

    path("", include("accounts.urls")),

    # Página principal y listado de dispositivos
    path('', inicio, name='inicio'),
    path('dispositivos/', inicio, name='dispositivos'),

    # Crear dispositivo
    path('dispositivos/crear/', crear_dispositivo, name='crear_dispositivo'),

    # Editar dispositivo
    path('dispositivos/editar/<int:dispositivo_id>/', editar_dispositivo, name='editar_dispositivo'),

    # Eliminar dispositivo
    path('dispositivos/eliminar/<int:dispositivo_id>/', eliminar_dispositivo, name='eliminar_dispositivo'),

    # Detalle de un dispositivo
    path('dispositivos/<int:dispositivo_id>/', dispositivo, name='dispositivo'),

    #mediciones
    path('mediciones/crear/', views.crear_medicion, name='crear_medicion'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

