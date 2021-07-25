from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, CreateView
from core.models import prueba
from .forms import PruebaForm
from django.db import models


class PruebaTemplateView(ListView):
    model = prueba
    template_name = 'prueba/prueba.html'
    context_object_name = 'pruebas'
    form_class = PruebaForm
    obj_prueba = prueba()

    simple_field_names = [field.name for field in prueba._meta.get_fields()
                          if not isinstance(field, (models.ForeignKey, models.ManyToOneRel, models.ManyToManyRel))]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['accion'] == 'obtener_pruebas':
                data = []
                for i in prueba.objects.all():
                    data.append(i.toJSON())

            if request.POST['accion'] == 'agregar':
                obj_prueba = prueba()
                obj_prueba.tipo_prueba = str(request.POST['tipo_prueba']).upper()
                obj_prueba.tipo_licencia = str(request.POST['tipo_licencia']).upper()
                obj_prueba.save()

            if request.POST['accion'] == 'editar':
                obj_prueba = prueba.objects.get(pk=request.POST['id'])
                obj_prueba.tipo_prueba = str(request.POST['tipo_prueba']).upper()
                obj_prueba.tipo_licencia = str(request.POST['tipo_licencia']).upper()
                obj_prueba.save()

            if request.POST['accion'] == 'eliminar':
                obj_prueba = prueba.objects.get(pk=request.POST['id'])
                obj_prueba.delete()
                
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Pruebas'
        context['page_info'] = 'Pruebas'
        context['agregar_title'] = "Agregar una Prueba"
        context['table_content'] = self.simple_field_names
        context['form'] = PruebaForm()
        return context
