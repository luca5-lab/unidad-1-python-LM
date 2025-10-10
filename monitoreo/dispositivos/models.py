from django.db import models
from organizations.models import Organization


class BaseModel(models.Model):
    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
    ]

    estado = models.CharField(max_length=10, choices=ESTADOS, default="ACTIVO")
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)       
    deleted_at = models.DateTimeField(null=True, blank=True)

    

    class Meta:
        abstract = True  


class Categoria(BaseModel):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Zona(BaseModel):
    organization = models.ForeignKey(
    'organizations.Organization',
    on_delete=models.CASCADE,
    related_name='zonas_dispositivo',
    default = 1
    )
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.organization.name})"


class Dispositivo(BaseModel):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    consumo_maximo = models.IntegerField()  # watts
    imagen = models.ImageField(upload_to='dispositivos/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Medicion(BaseModel):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    consumo = models.FloatField()  # kWh

    def __str__(self):
        return f"{self.dispositivo} - {self.consumo} kWh"


class Alerta(BaseModel):
    NIVEL_CHOICES = [
        ("GRAVE", "Grave"),
        ("ALTA", "Alta"),
        ("MEDIA", "Media"),
    ]
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=200)
    nivel = models.CharField(max_length=5, choices=NIVEL_CHOICES, default="MEDIA")
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alerta {self.dispositivo} - {self.mensaje}"
