from django.urls import path
from . import views


urlpatterns = [
    path('autores/', views.AutorListView.as_view(), name='autores')
]