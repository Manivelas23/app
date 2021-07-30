from django.core.serializers import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, CreateView
from core.models import prueba, curso
from .forms import PruebaForm, CursoForm
from django.db import models


class PruebaTemplateView(ListView):
    model = prueba
    template_name = 'prueba/prueba.html'
    context_object_name = 'pruebas'
    form_class = PruebaForm, CursoForm
    obj_prueba = prueba()

    simple_field_names = [field.name for field in prueba._meta.get_fields() if not isinstance(field, (models.ForeignKey, models.ManyToOneRel, models.ManyToManyRel))]
    simple_field_names += [field.name for field in curso._meta.get_fields() if not isinstance(field, (models.ForeignKey, models.ManyToOneRel, models.ManyToManyRel))]
    simple_field_names.pop(3)



    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        curso_guardado = False
        try:
            if request.POST['accion'] == 'obtener_pruebas':
                data = []
                for i in prueba.objects.all():
                    for j in curso.objects.all():
                        prueba_dict = i.toJSON()
                        prueba_dict.update(j.toJSON())
                        prueba_dict.pop('id_curso')
                        data.append(prueba_dict)

            # TODO: Probar si valida si no se agrega un curso pero si una prueba
            if request.POST['accion'] == 'agregar':
                obj_curso = curso()
                obj_prueba = prueba()

                if request.POST['nomb_curso'] != '' and request.POST['tipo_curso'] != '':
                    obj_curso.nomb_curso = str(request.POST['nomb_curso']).upper()
                    obj_curso.tipo_curso = str(request.POST['tipo_curso']).upper()
                    obj_curso.desc_curso = str(request.POST['desc_curso']).upper()
                    obj_curso.save()
                    curso_guardado = True

                if curso_guardado:
                    obj_prueba.tipo_prueba = str(request.POST['tipo_prueba']).upper()
                    obj_prueba.tipo_licencia = str(request.POST['tipo_licencia']).upper()
                    obj_prueba.id_curso = obj_curso
                    obj_prueba.save()
                else:
                    obj_prueba.tipo_prueba = str(request.POST['tipo_prueba']).upper()
                    obj_prueba.tipo_licencia = str(request.POST['tipo_licencia']).upper()
                    obj_prueba.save()

            # TODO: Modificar el update para que sirva
            if request.POST['accion'] == 'editar':
                obj_prueba = prueba.objects.get(pk=request.POST['id'])
                obj_prueba.tipo_prueba = str(request.POST['tipo_prueba']).upper()
                obj_prueba.curso = str(request.POST['curso']).upper()
                obj_prueba.tipo_licencia = str(request.POST['tipo_licencia']).upper()
                obj_prueba.save()

            if request.POST['accion'] == 'eliminar':
                obj_prueba = prueba.objects.get(pk=request.POST['id'])
                obj_prueba.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)



    def get_context_data(self, *, object_list=None, **kwargs):
        print(self.simple_field_names)
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Pruebas'
        context['page_info'] = 'Pruebas'
        context['agregar_title'] = "Agregar una Prueba"
        context['table_content'] = self.simple_field_names
        context['form'] = [PruebaForm(), CursoForm()]
        return context
