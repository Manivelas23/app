from django.urls import path, include
from core.sedes.views import *
from core.fechas.views import *
from core.pruebas.views import *
from core.personas.views import *
from core.citas.views import *
from core.views import *

urlpatterns = [
    # dashboard index
    path('', DashboardIndexView.as_view(), name='DashboardIndexView'),

    # sedes
    path('sedes/', SedeListView.as_view(), name='SedeTemplateView'),

    # fechas
    path('generarfechas/', CreateFechaListView.as_view(), name='CreateFechaTemplateView'),
    path('fechas/', FechasListView.as_view(), name='FechaTemplateView'),

    # pruebas
    path('pruebas/', PruebaTemplateView.as_view(), name='PruebaTemplateView'),

    # personas
    path('personas/', ListPersonasView.as_view(), name='ListPersonasView'),
    path('crear-persona/', CrearPersonaView.as_view(), name='CrearPersonaView'),
    path('editar/persona/<int:pk>', EditarPersonaView.as_view(), name='EditarPersonaView'),
    path('eliminar/persona/<int:pk>', EliminarPersonaView.as_view(), name='EliminarPersonaView'),

    # citas
    path('citas/', ListCitasView.as_view(), name='ListCitasView'),
    path('crear-cita/', CrearCitaView.as_view(), name='CrearCitaView'),
    path('citas/imprimir/<int:pk>', DetalleCitaView.as_view(), name='DetalleCitaView'),

]
