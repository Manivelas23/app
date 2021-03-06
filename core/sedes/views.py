from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from .forms import SedeForm
from .extra import *
from core.models import sede


class SedeListView(ListView):
    model = sede
    template_name = 'sedes/sede.html'
    context_object_name = 'sedes'
    form_class = SedeForm

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['accion'] == 'obtener_sedes':
                data = [i.toJSON() for i in sede.objects.all()]

            if request.POST['accion'] == 'agregar':
                obj_sede = sede(
                    ubicacion=str(request.POST['ubicacion']).title(),
                    cant_supervisores=int(request.POST['cant_supervisores']),
                    cant_computadoras=int(request.POST['cant_computadoras']),
                    activo=request.POST['activo']
                )
                obj_sede.save()
                data['redirect'] = False

            if request.POST['accion'] == 'editar':
                obj_sede = sede.objects.get(pk=request.POST['id'])
                obj_sede.ubicacion = str(request.POST['ubicacion']).title()
                obj_sede.cant_supervisores = request.POST['cant_supervisores']
                obj_sede.cant_computadoras = request.POST['cant_computadoras']
                obj_sede.activo = request.POST['activo']
                obj_sede.save()
                data['redirect'] = False

            if request.POST['accion'] == 'eliminar':
                obj_sede = sede.objects.get(pk=request.POST['id'])
                obj_sede.delete()
                data['redirect'] = False


        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Sedes'
        context['page_info'] = 'Sedes'
        context['form'] = SedeForm()
        context['table_content'] = getModelVerbosename()
        context['agregar_title'] = "Agregar una Nueva Sede"
        return context
