from django.contrib import admin
from django.urls import path

from . import views


# de esta manera podemos meternos dentro del array de urlpatterns ara poder llamar al name de la url
app_name = "departamento_app"


urlpatterns = [
    path(
        'new-departamento/',
        views.NewDepartamentoView.as_view(),
        name='nuevo-departamento'
    ),
    path(
        'departamento-lista/',
        views.DepartamentoListView.as_view(),
        name='departamento_list'
    ),
]
