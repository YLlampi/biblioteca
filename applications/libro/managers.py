import datetime

from django.db import models

from django.db.models import Q, Count


class LibroManager(models.Manager):
    """
    managers para el model Libro
    """

    def listar_libros(self, kword):
        fecha_actual = datetime.datetime.now()

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('1800-01-01', fecha_actual)
        )
        # print(fecha_actual)

        return resultado

    def listar_libros_entre_fechas(self, kword, fecha1, fecha2):
        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2)
        )

        return resultado

    def listar_libros_categoria(self, categoria):
        return self.filter(
            categoria__id=categoria,
        ).order_by('titulo')

    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro

    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_prestamos=Count('libro_prestamo')
        )
        return resultado

    def num_libros_prestados(self):
        resultado = self.annotate(
            num_prestados=Count('libro_prestamo')
        )
        for r in resultado:
            print('*****************+')
            print(r, r.num_prestados)

        return resultado


class CategoriaManager(models.Manager):
    """
    managers para el model Categoria
    """

    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()

    def cantidad_libros_por_categoria(self):
        resultado = self.annotate(
            num_libros=Count('categoria_libro')
        )

        for r in resultado:
            print('****')
            print(f'{r} |-|  {r.num_libros}')
        return resultado

