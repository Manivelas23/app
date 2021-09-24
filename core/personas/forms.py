from core.models import *
from django.forms import *
from django.forms import forms

tipo_identificacion_choices = tipo_identificacion.objects.all().values_list("tipo", 'tipo')

choice_list = []

for i in tipo_identificacion_choices:
    choice_list.append(i)
tipo_identificacion_choices = tipo_identificacion.objects.all().values_list("tipo", 'tipo')

choice_list = []

for i in tipo_identificacion_choices:
    choice_list.append(i)


class PersonaForm(ModelForm):
    class Meta:
        model = persona
        fields = ['numero_identificacion', 'nombre', 'primer_apellido', 'segundo_apellido',
                  'tipo_identificacion_persona']

        widgets = {
            "tipo_identificacion_persona": Select(choices=choice_list)
        }


        widgets = {
            "tipo_identificacion_persona": Select(choices=choice_list)
        }

