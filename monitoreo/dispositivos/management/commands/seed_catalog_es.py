from django.core.management.base import BaseCommand
from django.db import transaction
from dispositivos.models import Categoria, Zona, Dispositivo, Medicion, Alerta

class Command(BaseCommand):
    help = "Carga datos iniciales de categorías, zonas, dispositivos, mediciones y alertas"

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            # Categorías
            cat_luz, _ = Categoria.objects.get_or_create(nombre="Iluminación")
            cat_sensor, _ = Categoria.objects.get_or_create(nombre="Sensores")

            # Zonas
            zona1, _ = Zona.objects.get_or_create(nombre="Oficina")
            zona2, _ = Zona.objects.get_or_create(nombre="Almacén")

            # Dispositivos
            disp1, _ = Dispositivo.objects.get_or_create(
                nombre="Panel LED 40W",
                categoria=cat_luz,
                zona=zona1,
                consumo_maximo=40
            )
            disp2, _ = Dispositivo.objects.get_or_create(
                nombre="Sensor de Movimiento PIR",
                categoria=cat_sensor,
                zona=zona2,
                consumo_maximo=5
            )

            # Mediciones de ejemplo
            Medicion.objects.get_or_create(
                dispositivo=disp1,
                consumo=12.5
            )
            Medicion.objects.get_or_create(
                dispositivo=disp2,
                consumo=2.3
            )

            # Alertas de ejemplo
            Alerta.objects.get_or_create(
                dispositivo=disp1,
                mensaje="Consumo excedido en horario nocturno",
                nivel="ALTA"
            )
            Alerta.objects.get_or_create(
                dispositivo=disp2,
                mensaje="Sensor inactivo más de 24h",
                nivel="MEDIA"
            )

        self.stdout.write(self.style.SUCCESS("Seed ejecutado correctamente"))
