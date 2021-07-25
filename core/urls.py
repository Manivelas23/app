from django.urls import path
from core.sedes.views import *
from core.fechas.views import *
from core.pruebas.views import *

urlpatterns = [
    path('', SedeListView.as_view(), name='SedeTemplateView'),
    path('fechas/', FechaListView.as_view(), name='FechaTemplateView'),
    path('pruebas/', PruebaTemplateView.as_view(), name='PruebaTemplateView'),
]
