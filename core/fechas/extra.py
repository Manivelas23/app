from core.models import *
from django.db import connection


class Extra:
    # SQL
    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def get_fechas_filtradas(self, obj_filtro):
        data = {}
        try:
            if len(obj_filtro['sedes']) > 1:
                sql_query = """
                SELECT core_fecha.id,
                   core_fecha.fecha_disponible as start,
                   core_fecha.fecha_fin        as  end,
                   core_sede.ubicacion         as UBICACION,
                   core_prueba.tipo_prueba     as title,
                   core_prueba.tipo_licencia   as LICENCIA,
                   core_curso.nomb_curso       AS CURSO,
                   core_curso.tipo_curso       AS TIPO,
                   core_curso.desc_curso       AS DESCRIPCION
                    FROM core_sede
                             LEFT JOIN core_fecha
                                ON core_fecha.id_sede_id = core_sede.id
                             LEFT JOIN core_prueba
                                ON core_prueba.id = core_fecha.id_prueba_id
                             INNER JOIN core_curso
                                ON core_curso.id = core_prueba.id_curso_id
                    where core_prueba.id = %s
                      and core_sede.id IN {}
                """.format(obj_filtro['sedes'])
            else:
                sql_query = """  
                              SELECT core_fecha.id,
                                 core_fecha.fecha_disponible as start,
                                 core_fecha.fecha_fin        as  end,
                                 core_sede.ubicacion         as UBICACION,
                                 core_prueba.tipo_prueba     as title,
                                 core_prueba.tipo_licencia   as LICENCIA,
                                 core_curso.nomb_curso       AS CURSO,
                                 core_curso.tipo_curso       AS TIPO,
                                 core_curso.desc_curso       AS DESCRIPCION
                                  FROM core_sede
                                           LEFT JOIN core_fecha
                                              ON core_fecha.id_sede_id = core_sede.id
                                           LEFT JOIN core_prueba
                                              ON core_prueba.id = core_fecha.id_prueba_id
                                           INNER JOIN core_curso
                                              ON core_curso.id = core_prueba.id_curso_id
                                  where core_prueba.id = %s
                                    and core_sede.id IN ({x})
                              """.format(x=obj_filtro['sedes'][0])
            with connection.cursor() as cursor:
                cursor.execute(sql_query, [obj_filtro['id_prueba']])
                row = self.dictfetchall(cursor)
                data = row
        except Exception as e:
            data['error'] = str(e)
        finally:
            cursor.close()
        return data
