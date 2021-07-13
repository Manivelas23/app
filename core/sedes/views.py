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


<<<<<<< Updated upstream
<<<<<<< Updated upstream
class SedeListView(ListView):
=======
=======
>>>>>>> Stashed changes
class SedeListView(TemplateView):
>>>>>>> Stashed changes
    model = sede
    template_name = 'sedes/list.html'
    context_object_name = 'sedes'

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
                obj_sede.ubicacion = request.POST['ubicacion']
                print(sede.ubicacion)
                obj_sede.save()

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Sedes'
        context['page_info'] = 'Sedes'
        return context

<<<<<<< Updated upstream
<<<<<<< Updated upstream

class SedeCreateView(CreateView):
    model = sede
    template_name = 'sedes/create.html'
    form_class = SedeForm
    success_url = reverse_lazy('sede_list_view')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = self.get_form()
            if form.is_valid():
                form.save()
            else:
                data = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Agregar Sede'
        context['page_info'] = 'Sedes'
        context['sede_list'] = self.success_url
        context['accion'] = 'agregar'
        return context
=======
=======
>>>>>>> Stashed changes
# Clasico - Sirve
# class SedeListView(ListView):
#     model = sede
#     template_name = 'sedes/list.html'
#     context_object_name = 'sedes'
#
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             data = []
#             for i in sede.objects.all():
#                 data.append(i.toJSON())
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_title'] = 'Listado Sedes'
#         context['page_info'] = 'Sedes'
#         context['modal_title'] = 'Formulario Crear Sede'
#         return context

# inventado para despues
# class SedeTemplateView(TemplateView):
#     model = sede
#     template_name = 'sedes/list.html'
#     context_object_name = 'sedes'
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#
#             #agregar datos a la sede
#             if action == 'agregar':
#                 form = self.get_form()
#                 if form.is_valid():
#                     form.save()
#                 else:
#                     data = form.errors
#
#             #buscar datos a la sede
#             elif action == 'buscar':
#                 data = []
#                 for i in sede.objects.all():
#                     data.append(i.toJSON())
#
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)

#
# class SedeCreateView(CreateView):
#     model = sede
#     template_name = 'sedes/create.htmls'
#     form_class = SedeForm
#     success_url = reverse_lazy('sede_list_view')
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             form = self.get_form()
#             if form.is_valid():
#                 form.save()
#             else:
#                 data = form.errors
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_title'] = 'Agregar Sede'
#         context['page_info'] = 'Sedes'
#         context['sede_list'] = self.success_url
#         context['accion'] = 'agregar'
#         return context
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
