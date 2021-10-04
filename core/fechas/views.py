import time

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from .forms import *
from core.models import *
from django.db import models
import numpy as np
from .extra import *
from .bot_fechas import GeneradorCitas
from ..pruebas.extra import get_pruebas


class FechasListView(ListView):
    model = Fecha
    template_name = 'fechas/fecha.html'
    context_object_name = 'fechas'
    extra = Extra()

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}

        try:
            if request.POST['accion'] == 'obtener_fechas':
                data = self.extra.get_fechas(request.POST)
                # **********

            if request.POST['accion'] == 'eliminar':
                fecha = Fecha.objects.get(pk=request.POST['id'])
                fecha.delete()
                data['redirect'] = False
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
    generador_citas = GeneradorCitas
    success_url = reverse_lazy('FechaTemplateView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['accion'] == 'agregar':
                self.generador_citas(request.POST).guardar_citas()
                data['redirect'] = True
                data['redirect_url'] = self.success_url

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
