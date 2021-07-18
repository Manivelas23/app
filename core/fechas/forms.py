from django import forms
from django.forms import ModelForm
from tempus_dominus.widgets import DatePicker

from core.models import fecha
from datetime import datetime


class FechaForm(ModelForm):
    class Meta:
        model = fecha
        fields = '__all__'
        fecha_disponible = forms.DateTimeField(
            input_formats=['%d/%m/%Y %H:%M'],
            widget=forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        )
        labels = {
            'fecha_disponible': 'Seleccione una fecha disponible',
            'id_sede': 'Seleccione una sede'
        }
