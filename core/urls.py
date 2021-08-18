from django.urls import path
from core.sedes.views import *
from core.fechas.views import *
from core.pruebas.views import *

urlpatterns = [
    path('', SedeListView.as_view(), name='SedeTemplateView'),
    path('generarfechas/', CreateFechaListView.as_view(), name='CreateFechaTemplateView'),
    path('fechas/', FechasListView.as_view(), name='FechaTemplateView'),
    path('pruebas/', PruebaTemplateView.as_view(), name='PruebaTemplateView'),
]
