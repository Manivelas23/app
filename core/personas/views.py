from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from core.models import persona
from django.views.generic import *
from .forms import *


class ListPersonasView(ListView):
    model = persona
    template_name = 'persona/list_personas.html'
    context_object_name = 'personas'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Listado Personas'
        context['page_info'] = 'Personas'
        return context


class CrearPersonaView(CreateView):
    model = persona
    form_class = PersonaForm
    template_name = 'persona/crear_persona.html'
    success_url = reverse_lazy('ListPersonasView')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Formulario Personas'
        context['page_info'] = 'Personas'
        return context


class EditarPersonaView(UpdateView):
    model = persona
    form_class = PersonaForm
    template_name = 'persona/editar_persona.html'
    success_url = reverse_lazy("ListPersonasView")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Editar Persona'
        context['page_info'] = 'Personas'
        return context

class EliminarPersonaView(DeleteView):
    model = persona
    template_name = 'persona/eliminar_persona.html'
    success_url = reverse_lazy("ListPersonasView")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Eliminar Persona'
        context['page_info'] = 'Personas'
        return context
