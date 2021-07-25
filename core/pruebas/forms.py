from django.forms import *
from core.models import prueba
from datetime import datetime

class PruebaForm(ModelForm):
    class Meta:
        model = prueba
        fields = '__all__'
        labels = {
            'tipo_prueba':'Ingrese aquí el tipo de prueba:',
            'tipo_licencia':'Ingrese aquí el tipo de licencia:',
        }




