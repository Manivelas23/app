from django.urls import path
from core.sedes.views import *

urlpatterns = [
    path('', SedeListView.as_view(), name='sede_list_view'),
]
