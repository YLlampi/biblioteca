from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Libro, Categoria

# Create your views here.


class LibroListView(ListView):
    context_object_name = 'lista_libros'
    template_name = "libro/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword","")

        # Fecha 1
        f1 = self.request.GET.get("fecha1","")
        # Fecha 2
        f2 = self.request.GET.get("fecha2","")

        if f1 and f2:
            return Libro.objects.listar_libros_entre_fechas(palabra_clave, f1, f2)
        else: 
            return Libro.objects.listar_libros(palabra_clave)


class LibroListView2(ListView):
    context_object_name = 'lista_libros'
    template_name = "libro/lista2.html"

    def get_queryset(self):
        categoria = 3
        return Libro.objects.listar_libros_categoria(categoria)


class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libro/detalle.html'