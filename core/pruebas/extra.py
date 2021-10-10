from core.models import prueba, curso, sede
from django.db import models


def getModelVerbosename():
    return [name.verbose_name for name in prueba._meta.get_fields()[1:4] if hasattr(name, 'verbose_name')] + [
        name.verbose_name for name in curso._meta.get_fields()[-3:] if hasattr(name, 'verbose_name')]


def get_pruebas():
    data = []
    try:
        pruebas_select_related = prueba.objects.select_related()
        for i in pruebas_select_related:
            dict_pruebas = {
                'id': i.id,
                'tipo_prueba': i.tipo_prueba,
                'tipo_licencia': i.tipo_licencia,
                'nomb_curso': i.id_curso.nomb_curso,
                'tipo_curso': i.id_curso.tipo_curso,
                'desc_curso': i.id_curso.desc_curso
            }
            data.append(dict_pruebas)
    except Exception as e:
        data['error'] = str(e)
    return data
