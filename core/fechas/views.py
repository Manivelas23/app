import time
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.timezone import make_aware
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from .forms import *
from core.models import *
from django.db import models
import numpy as np
from .extra import *
from .bot_fechas import GeneradorCitas
from ..pruebas.extra import get_pruebas


class FechasListView(TemplateView):
    model = Fecha
    template_name = 'fechas/fecha.html'
    context_object_name = 'fechas'
    extra = Extra()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}

        try:
            if request.POST['accion'] == 'obtener_fechas':
                fechas_queryset = self.extra.get_fechas()

                inicio_entradas = int(request.POST['inicio'])
                limite_entradas = int(request.POST['limite'])

                print(inicio_entradas, limite_entradas)

                fechas_paginadas = [valor for indice, valor in
                                    enumerate(fechas_queryset[inicio_entradas:inicio_entradas + limite_entradas],
                                              inicio_entradas)]

                data = {
                    'fechas': fechas_paginadas,
                    'length': len(fechas_queryset)
                }
                # **********

                if request.POST['accion'] == 'eliminar':
                    fecha = Fecha.objects.get(pk=request.POST['id'])
                fecha.delete()
                # **********

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Fechas'
        context['page_info'] = 'Fechas Disponibles'
        context['table_content'] = self.extra.get_table_header_names()
        context['agregar_title'] = "Agregar una Nueva Fecha"
        context['form'] = FechaForm()
        return context


class CreateFechaListView(TemplateView):
    model = Fecha
    template_name = 'fechas/create_fecha.html'
    context_object_name = 'fechas'
    form_class = FechaForm, PruebaForm
    obj_extra = Extra()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['accion'] == 'agregar':
                generadorCitas = GeneradorCitas(request.POST)
                for fecha_cita in generadorCitas.generar_citas():
                    fecha = Fecha()
                    fecha_naive = fecha_cita['fecha_disponible']
                    fecha.fecha_disponible = make_aware(fecha_naive)
                    fecha.id_prueba = prueba.objects.get(pk=int(fecha_cita['id_prueba']))
                    fecha.id_sede = sede.objects.get(pk=int(fecha_cita['id_sede']))
                    fecha.save()

            if request.POST['accion'] == 'cargar_pruebas':
                data = get_pruebas()

            if request.POST['accion'] == 'cargar_sedes':
                data = [i.toJSON() for i in sede.objects.all()]

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Fechas'
        context['page_info'] = 'Fechas Disponibles'
        context['agregar_title'] = "Agregar una Nueva Fecha"
        context['form'] = FechaForm()
        return context
