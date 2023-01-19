from django.db import models

# managers
from .managers import AutorManager


# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveSmallIntegerField()

    objects = AutorManager()

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.apellido}'
