from core.models import *
from django.db import connection


class Extra:

    # Table Headers Names
    def get_table_header_names(self):
        return [name.verbose_name for name in Fecha._meta.get_fields()[0:4] if hasattr(name, 'verbose_name')] + [
            name.verbose_name for name in prueba._meta.get_fields()[3:5] if hasattr(name, 'verbose_name')] + [
                   name.verbose_name for name in curso._meta.get_fields()[2:] if hasattr(name, 'verbose_name')]

    # SQL
    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def sql_query_execution(self):
        data = None
        try:
            sql_query = """
                                  SELECT core_fecha.id, 
                                      core_fecha.fecha_disponible as start,
                                      core_fecha.fecha_fin as end,
                                      core_sede.ubicacion as UBICACION,
                                      core_prueba.tipo_prueba as title, 
                                      core_prueba.tipo_licencia as LICENCIA,
                                      core_curso.nomb_curso AS CURSO, 
                                      core_curso.tipo_curso AS TIPO , 
                                      core_curso.desc_curso AS DESCRIPCION
                                         FROM core_sede
                                         LEFT JOIN core_fecha
                                         ON  core_fecha.id_sede_id = core_sede.id
                                         LEFT JOIN core_prueba
                                         ON  core_prueba.id = core_fecha.id_prueba_id
                                         INNER JOIN core_curso
                                         ON core_curso.id = core_prueba.id_curso_id
                                         """
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                row = self.dictfetchall(cursor)
                data = row
        except Exception as e:
            data['error'] = str(e)
        return data

    def get_fechas(self, request):
        data = None
        try:
            row = self.sql_query_execution()

            #
            # inicio_entradas, limite_entradas = int(request['inicio']), int(request['limite'])
            #
            # fechas_paginadas = [valor for indice, valor in
            #                     enumerate(row[inicio_entradas:inicio_entradas + limite_entradas],
            #                               inicio_entradas)]
            #
            # data = {
            #     'fechas': fechas_paginadas,
            #     'length': len(row)
            # }

            data = {
                'fechas': row,
                'length': len(row)
            }

        except Exception as e:
            data['error'] = str(e)
        return data
