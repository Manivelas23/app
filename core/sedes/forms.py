from django.forms import ModelForm
from core.models import sede


class SedeForm(ModelForm):
    class Meta:
        model = sede
        fields = '__all__'




