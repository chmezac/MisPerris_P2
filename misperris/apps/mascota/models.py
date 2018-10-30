from django.db import models
from apps.adopcion.models import Persona

# Create your models here.

class Mascota(models.Model):

    DISPONIBLE = 'Disponible'
    ADOPTADO = 'Adoptado'
    RESCATADO = 'Rescatado'
    
    STATE_CHOICES = (
        (DISPONIBLE, 'Disponible'),
        (ADOPTADO, 'Adoptado'),
        (RESCATADO, 'Rescatado'),
    )

    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=RESCATADO)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)