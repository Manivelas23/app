from django import forms
from django.forms import ModelForm

from core.models import Fecha, prueba
from datetime import datetime


class FechaForm(ModelForm):
    class Meta:
        model = Fecha
        fields = '__all__'
        labels = {
            'id_prueba': 'Selecccione el Id de la Prueba'
        }


class PruebaForm(ModelForm):
    class Meta:
        model = prueba
        fields = ['id','tipo_prueba','tipo_licencia','id_curso']

