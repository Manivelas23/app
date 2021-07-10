import listview as listview
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .forms import SedeForm


from core.models import sede


class SedeListView(ListView):
    model = sede
    template_name = 'sedes/list.html'
    context_object_name = 'sedes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['saludo'] = 'Listado de Sedes'
        return context
#
class SedeCreateView(CreateView):
    model = sede
    template_name = 'sedes/create.html'
    form_class = SedeForm
    success_url = reverse_lazy('sede_list_view')
