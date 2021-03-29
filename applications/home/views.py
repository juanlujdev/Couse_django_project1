from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)
# import models
from .models import Prueba

from .forms import PruebaForm


class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foudation.html'


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['1', '10', '20', '30']


class ListaPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    # quito lòs campos que quiero visualizar porque con la importacion de PruebaForm de mi forms.py los voy a sacar
    # fields = ['titulo', 'subtitulo', 'cantidad']
    # con form_class = PruebaForm me traigo tambien el campo field de forms.py asi no me da error y sigue teniendo form
    # del html sus field (campos) a mostrar
    form_class = PruebaForm
    success_url = '/'
