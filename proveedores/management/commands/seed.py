# proveedores/management/commands/seed_users.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = "Crea 3 usuarios (lucas, editor, vista) y les asigna permisos específicos para la app 'proveedores'."

    def handle(self, *args, **options):
        password = "ola123"

        # 1) Usuario lucas: todos los permisos del app 'proveedores'
        username_lucas = "lucas@gmail.com"
        lucas, created = User.objects.get_or_create(
            username=username_lucas,
            defaults={"email": username_lucas, "first_name": "Lucas"}
        )
        if created:
            lucas.set_password(password)
            lucas.is_staff = True
            lucas.save()
            self.stdout.write(self.style.SUCCESS(f"Usuario creado: {username_lucas}"))
        else:
            # aseguramos password y is_staff (opcional)
            lucas.set_password(password)
            lucas.is_staff = True
            lucas.save()
            self.stdout.write(self.style.WARNING(f"Usuario ya existía (actualizado password/is_staff): {username_lucas}"))

        # Asignar todas las permissions del app 'proveedores' a lucas
        perms_app = Permission.objects.filter(content_type__app_label='proveedores')
        lucas.user_permissions.set(perms_app)
        self.stdout.write(self.style.SUCCESS(f"Asignadas {perms_app.count()} permisos de 'proveedores' a {username_lucas}"))

        # 2) Usuario editor: add & change para Proveedor y Producto (y view)
        username_editor = "editor@gmail.com"
        editor, created = User.objects.get_or_create(
            username=username_editor,
            defaults={"email": username_editor, "first_name": "Editor"}
        )
        if created:
            editor.set_password(password)
            editor.is_staff = False
            editor.save()
            self.stdout.write(self.style.SUCCESS(f"Usuario creado: {username_editor}"))
        else:
            editor.set_password(password)
            editor.save()
            self.stdout.write(self.style.WARNING(f"Usuario ya existía (password actualizado): {username_editor}"))

        # Codenames que queremos darle al editor (sin delete)
        editor_codenames = [
            # Proveedor perms
            "add_proveedor", "change_proveedor", "view_proveedor",
            # Producto perms (si existe Producto model)
            "add_producto", "change_producto", "view_producto",
            # Si quieres incluir desempeño view/edit, añade "view_desempeno","add_desempeno","change_desempeno" si aplican
        ]
        editor_perms = Permission.objects.filter(codename__in=editor_codenames, content_type__app_label='proveedores')
        editor.user_permissions.set(editor_perms)
        self.stdout.write(self.style.SUCCESS(f"Asignados {editor_perms.count()} permisos al editor."))

        # 3) Usuario vista: solo permisos de view para Proveedor y Producto
        username_vista = "vista@gmail.com"
        vista, created = User.objects.get_or_create(
            username=username_vista,
            defaults={"email": username_vista, "first_name": "Vista"}
        )
        if created:
            vista.set_password(password)
            vista.is_staff = False
            vista.save()
            self.stdout.write(self.style.SUCCESS(f"Usuario creado: {username_vista}"))
        else:
            vista.set_password(password)
            vista.save()
            self.stdout.write(self.style.WARNING(f"Usuario ya existía (password actualizado): {username_vista}"))

        vista_codenames = [
            "view_proveedor",
            "view_producto",
            # y cualquier otro 'view_*' que quieras añadir
        ]
        vista_perms = Permission.objects.filter(codename__in=vista_codenames, content_type__app_label='proveedores')
        vista.user_permissions.set(vista_perms)
        self.stdout.write(self.style.SUCCESS(f"Asignados {vista_perms.count()} permisos al usuario vista."))

        self.stdout.write(self.style.SUCCESS("Seed usuarios completada."))
        self.stdout.write(self.style.WARNING("⚠️ Contraseña por defecto para los 3 usuarios: 'ola123'. Cámbiala en producción."))
