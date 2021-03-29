from django.contrib import admin
from django.urls import path
from . import views

# de esta manera podemos meternos dentro del array de urlpatterns ara poder llamar al name de la url
app_name = "persona_app"

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),
    path(
        'listar-todo-empleados/',
        views.ListAllEmpeados.as_view(),
        name='empleados_all',
    ),
    path(
        'listar-by-area/<shorname>',
        views.ListByAreaEmpleados.as_view(),
        name='empleado_area'
    ),
    path(
        'lista-empleados-admin/',
        views.ListaEmpleadosAdmin.as_view(),
        name='empleado_admin'
    ),
    path('listar-by-trabajo/', views.ListEmploydByWork.as_view()),
    path('buscar-empleado/', views.LisEmpleadosByKword.as_view()),
    path('listar-habilidades-empleado/', views.ListHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>',
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),
    path(
        'add-empleado/',
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'
    )    ,
    path('succes/', views.SuccessView.as_view(), name='correcto'),
    path(
        'update-empleado/<pk>',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),
    path(
        'delete-empleado/<pk>',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    ),

]
