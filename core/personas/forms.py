from core.models import *
from django.forms import *
from django.forms import forms


def get_tipo_identificaciones():
    choice_list = []
    try:
        tipo_identificacion_choices = tipo_identificacion.objects.all().values_list("tipo", 'tipo')

        choice_list = [i for i in tipo_identificacion_choices]
    except Exception as e:
        print(str(e))
    return choice_list


class PersonaForm(ModelForm):
    class Meta:
        model = persona
        fields = ['numero_identificacion', 'nombre', 'primer_apellido', 'segundo_apellido',
                  'tipo_identificacion_persona']

        widgets = {
            "tipo_identificacion_persona": Select(choices=get_tipo_identificaciones())
        }
