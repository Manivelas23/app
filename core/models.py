from django.db import models

# modelos para las tablas de la base de datos
from django.forms import model_to_dict


class tipo_identificacion(models.Model):
    identificacion = models.IntegerField(
        primary_key=True,
        verbose_name="numId")

    tipo = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=False,
        verbose_name="tipoId"
    )

    def __str__(self):
        return self.identificacion

    class Meta:
        ordering = ["identificacion"]
        verbose_name = "Tipo de Identifación"
        verbose_name_plural = "Tipo de Identificaciones"


class prueba(models.Model):
    tipo_prueba = models.CharField(
        max_length=9,
        unique=True,
        null=False,
        blank=False,
        verbose_name="tipo_prueba"
    )

    tipo_licencia = models.CharField(
        max_length=2,
        unique=True,
        null=True,
        blank=False,
        verbose_name="tipo_licencia"
    )

    def __str__(self):
        return self.tipo_prueba

    class Meta:
        ordering = ["id"]
        verbose_name = "Prueba"
        verbose_name_plural = "Pruebas"


class persona(models.Model):
    numero_identificacion = models.OneToOneField(
        tipo_identificacion,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="numIdPersona",
    )

    nombre = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=False,
        verbose_name="nombre"
    )

    primer_apellido = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=False,
        verbose_name="primerApellido",
    )

    segundo_apellido = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=False,
        verbose_name="segundoApellido",
    )

    def __str__(self):
        return self.numero_identificacion

    class Meta:
        ordering = ["numero_identificacion"]
        verbose_name = "Persona"
        verbose_name_plural = "Personas"


class sede(models.Model):
    ubicacion = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="ubicacionSede"
    )

    def __str__(self):
        return self.ubicacion

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        ordering = ["id"]
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"


class fecha(models.Model):
    fecha_disponible = models.DateTimeField(
        auto_now_add=False,
        null=False,
        blank=False,
        unique=True
    )

    id_sede = models.ForeignKey(
        sede,
        on_delete=models.DO_NOTHING
    )

    id_prueba = models.ForeignKey(
        prueba,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.fecha_disponible

    class Meta:
        ordering = ["fecha_disponible"]
        verbose_name = "fecha"
        verbose_name_plural = "fechas"


class cita(models.Model):
    # se hace un llamado a la tabla tipo_identificacion en vez de la persona
    id_persona = models.ForeignKey(
        tipo_identificacion,
        on_delete=models.CASCADE,
    )

    id_prueba = models.OneToOneField(
        prueba,
        on_delete=models.CASCADE
    )

    id_fecha_cita = models.OneToOneField(
        fecha,
        on_delete=models.CASCADE,
        verbose_name="fechaCita"
    )

    otras_indicaciones = models.CharField(
        max_length=450,
        null=True,
        blank=False)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ["id"]
        verbose_name = "cita"
        verbose_name_plural = "citas"
