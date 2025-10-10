from django.contrib import admin
from django import forms
from .models import Categoria, Zona, Dispositivo, Alerta, Medicion


admin.site.register([Categoria, Zona])



class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = '__all__'

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('consumo_maximo') is not None and cleaned.get('consumo_maximo') <= 0:
            raise forms.ValidationError(' El consumo máximo debe ser mayor que 0.')
        return cleaned



class MedicionInline(admin.TabularInline):
    model = Medicion
    extra = 1  # número de filas vacías
    readonly_fields = ('fecha', 'consumo')



@admin.action(description="Desactivar seleccionados")
def marcar_en_mantenimiento(modeladmin, request, queryset):
    updated = queryset.update(estado='INACTIVO') 
    modeladmin.message_user(request, f"{updated} dispositivos marcados como en mantenimiento")

@admin.action(description="Activar seleccionados")
def marcar_como_activos(modeladmin, request, queryset):
    updated = queryset.update(estado='ACTIVO')
    modeladmin.message_user(request, f"{updated} dispositivos reactivados correctamente")



@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    form = DispositivoForm
    list_display = ('id', 'nombre', 'categoria', 'zona', 'consumo_maximo', 'estado')
    search_fields = ('nombre',)
    list_filter = ('categoria', 'zona', 'estado')
    inlines = [MedicionInline]  
    actions = [marcar_en_mantenimiento, marcar_como_activos]  

  
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            profile = request.user.userprofile
        except Exception:
            return qs.none()
        if hasattr(profile, 'organization'):
            return qs.filter(zona__organization=profile.organization)
        return qs


    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            actions.pop('delete_selected', None)
        return actions



@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ('dispositivo', 'mensaje', 'nivel', 'fecha', 'estado')
    list_filter = ('nivel', 'estado')
