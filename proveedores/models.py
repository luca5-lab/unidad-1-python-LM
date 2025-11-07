from django.db import models

TIPO_PRODUCTO = [
    ('Liquido', 'Liquido'),
    ('Seco', 'Seco'),
]

class Desempeno(models.Model):
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE, related_name='desempenos')
    calidad = models.IntegerField(default=0)
    entrega = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.proveedor.nombre} - Desempeño {self.fecha.strftime('%Y-%m-%d')}"

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=20)
    contacto = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

    

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_producto = models.CharField(
        max_length=50,
        choices=[('Liquido', 'Líquido'), ('Seco', 'Seco')]
    )
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        related_name="productos"  # 👈 esto es clave
    )

    def __str__(self):
        return self.nombre

