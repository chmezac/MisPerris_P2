from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.usuario.forms import RegistroForm

# Create your views here.
class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('mascota:mascota_listar')


def entrar(request):
    return render(request, 'usuario/entrar.html')

def PasswordResetView(request):
    return render(request, 'usuario/password_reset_email.html')

class PasswordReset(CreateView):
	model = User
	template_name = "usuario/password_reset_email.html.html"
