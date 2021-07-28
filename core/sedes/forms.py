from django.forms import *
from django.forms import forms
from core.models import sede
from datetime import datetime

class SedeForm(ModelForm):

    CHOICES = (('SI', 'SI'),('NO', 'NO'),)
    activo = ChoiceField(choices=CHOICES)

    class Meta:
        model = sede
        fields = '__all__'
        labels = {
            'ubicacion':'Ingrese aquí la ubicación de la sede:'
        }
