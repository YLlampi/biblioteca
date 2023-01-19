from django.urls import path
from . import views


urlpatterns = [
    path('libros/', views.LibroListView.as_view(), name='libros'),
    path('libros-2/', views.LibroListView2.as_view(), name='libros2'),
    path('libro-detalle/<pk>', views.LibroDetailView.as_view(), name='libro-detalle'),
]