from core.models import *
from django.db import models
from core.pruebas.extra import getTableData


def get_model_verbosename():
    return [field.verbose_name for field in fecha._meta.get_fields() if
            not isinstance(field, (models.ManyToOneRel, models.ManyToManyRel))]


def getSedes():
    return [i.toJSON() for i in sede.objects.all()]


getTableData()
