from django.core.serializers import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, CreateView
from core.models import prueba, curso
from .forms import PruebaForm, CursoForm
from django.db import models, transaction


class PruebaTemplateView(ListView):
    model = prueba
    template_name = 'prueba/prueba.html'
    context_object_name = 'pruebas'
    form_class = PruebaForm, CursoForm
    obj_prueba = prueba()

    # CLASS METHODS
    def get_model_names(self):
        simple_field_names = [field.name for field in prueba._meta.get_fields() if
                              not isinstance(field, (models.ForeignKey, models.ManyToOneRel, models.ManyToManyRel))]
        simple_field_names += [field.name for field in curso._meta.get_fields() if
                               not isinstance(field, (models.ForeignKey, models.ManyToOneRel, models.ManyToManyRel))]
        simple_field_names.pop(3)
        return simple_field_names

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['accion'] == 'obtener_pruebas':
                data = []
                lista_pruebas = [i.toJSON() for i in prueba.objects.all()]
                lista_cursos = [i.toJSON() for i in curso.objects.all()]
                lista_curso_pruebas = list(zip(lista_pruebas,lista_cursos))
                x = {}
                for i,j in lista_curso_pruebas:
                    print("i: "+ str(i))
                    print("j: "+ str(j))
                    x = i
                    j['id_curso'] = j.pop('id')
                    x.update(j)

                    print("x:" + str(x))
                    data.append(x)

            if request.POST['accion'] == 'agregar':
                obj_curso = curso()
                obj_prueba = prueba()

                obj_curso.nomb_curso = str(request.POST['nomb_curso']).upper()
                obj_curso.tipo_curso = str(request.POST['tipo_curso']).upper()
                obj_curso.desc_curso = str(request.POST['desc_curso']).upper()

                obj_prueba.tipo_prueba = str(request.POST['tipo_prueba']).upper()
                obj_prueba.tipo_licencia = str(request.POST['tipo_licencia']).upper()
                obj_prueba.id_curso = obj_curso

                obj_curso.save()
                obj_prueba.save()

            if request.POST['accion'] == 'editar':

                with transaction.atomic():
                    obj_curso = curso.objects.get(pk=request.POST['id_curso'])
                    obj_curso.nomb_curso = str(request.POST['nomb_curso']).upper()
                    obj_curso.tipo_curso = str(request.POST['tipo_curso']).upper()
                    obj_curso.desc_curso = str(request.POST['desc_curso']).upper()
                    obj_curso.save()

                    obj_prueba = prueba.objects.get(pk=request.POST['id'])
                    obj_prueba.tipo_prueba = str(request.POST['tipo_prueba']).upper()
                    obj_prueba.tipo_licencia = str(request.POST['tipo_licencia']).upper()
                    obj_prueba.save()

            if request.POST['accion'] == 'eliminar':
                obj_prueba = prueba.objects.get(pk=request.POST['id'])
                obj_curso = curso.objects.get(pk=request.POST['id_curso'])
                obj_prueba.delete()
                obj_curso.delete()

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Pruebas'
        context['page_info'] = 'Pruebas'
        context['agregar_title'] = "Agregar una Prueba"
        context['table_content'] = self.get_model_names()
        context['form'] = [PruebaForm(), CursoForm()]
        return context
