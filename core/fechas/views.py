from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView
from .forms import FechaForm, PruebaForm
from core.models import fecha, sede, prueba,curso
from django.db import models
from .extra import *
from .bot_fechas import GeneradorCitas

class FechaListView(TemplateView):
    model = fecha
    template_name = 'fechas/create_fecha.html'
    context_object_name = 'fechas'
    form_class = FechaForm, PruebaForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['accion'] == 'agregar':
                generadorCitas = GeneradorCitas(request.POST)
                generadorCitas.citas_dias_laborales()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Fechas'
        context['page_info'] = 'Fechas Disponibles'
        context['sedes'] = sede.objects.all()
        context['table_content'] = get_model_verbosename
        context['agregar_title'] = "Agregar una Nueva Fecha"
        context['form'] = FechaForm()
        context['prueba_curso_data'] = get_table_data()
        return context
