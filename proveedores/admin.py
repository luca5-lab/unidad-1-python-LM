from django.contrib import admin

from django.contrib import admin
from .models import Proveedor, Categoria, Producto

admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Producto)
