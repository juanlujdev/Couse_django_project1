from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import NewDepartamentoForm
# me traigo la tabla del modelo de Empleado porque como dice el ejercicio se tiene que hacer un post a la vez tanto
# en el departamento como en el empleado
from applications.persona.models import Empleado
# Me traigo de models la tabla de datos de Departamento por el mismo caso que digo arriba con lo de Empleado
from .models import Departamento

#Proyecto 1
class DepartamentoListView(ListView):
    template_name = 'departamento/lista.html'
    model = Departamento
    context_object_name = 'departamentos'



# El ejercicio consta de que se puede registrar un nuevo departameneto solo si hay un empleado en dicho departamento, por
# lo tanto se debe registrar un departamento a la vez que un empleado, sde tiene que hacer en base de dos modelos
# Cuando no vamos a trabajar sobre una tabla de un modelo y tenemos que trabajar sobre varias tablas utilizamos FormView
# En la clase persona en su view importamos su model que sera Empleado porque solo trabaja con una tabla
class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    # como tengo que hacer mi formulario, lo primero que hago es importarme mi formulario que esta en forms y previamente
    # esta hecho. igualo al form_class mi formulario hecho, es la manera de hacer un formulario personalizado, esta en forms
    # se llama NewDepartamentoForm
    form_class = NewDepartamentoForm
    # RECORDATORIO: succes para dirigir cuando se complementa el formulario
    success_url = '/'

    # RECORDATORIO form_valid metodo que validara que el formulario esta todo correcto, le pasamos niestro form
    def form_valid(self, form):
        print("***********estamos en el form valid****************")
        # instanciamos Departamento y asignamos form.cleaned_data los datos del campo departamento que viene de
        # nuestro form a los campos de models name y shor_name y guardamos los datos en su tabla. despues se lo
        # asignamos en el campo departamento de Empleados.objects.create para que a cada usuario creado quede guardado
        # su departamento
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname'],
        )
        depa.save()
        # con form.cleaned_data recupero los datos del campo de nombre y apellidos
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        # para guardar en el modelo (bbdd)empleado se utiliza siempre su objects.create() y se ve que palabra exacta
        # utilizaba cada campo en esa tabla
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',  # Esta puesto como dato obligatorio a rellenar y como en su model es un choices su id es numerico
            departamento=depa  # Departamento esta en la tabla (mopdel) departamento

        )

        return super(NewDepartamentoView, self).form_valid(form)
