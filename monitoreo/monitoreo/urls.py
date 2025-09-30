from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from dispositivos import views
from dispositivos.views import (
    inicio, 
    dispositivo, 
    crear_dispositivo, 
    editar_dispositivo, 
    eliminar_dispositivo
)

urlpatterns = [
    path('admin/', admin.site.urls),

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

    #inicio sesion
    path('login/', views.login_view, name='login'),

    #registrarse
    path('register/', views.register_view, name='register'),

    path('dashboard', views.dashboard_view, name='dashboard'), 

    path('password-reset', views.password_reset_view, name='password-reset'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

