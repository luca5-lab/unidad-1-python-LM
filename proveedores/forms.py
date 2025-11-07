from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Proveedor, Producto, Desempeno, TIPO_PRODUCTO
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class AgregarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'tipo_producto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'tipo_producto': forms.Select(attrs={'class': 'form-select'}),
        }



class DesempenoForm(forms.ModelForm):
    class Meta:
        model = Desempeno
        fields = ['calidad', 'entrega', 'precio']
        widgets = {
            'calidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
            'entrega': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
        }

class ProveedorForm(forms.ModelForm):
    # Campo extra para el producto
    producto_nombre = forms.CharField(
        max_length=100,
        required=True,
        label="Nombre del producto",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'})
    )

    class Meta:
        model = Proveedor
        fields = ['nombre', 'rut', 'contacto', 'email']  # solo campos reales de Proveedor
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proveedor'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT del proveedor'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del contacto'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Inicializamos el producto si ya existe
        if self.instance.pk and self.instance.productos.exists():
            self.fields['producto_nombre'].initial = self.instance.productos.first().nombre


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Usuario'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña'
            }
        )
    )
class EditarPerfilForm(forms.ModelForm):
    password = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        help_text="Dejar vacío si no deseas cambiar la contraseña"
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # mantenemos email visible

    def clean_email(self):
        email = self.cleaned_data['email']
        # Validamos si otro usuario ya tiene ese email
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este correo ya está en uso.")
        return email
