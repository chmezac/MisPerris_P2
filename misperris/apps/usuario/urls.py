from django.shortcuts import render, redirect
from django.urls import path, include
from apps.usuario.views import RegistroUsuario, entrar, PasswordResetView, PasswordReset

urlpatterns = [
    path('registrar/', RegistroUsuario.as_view(), name='registrar'),
    path('', entrar, name='entrar'),
    path('pass/', PasswordResetView, name='PasswordResetView'),
]
