from django.urls import path
from core.sedes.views import *
from core.fechas.views import *

urlpatterns = [
    path('', SedeListView.as_view(), name='sede_list_view'),
    path('fechas', FechaListView.as_view(), name='fecha_list_view'),
]
