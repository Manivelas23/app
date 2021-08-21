import listview as listview
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, CreateView
from .forms import SedeForm
from core.models import sede
from django.db import models


class SedeListView(TemplateView):
    model = sede
    template_name = 'sedes/sede.html'
    context_object_name = 'sedes'
    form_class = SedeForm

    simple_field_names = [field.name for field in sede._meta.get_fields()
                          if not isinstance(field, (models.ForeignKey, models.ManyToOneRel, models.ManyToManyRel))]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['accion'] == 'obtener_sedes':
                data = []
                for i in sede.objects.all():
                    data.append(i.toJSON())

            if request.POST['accion'] == 'agregar':
                obj_sede = sede()
                obj_sede.ubicacion = str(request.POST['ubicacion']).title()
                obj_sede.cant_supervisores = request.POST['cant_supervisores']
                obj_sede.cant_computadoras = request.POST['cant_computadoras']
                obj_sede.activo = request.POST['activo']
                obj_sede.save()

            if request.POST['accion'] == 'editar':
                obj_sede = sede.objects.get(pk=request.POST['id'])
                obj_sede.ubicacion = str(request.POST['ubicacion']).title()
                obj_sede.cant_supervisores = request.POST['cant_supervisores']
                obj_sede.cant_computadoras = request.POST['cant_computadoras']
                obj_sede.activo = request.POST['activo']
                obj_sede.save()

            if request.POST['accion'] == 'eliminar':
                obj_sede = sede.objects.get(pk=request.POST['id'])
                obj_sede.delete()

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Sedes'
        context['page_info'] = 'Sedes'
        context['form'] = SedeForm()
        context['table_content'] = self.simple_field_names
        context['agregar_title'] = "Agregar una Nueva Sede"
        return context
