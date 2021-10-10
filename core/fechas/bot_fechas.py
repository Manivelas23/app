from datetime import timedelta
import datetime
from dateutil.easter import *
import numpy as np
import re
from django.utils.timezone import make_aware
from core.models import prueba, sede, Fecha


class GeneradorCitas:
    def __init__(self, data):
        try:
            data = data.dict()

            fecha_inicio_citas = datetime.datetime.strptime(data['fecha_inicio'], '%Y/%m/%d %H:%M')
            fecha_fin_citas = datetime.datetime.strptime(data['fecha_fin'], '%Y/%m/%d %H:%M')

            self.fecha_inicio = datetime.datetime(fecha_inicio_citas.year,
                                                  fecha_inicio_citas.month,
                                                  fecha_inicio_citas.day,
                                                  fecha_inicio_citas.hour,
                                                  fecha_inicio_citas.minute)

            self.fecha_fin = datetime.datetime(fecha_fin_citas.year,
                                               fecha_fin_citas.month,
                                               fecha_fin_citas.day,
                                               fecha_fin_citas.hour,
                                               fecha_fin_citas.minute)

            self.id_prueba = data['select_prueba']

            self.sedes = re.findall('[0-9]+', data['sedes'])

            self.feriados = [datetime.date(i[2], i[0], i[1]) for i in
                             [(1, 1, 2021),
                              (4, 11, 2021),
                              (5, 1, 2021),
                              (7, 26, 2021),
                              (8, 2, 2021),
                              (8, 15, 2021),
                              (9, 15, 2021),
                              (12, 25, 2021),
                              (12, 2, 2021)]]

        except Exception as e:
            print("err", str(e))

    def get_semana_santa(self):
        domingo_resurreccion = easter(2021)
        return [domingo_resurreccion - timedelta(days=i) for i in range(0, 8)]

    def citas_dias_laborales(self, finesSemana=(6, 7)):
        feriados = self.feriados + self.get_semana_santa()
        fechas = []

        try:
            while self.fecha_inicio.date() <= self.fecha_fin.date():

                if self.fecha_inicio.isoweekday() not in finesSemana:

                    for i in range(7, 15):
                        hours_added = datetime.timedelta(hours=1)
                        feriados = np.unique(
                            np.array([datetime.datetime.combine(j, self.fecha_inicio.time()) for j in feriados]))

                        if self.fecha_inicio not in feriados:
                            if self.fecha_inicio.hour == 14: hours_added = datetime.timedelta(hours=-7)
                            self.fecha_inicio = self.fecha_inicio + hours_added

                            if self.fecha_inicio.hour != 12: fechas.append(self.fecha_inicio)

                self.fecha_inicio += timedelta(days=1)
        except Exception as e:
            print("err", str(e))
        return fechas

    def generar_citas(self):
        citas_dict_list = []
        id_prueba = self.id_prueba
        fechas = self.citas_dias_laborales()
        for sede in self.sedes:
            for fecha in fechas:
                fecha_cita = {
                    "fecha_disponible": fecha,
                    "fecha_fin": fecha +timedelta(hours=1),
                    "id_sede": sede,
                    "id_prueba": id_prueba
                }
                citas_dict_list.append(fecha_cita)
        return citas_dict_list

    def guardar_citas(self):
        data = {}
        try:
            for fecha_cita in self.generar_citas():
                fecha = Fecha()
                fecha_naive = fecha_cita['fecha_disponible']
                fecha.fecha_disponible = make_aware(fecha_naive)
                fecha.fecha_fin = fecha_cita['fecha_fin']
                fecha.id_prueba = prueba.objects.get(pk=int(fecha_cita['id_prueba']))
                fecha.id_sede = sede.objects.get(pk=int(fecha_cita['id_sede']))
                fecha.save()
        except Exception as e:
            data['error'] = str(e)
            print("err", str(e))
        return data
