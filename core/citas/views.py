from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from core.models import cita
from django.views.generic import *
from .forms import *
from .extra import Extra
from django.http import JsonResponse
from core.pruebas.extra import get_pruebas


class CrearCitaView(TemplateView):
    model = cita
    template_name = 'citas/crear_cita.html'
    context_object_name = 'citas'
    obj_extra = Extra()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['accion'] == 'obtener_citas':
                data = self.obj_extra.queryDataCita()
                print(data)

            if request.POST['accion'] == 'agregar':
                obj_cita = cita()

                obj_persona = persona.objects.filter(pk=request.POST['id_persona'])
                obj_cita.id_persona = obj_persona[0]

                obj_fecha = fecha.objects.filter(pk=request.POST['select_fecha_cita'])
                obj_cita.id_fecha_cita = obj_fecha[0]

                obj_cita.otras_indicaciones = request.POST['otras_indicaciones']
                obj_cita.save()

            if request.POST['accion'] == 'cargar-fechas-select':
                data = self.obj_extra.getFechaData()

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Crear Cita'
        context['page_info'] = 'Citas'
        context['form_cita'] = CitaForm
        return context


class ListCitasView(TemplateView):
    model = cita
    template_name = 'citas/list_citas.html'
    context_object_name = 'citas'
    obj_extra = Extra()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['accion'] == 'obtener_citas':
                data = self.obj_extra.queryDataCita()

            if request.POST['accion'] == 'eliminar':
                obj_cita = cita.objects.get(pk=request.POST['id'])
                obj_cita.delete()


        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Citas'
        context['page_info'] = 'Citas'
        context['agregar_title'] = "Agregar una Cita"
        context['table_content'] = ['id', 'Fecha', 'Persona', 'Tipo Prueba', 'Tipo Licencia', 'Tipo Curso', 'Curso']
        return context


class DetalleCitaView(DetailView):
    model = cita
    template_name = 'citas/imprimir_cita.html'
    obj_extra = Extra()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detalles_cita'] = self.obj_extra.get_cita_data_by_id(self.kwargs['pk'])
        return context
