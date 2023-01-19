from django.db import models

from ..libro.models import Libro

from .managers import PrestamoManager
# Create your models here.


class Lector(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=20)
    edad = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return self.nombre


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')

    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)

    devuelto = models.BooleanField()

    objects = PrestamoManager()

    def __str__(self) -> str:
        return f'{self.libro.titulo}'