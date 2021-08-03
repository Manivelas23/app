from django import forms
from django.forms import ModelForm
from tempus_dominus.widgets import DatePicker

from core.models import fecha, prueba
from datetime import datetime


class FechaForm(ModelForm):
    class Meta:
        model = fecha
        fields = '__all__'
        labels = {
            'id_prueba': 'Selecccione el Id de la Prueba'
        }


class PruebaForm(ModelForm):
    class Meta:
        model = prueba
        fields = ['id','tipo_prueba','tipo_licencia','id_curso']

