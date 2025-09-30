from django import forms
from .models import Dispositivo, Medicion # importa tu modelo

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo  # Modelo asociado
        fields = ['nombre', 'categoria', 'zona', 'consumo_maximo', 'estado', 'imagen']  # Lista de campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'consumo_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'zona': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),  # asumiendo que estado es un select
            'imagen': forms.FileInput (attrs={'class': 'form-control'}), # input file bootstrap
        }

class MedicionForm(forms.ModelForm):
    class Meta:
        model = Medicion
        fields = ['dispositivo', 'consumo']
        widgets = {
            'dispositivo': forms.Select(attrs={'class': 'form-select'}),
            'consumo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
        labels = {
            'dispositivo': 'Dispositivo',
            'consumo': 'Valor de la medición',
        }