from core.models import sede
from django.db import models


def getModelVerbosename():
    return [name.verbose_name for name in sede._meta.get_fields() if hasattr(name, 'verbose_name')]
