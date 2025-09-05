from django.contrib import admin


from .models import Categoria, Zona, Dispositivo, Alerta

admin.site.register([Categoria, Zona ])


@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'zona', 'consumo_maximo')



@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ('dispositivo', 'mensaje', 'fecha')