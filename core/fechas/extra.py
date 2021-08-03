from core.models import fecha, prueba, curso
from django.db import models
from core.pruebas.extra import get_table_data


def get_model_verbosename():
    return [field.verbose_name for field in fecha._meta.get_fields() if
            not isinstance(field, (models.ManyToOneRel, models.ManyToManyRel))]


get_table_data()
