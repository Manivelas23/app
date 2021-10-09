from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from .forms import *
import re
from core.models import *
from .extra import *
from .bot_fechas import GeneradorCitas
from ..mixins import IsSuperUserMixin
from ..pruebas.extra import get_pruebas


class MostrarCalendarioView(TemplateView):
    model = Fecha
    template_name = 'fechas/calendar_prueba.html'
    context_object_name = 'fechas'
    extra = Extra()

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:

            if request.POST['accion'] == 'filtrar_fechas':
                sedes_post = tuple(map(int, re.findall('[0-9]+', request.POST['sedes'])))

                obj_filtro = {
                    'id_prueba': int(request.POST['select_prueba']),
                    'sedes': sedes_post
                }

                data = self.extra.get_fechas_filtradas(obj_filtro)

            if request.POST['accion'] == 'cargar_fechas':
                data = self.extra.get_fechas()

            if request.POST['accion'] == 'cargar_pruebas':
                data = get_pruebas()

            if request.POST['accion'] == 'cargar_sedes':
                data = [i.toJSON() for i in sede.objects.all()]

            if request.POST['accion'] == 'eliminar':
                fecha = Fecha.objects.get(pk=request.POST['id_evento'])
                fecha.delete()

        except Exception as e:
            data['error'] = str(e)
            print(data['error'])
        return JsonResponse(data, safe=False)

        def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            context['page_title'] = 'Listado Fechas'
            context['page_info'] = 'Fechas Disponibles'
            context['table_content'] = self.extra.get_table_header_names()
            context['agregar_title'] = "Agregar una Nueva Fecha"
            return context


class CreateFechaListView(LoginRequiredMixin, TemplateView):
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
            print(data['error'])
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Fechas'
        context['page_info'] = 'Fechas Disponibles'
        context['agregar_title'] = "Agregar una Nueva Fecha"
        context['form'] = FechaForm()
        return context
