from django.db import models

# modelos para las tablas de la base de datos
from django.forms import model_to_dict


class tipo_identificacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Tipo Identificacion"
    )

    def __str__(self):
        return str(self.tipo)

    class Meta:
        ordering = ["tipo"]
        verbose_name = "Tipo de Identifación"
        verbose_name_plural = "Tipo de Identificaciones"


class curso(models.Model):
    nomb_curso = models.CharField(
        max_length=200,
        unique=False,
        null=True,
        blank=True,
        verbose_name="Nombre del Curso"
    )
    tipo_curso = models.CharField(
        max_length=300,
        unique=False,
        null=True,
        blank=True,
        verbose_name="Tipo de Curso"
    )
    desc_curso = models.CharField(
        max_length=300,
        unique=False,
        null=True,
        blank=True,
        verbose_name="Descripcion de Curso"
    )

    def __str__(self):
        return str(self.id)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        ordering = ["id"]
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class prueba(models.Model):
    tipo_prueba = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        blank=False,
        verbose_name="Tipo de Prueba"
    )

    tipo_licencia = models.CharField(
        max_length=2,
        unique=False,
        null=True,
        blank=True,
        verbose_name="Tipo de Licencia"
    )
    id_curso = models.ForeignKey(
        curso,
        on_delete=models.CASCADE
    )

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return str('{} - {}'.format(self.tipo_prueba, self.tipo_licencia))

    class Meta:
        ordering = ["id"]
        verbose_name = "Prueba"
        verbose_name_plural = "Pruebas"


class persona(models.Model):
    numero_identificacion = models.IntegerField(
        primary_key=True,
        null=False,
        unique=True
    )

    nombre = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Nombre"
    )

    primer_apellido = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Primer Apellido",
    )

    segundo_apellido = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Segundo Apellido",
    )
    tipo_identificacion_persona = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Tipo Identificación Persona",
    )

    def __str__(self):
        return str(self.numero_identificacion)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Persona"
        verbose_name_plural = "Personas"


class sede(models.Model):
    ubicacion = models.CharField(
        max_length=60,
        null=False,
        blank=False,
        unique=True,
        verbose_name="Ubicación de la Sede"
    )
    cant_supervisores = models.IntegerField(
        default=0,
        verbose_name="Cantidad de Supervisores"
    )
    cant_computadoras = models.IntegerField(
        default=0,
        verbose_name="Cantidad de Computadoras"
    )
    activo = models.CharField(
        max_length=5,
        verbose_name="Sede Activa"
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


class Fecha(models.Model):
    fecha_disponible = models.DateTimeField(
        auto_now_add=False,
        null=False,
        blank=False,
        unique=False,
        verbose_name='Fecha Disponible'
    )
    fecha_fin = models.DateTimeField(
        auto_now_add=False,
        null=False,
        blank=False,
        unique=False,
        verbose_name='Fecha Fin'
    )

    id_sede = models.ForeignKey(
        sede,
        on_delete=models.DO_NOTHING,
        verbose_name='Sede'
    )

    id_prueba = models.ForeignKey(
        prueba,
        on_delete=models.DO_NOTHING,
        verbose_name='Prueba'
    )

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return str(self.fecha_disponible)

    class Meta:
        ordering = ["fecha_disponible"]
        verbose_name = "fecha"
        verbose_name_plural = "fechas"


class cita(models.Model):
    # se hace un llamado a la tabla tipo_identificacion en vez de la persona
    id_persona = models.ForeignKey(
        persona,
        on_delete=models.DO_NOTHING,
    )

    id_fecha_cita = models.ForeignKey(
        Fecha,
        on_delete=models.CASCADE,
        verbose_name="Fecha de la Cita"
    )

    otras_indicaciones = models.CharField(
        max_length=450,
        null=True,
        blank=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["id"]
        verbose_name = "cita"
        verbose_name_plural = "citas"
