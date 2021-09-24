from core.models import *
from django.db import connection


class Extra:
    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    # fechas
    def getFechaData(self):
        try:
            data = self.queryDataFecha()
        except Exception as e:
            print(str(e))
        return data

    def queryDataFecha(self):
        try:
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
                row = self.dictfetchall(cursor)
        except Exception as e:
            print(str(e))
        return row

    # citas
    def get_cita_data(self):
        try:
            data = self.queryDataCita()
        except Exception as e:
            print(str(e))
        return data

    def get_cita_data_by_id(self, __pk):
        try:
            data = self.queryDataCitaById(__pk)
        except Exception as e:
            print(str(e))
        return data

    def queryDataCita(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                      select core_cita.id,
               core_fecha.fecha_disponible,
               core_sede.ubicacion,
               core_persona.numero_identificacion,
               core_prueba.tipo_prueba,
               core_prueba.tipo_licencia,
               core_curso.tipo_curso,
               core_curso.nomb_curso,
               core_curso.desc_curso
        
        from core_cita
                 left join core_persona
                           on core_persona.numero_identificacion = core_cita.id_persona_id
                 inner join core_fecha on
            core_fecha.id = core_cita.id_fecha_cita_id
                 inner join core_sede
                            on core_sede.id = core_fecha.id_sede_id
                 inner join core_prueba
                            on core_prueba.id = core_fecha.id_prueba_id
                 inner join core_curso
                            on core_curso.id = core_prueba.id_curso_id
           """)
                row = self.dictfetchall(cursor)
        except Exception as e:
            print(str(e))
        return row

    def queryDataCitaById(self, __pk):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
        select core_cita.id,
               core_cita.otras_indicaciones,
               core_fecha.fecha_disponible,
               core_sede.ubicacion,
               core_persona.numero_identificacion,
               core_persona.nombre,
               core_persona.primer_apellido,
               core_persona.segundo_apellido,
               core_persona.tipo_identificacion_persona,
               core_prueba.tipo_prueba,
               core_prueba.tipo_licencia,
               core_curso.tipo_curso,
               core_curso.nomb_curso,
               core_curso.desc_curso

        from core_cita
                 left join core_persona
                           on core_persona.numero_identificacion = core_cita.id_persona_id
                 inner join core_fecha on
            core_fecha.id = core_cita.id_fecha_cita_id
                 inner join core_sede
                            on core_sede.id = core_fecha.id_sede_id
                 inner join core_prueba
                            on core_prueba.id = core_fecha.id_prueba_id
                 inner join core_curso
                            on core_curso.id = core_prueba.id_curso_id
        where core_cita.id = %s
           """, [__pk])
                row = self.dictfetchall(cursor)
        except Exception as e:
            print(str(e))
        return row
