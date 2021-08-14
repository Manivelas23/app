# -*- coding: utf-8 -*-
from datetime import timedelta
import datetime
from dateutil.easter import *
from core.models import *
import re


class GeneradorCitas:
    def __init__(self, data):
        try:
            data = data.dict()

            self.lista_citas = []

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
        domingo_resurr = easter(2021)
        dia_semana_santa = domingo_resurr
        for i in range(0, 7):
            dia_semana_santa = dia_semana_santa - timedelta(days=1)
            self.feriados.append(dia_semana_santa)

    def citas_dias_laborales(self, finesSemana=(6, 7)):
        self.calcular_semana_santa()
        dias = []
        while self.fecha_inicio.date() <= self.fecha_fin.date():
            if self.fecha_inicio.isoweekday() not in finesSemana:
                for i in range(7, 15):
                    hours_added = datetime.timedelta(hours=1)
                    if self.fecha_inicio.date() not in self.feriados:
                        if self.fecha_inicio.hour == 14: hours_added = datetime.timedelta(hours=-7)
                        self.fecha_inicio = self.fecha_inicio + hours_added
                        if self.fecha_inicio.hour != 12: dias.append(self.fecha_inicio)
                self.fecha_inicio += timedelta(days=1)
        print("feriados", self.feriados)
        print("dias", dias)
        return dias
