from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.conf import settings

class Command(BaseCommand):
    help = "Seed basic data: groups and two users (superuser and limitado)."

    def handle(self, *args, **options):
       
        g_admin, _ = Group.objects.get_or_create(name='admin')
        g_limitado, _ = Group.objects.get_or_create(name='maestro')

       
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin12@.com', 'admin123')
            self.stdout.write('Superuser "admin" creado con contraseña: admin123')
        else:
            self.stdout.write('Superuser "admin" ya existe.')

       
        if not User.objects.filter(username='maestro').exists():
            u = User.objects.create_user('maestro', 'maestro53@gmail.com', 'master123')
            u.is_staff = True
            u.save()
            u.groups.add(g_limitado)
            self.stdout.write('Usuario "maestro" creado con contraseña: master123')
        else:
            self.stdout.write('Usuario "maestro" ya existe.')

        self.stdout.write('Seed completado. Ajusta contraseñas y corre migrations si hace falta.')