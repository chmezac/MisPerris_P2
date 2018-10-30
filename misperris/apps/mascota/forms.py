from django import forms
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'raza',
            'descripcion',
            'state',
            'persona',
        ]

        labels = {
            'nombre': 'Nombre',
            'raza': 'Raza',
            'descripcion': 'Descripcion',
            'state': 'Estado',
            'persona': 'Adoptante',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'raza': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),

        }


        