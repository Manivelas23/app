from core.models import prueba, curso, sede
from django.db import models


def getModelVerbosename():
    return [name.verbose_name for name in sede._meta.get_fields()[1:4] if hasattr(name, 'verbose_name')]

