import numpy as np
import json
from core.models import *
from datetime import timedelta
import datetime
from django.db import connection
from django.db import models


# TODO: hacer esto una clase
# TODO: hacer los try catch de conexion a base de datos

def getModelVerbosename():
    return [name.verbose_name for name in fecha._meta.get_fields()[0:4] if hasattr(name, 'verbose_name')] + [
        name.verbose_name for name in prueba._meta.get_fields()[3:5] if hasattr(name, 'verbose_name')] + [
               name.verbose_name for name in curso._meta.get_fields()[2:] if hasattr(name, 'verbose_name')]


def getSedes():
    return [i.toJSON() for i in sede.objects.all()]


def getFechaData():
    try:
        data = getSedeName()
    except Exception as e:
        print(str(e))
    return data


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def getSedeName():
    with connection.cursor() as cursor:
        cursor.execute("""
     SELECT core_fecha.id, core_fecha.fecha_disponible,core_sede.ubicacion,core_prueba.tipo_prueba, core_prueba.tipo_licencia,core_curso.nomb_curso, core_curso.tipo_curso, core_curso.desc_curso
        FROM core_sede
        LEFT JOIN core_fecha
        ON  core_fecha.id_sede_id = core_sede.id
        LEFT JOIN core_prueba
        ON  core_prueba.id = core_fecha.id_prueba_id
        INNER JOIN core_curso
        ON core_curso.id = core_prueba.id_curso_id


""")
        row = dictfetchall(cursor)
    return row

# SELECT core_fecha.id, core_fecha.fecha_disponible,core_sede.ubicacion,core_prueba.tipo_prueba, core_prueba.tipo_licencia,core_curso.nomb_curso, core_curso.tipo_curso, core_curso.desc_curso
# FROM core_sede
# LEFT JOIN core_fecha
# ON  core_fecha.id_sede_id = core_sede.id
# LEFT JOIN core_prueba
# ON  core_prueba.id = core_fecha.id_prueba_id
# INNER JOIN core_curso
# ON core_curso.id = core_prueba.id_curso_id
#
