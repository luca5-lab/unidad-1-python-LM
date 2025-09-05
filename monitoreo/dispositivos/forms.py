from django import forms
from .models import Dispositivo  # importa tu modelo

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo  # Aquí va el modelo asociado
        fields = '__all__'   # o una lista con los campos que quieras usar