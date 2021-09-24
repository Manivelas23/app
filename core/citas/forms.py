from django.forms import *
from core.models import cita, persona, fecha


class CitaForm(ModelForm):
    class Meta:
        model = cita
        fields = ['id_persona', 'otras_indicaciones']

        widget = {
            'id_persona': ModelChoiceField(queryset=persona.objects.all(), widget=Select(attrs={
                'class': 'select2 form-control'
            })),
            'id_fecha_cita': ModelChoiceField(queryset=fecha.objects.all(), widget=Select(attrs={
                'class': 'select2 form-control'
            })),
        }
