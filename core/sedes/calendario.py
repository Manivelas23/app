# -*- coding: utf-8 -*-
import datetime
from datetime import timedelta
from dateutil.easter import *

fecha_inicio = datetime.datetime(2021, 1, 1, 6, 0)
fecha_fin = datetime.datetime(2021, 12, 30, 15, 0)

sedes = [
    "Central",
    "Alajuela",
    "Cartago",
    "Guápiles",
    "Heredia",
    "Liberia",
    "Limón",
    "Nicoya",
    "Peréz Zeledón",
    "Puntarenas",
    "Río Claro",
    "San Carlos",
    "San Ramón"]

# feriados del año 2021
feriados = [
    (1, 1, 2021),
    (4, 11, 2021),
    (5, 1, 2021),
    (7, 26, 2021),
    (8, 2, 2021),
    (8, 15, 2021),
    (9, 15, 2021),
    (12, 25, 2021),
    (12, 2, 2021), ]

# parseando los feriados a formato "date"
feriados = [datetime.date(i[2], i[0], i[1]) for i in feriados]


# funcion para calcular la semana santa de cada año
def calcular_semana_santa(year):
    # tomando la fecha exacta de el domingo de resurrección de un año determinado
    domingo_resurr = easter(year)
    dia_semana_santa = domingo_resurr

    # restando desde el domingo de resurreccion al primer lunes de semana santa y agregando esos dias a la lista feriados
    for i in range(0, 7):
        dia_semana_santa = timedelta(days=-1)
        feriados.append(dia_semana_santa)


calcular_semana_santa(2021)


# obteniendo los dias laborales de cada mes y retornando una lista con los mismos
def citas_dias_laborales(fechaInicio, fechaFin, finesSemana=(6, 7)):
    dias = []
    while fechaInicio.date() <= fechaFin.date():
        if fechaInicio.isoweekday() not in finesSemana:
            for i in range(7, 15):

                hours_added = datetime.timedelta(hours=1)

                if fechaInicio.hour == 14: hours_added = datetime.timedelta(hours=-7)
                fechaInicio = fechaInicio + hours_added

                if fechaInicio.hour != 12: dias.append(fechaInicio)

        fechaInicio += timedelta(days=1)

    return dias


citas = citas_dias_laborales(fecha_inicio, fecha_fin)


# funcion que elimina los dias feriados de las fechas de las citas
def limpiar_citas(citas, feriados):
    for feriado in feriados[:]:
        for cita in citas[:]:
            if cita.date() == feriado: citas.remove(cita)
    return citas


citas_disponibles = limpiar_citas(citas, feriados)

# asignando cada cita a una sucursal
dict_cita_sede = {}
for sede in sedes: dict_cita_sede[sede] = {"citas_disponibles": citas_disponibles}

print(dict_cita_sede['Central'])