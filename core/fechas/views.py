from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.timezone import make_aware
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView
from .forms import FechaForm, PruebaForm
from core.models import *
from django.db import models
from .extra import *
from .bot_fechas import GeneradorCitas
from ..pruebas.extra import getPruebaData


class FechasListView(TemplateView):
    model = fecha
    template_name = 'fechas/fecha.html'
    context_object_name = 'fechas'
    obj_extra = Extra()
    success_url = '/fechas/'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['accion'] == 'obtener_fechas':
                data = self.obj_extra.getFechaData()

            if request.POST['accion'] == 'eliminar':
                obj_fecha = fecha.objects.get(pk=request.POST['id'])
                obj_fecha.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Fechas'
        context['page_info'] = 'Fechas Disponibles'
        context['table_content'] =self.obj_extra.getModelVerbosename()
        context['agregar_title'] = "Agregar una Nueva Fecha"
        context['form'] = FechaForm()
        return context


class CreateFechaListView(TemplateView):
    model = fecha
    template_name = 'fechas/create_fecha.html'
    context_object_name = 'fechas'
    form_class = FechaForm, PruebaForm
    success_url = reverse_lazy('core:FechaTemplateView')
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
                    obj_fecha = fecha()
                    fecha_naive = fecha_cita['fecha_disponible']
                    obj_fecha.fecha_disponible = make_aware(fecha_naive)
                    obj_fecha.id_prueba = prueba.objects.get(pk=int(fecha_cita['id_prueba']))
                    obj_fecha.id_sede = sede.objects.get(pk=int(fecha_cita['id_sede']))
                    obj_fecha.save()


            if request.POST['accion'] == 'cargar_pruebas':
                data = getPruebaData()

            if request.POST['accion'] == 'cargar_sedes':
                data = self.obj_extra.getSedes()
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
