from core.models import prueba, curso, sede
from django.db import models


def getModelVerbosename():
    return [name.verbose_name for name in prueba._meta.get_fields()[1:5] if hasattr(name, 'verbose_name')] + [
        name.verbose_name for name in curso._meta.get_fields()[-3:] if hasattr(name, 'verbose_name')]


def getPruebaData():
    data = []
    lista_pruebas = [i.toJSON() for i in prueba.objects.all()]
    lista_cursos = [i.toJSON() for i in curso.objects.all()]
    lista_curso_pruebas = list(zip(lista_pruebas, lista_cursos))

    dict_final_prueba = {}
    for i, j in lista_curso_pruebas:
        dict_final_prueba = i
        j['id_curso'] = j.pop('id')
        dict_final_prueba.update(j)
        data.append(dict_final_prueba)
    return data
