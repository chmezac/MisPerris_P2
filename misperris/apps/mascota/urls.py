from django.urls import path, include
from django.shortcuts import render, redirect

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete


app_name = 'mascota' 

urlpatterns = [
     path('', index, name='index'),
     path('nuevo/', MascotaCreate.as_view(), name='mascota_crear'),
     path('listar/', MascotaList.as_view(), name='mascota_listar'),
     path('editar/<int:pk>/', MascotaUpdate.as_view(), name='mascota_editar'),
     path('eliminar/<int:pk>/', MascotaDelete.as_view(), name='mascota_eliminar'),
]