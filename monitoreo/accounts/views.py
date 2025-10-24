from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.contrib import messages


def registrarse(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "El correo ya está registrado.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            
            # Asignar al grupo Proveedor (solo vista)
            grupo_proveedor, _ = Group.objects.get_or_create(name='Proveedor')
            user.groups.add(grupo_proveedor)
            
            user.save()
            login(request, user)
            return redirect('dispositivos')

    return render(request, 'accounts/registrarse.html')