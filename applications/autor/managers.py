from django.db import models

from django.db.models import Q


class AutorManager(models.Manager):
    """
    managers para el model Autor
    """

    def listar_autores(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        )

        return resultado

    def buscar_autor_nombre_o_apellido(self, kword):
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellido__icontains=kword)
        )

        return resultado

    def buscar_autor_excluir_edad(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        ).exclude(
            Q(edad__icontains=68) | Q(edad__icontains=65)
        )

        return resultado

    def buscar_autor_mayor_y_menor(self, kword):
        resultado = self.filter(
            edad__gt=50,
            edad__lt=65
        ).order_by('apellido', 'nombre')

        return resultado
