from django.urls import path, include
from apps.mascota.views import index, mascota_view#, mascota_list
from django.shortcuts import render, redirect


app_name = 'mascota' 

urlpatterns = [
     path('', index, name='index'),
     path('nuevo/', mascota_view, name='mascota_crear'),
     #path('listar/', mascota_list, name='mascota_listar'),
]