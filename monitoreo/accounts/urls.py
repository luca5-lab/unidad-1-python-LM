from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from django.shortcuts import render
from . import views


urlpatterns = [
    path("login/", LoginView.as_view(
        template_name="accounts/login.html",
        authentication_form=LoginForm,
        redirect_authenticated_user=True
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("registrarse/", views.registrarse, name="registrarse"),
]
