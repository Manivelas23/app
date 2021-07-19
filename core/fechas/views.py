import listview as listview
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, CreateView
from .forms import FechaForm
from core.models import fecha
from core.models import sede
from django.db import models

class FechaListView(ListView):
    model = fecha
    template_name = 'fechas/fecha_list.html'
    context_object_name = 'fechas'
    form_class = FechaForm

    simple_field_names = [field.name for field in fecha._meta.get_fields()
                          if not isinstance(field, (models.ManyToOneRel, models.ManyToManyRel))]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = []
            for i in fecha.objects.all():
                data.append(i)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Fechas'
        context['page_info'] = 'Fechas Disponibles'
        context['sedes'] = sede.objects.all()
        context['table_content'] = self.simple_field_names
        context['agregar_title'] = "Agregar una Nueva Fecha"
        return context
