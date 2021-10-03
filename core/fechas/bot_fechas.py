# -*- coding: utf-8 -*-
from datetime import timedelta
import datetime
from dateutil.easter import *
import numpy as np
from core.models import *
import re


class GeneradorCitas:
    def __init__(self, data):
        try:
            data = data.dict()

            fecha_inicio_parsed = datetime.datetime.strptime(data['fecha_inicio'], '%Y/%m/%d %H:%M')
            fecha_fin_parsed = datetime.datetime.strptime(data['fecha_fin'], '%Y/%m/%d %H:%M')

            self.fecha_inicio = datetime.datetime(fecha_inicio_parsed.year,
                                                  fecha_inicio_parsed.month,
                                                  fecha_inicio_parsed.day,
                                                  fecha_inicio_parsed.hour,
                                                  fecha_inicio_parsed.minute)

            self.fecha_fin = datetime.datetime(fecha_fin_parsed.year,
                                               fecha_fin_parsed.month,
                                               fecha_fin_parsed.day,
                                               fecha_fin_parsed.hour,
                                               fecha_fin_parsed.minute)

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
            print(str(e))

    def calcular_semana_santa(self):
        feriados_semana_santa = []
        domingo_resurr = easter(2021)
        dia_semana_santa = domingo_resurr
        for i in range(0, 7):
            dia_semana_santa = dia_semana_santa - timedelta(days=1)
            feriados_semana_santa.append(dia_semana_santa)
        return feriados_semana_santa

    def citas_dias_laborales(self, finesSemana=(6, 7)):
        feriados = self.feriados + self.calcular_semana_santa()
        fechas = []
        fechaInicio = self.fecha_inicio
        fechaFin = self.fecha_fin
        try:
            while fechaInicio.date() <= fechaFin.date():
                if fechaInicio.isoweekday() not in finesSemana:
                    for i in range(7, 15):
                        hours_added = datetime.timedelta(hours=1)
                        feriados = np.unique(
                            np.array([datetime.datetime.combine(j, fechaInicio.time()) for j in feriados]))
                        if fechaInicio not in feriados:
                            if fechaInicio.hour == 14: hours_added = datetime.timedelta(hours=-7)
                            fechaInicio = fechaInicio + hours_added
                            if fechaInicio.hour != 12: fechas.append(fechaInicio)
                fechaInicio += timedelta(days=1)
        except Exception as e:
            print(str(e))
        return fechas

    def generar_citas(self):
        citas_dict_list = []
        id_prueba = self.id_prueba
        fechas = self.citas_dias_laborales()
        for sede in self.sedes:
            for fecha in fechas:
                fecha_cita = {
                    "fecha_disponible": fecha,
                    "id_sede": sede,
                    "id_prueba": id_prueba
                }
                citas_dict_list.append(fecha_cita)
        return citas_dict_list
