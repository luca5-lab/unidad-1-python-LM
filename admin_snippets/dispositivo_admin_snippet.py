# Ejemplo de snippet para agregar en dispositivos/admin.py o donde registres el modelo Dispositivo

from django import forms
from django.contrib import admin
from .models import Dispositivo  # ajusta import según tu proyecto

# Validación con ModelForm
class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = '__all__'

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('consumo_maximo') is not None and cleaned.get('consumo_maximo') <= 0:
            raise forms.ValidationError('Consumo máximo debe ser mayor que 0.')
        return cleaned

# Acción personalizada
def marcar_en_mantenimiento(modeladmin, request, queryset):
    updated = queryset.update(status='mantenimiento')
    modeladmin.message_user(request, f"{updated} equipos marcados en mantenimiento")
marcar_en_mantenimiento.short_description = "Marcar seleccionados en mantenimiento"

# Scoping según organización del usuario
class DispositivoAdmin(admin.ModelAdmin):
    form = DispositivoForm
    list_display = ('id','nombre','organization','status')
    search_fields = ('nombre',)
    list_filter = ('status','organization')
    actions = [marcar_en_mantenimiento]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            profile = request.user.userprofile
        except Exception:
            return qs.none()
        return qs.filter(organization=profile.organization)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            actions.pop('delete_selected', None)
        return actions

# Luego registra:
# admin.site.register(Dispositivo, DispositivoAdmin)