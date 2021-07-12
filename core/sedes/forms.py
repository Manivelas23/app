from django.forms import *
from core.models import sede


class SedeForm(ModelForm):
    class Meta:
        model = sede
        fields = '__all__'
        labels = {
            'ubicacion':'Ingrese la ubicación de la sede:'
        }




