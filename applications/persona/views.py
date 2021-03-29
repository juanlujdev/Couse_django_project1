from django.shortcuts import render
from django.urls import reverse_lazy  # para navegar entre vistas
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,

)
# models
from .models import Empleado  # importo la tabla de la base de datos empleado
# forms
from .forms import EmpleadoForm


# Para el proyecto1
# ListView lista todos los datos de la tabla Empleado
class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10  # muestro los empleados de 4 en 4 para no sobrecargar los
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado


# ListView lista todos los datos de la tabla Empleado
class ListAllEmpeados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4  # muestro los empleados de 4 en 4 para no sobrecargar los
    ordering = 'first_name'

    # datos del servidor y funcine mas rapido
    # model = Empleado comento esto porque me voy a traer los datos con get_queryset
    # como tenemos que pasarle un parametro a la consulta (kword), hay que indicarselo en su input de
    # list_all.html, dandole un id con el mismo nombre "kword" y su name igiual
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            # icontains dice que me va a buscar las listas que contengan cualquier caracter que me venga en kword, y
            # si viene vacio te saca todo
            full_name__icontains=palabra_clave
        )
        return lista


# Clase de vista para ver nuestra pantalla de inicio
class InicioView(TemplateView):
    """vista que carga la pagina de inicio"""
    # como no va a estar dentro de ninguna carpeta en el teemplate, y va a estar directa en el template, no tiene ruta
    template_name = 'inicio.html'


# ListView devuelve una lista pero con especificaciones
class ListByAreaEmpleados(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    # en vez de model=Empleado y traerse todos los datos de la tabla se especifica que datos
    # quieres traer para ser mas rapido la carga de datos, con get_queryset
    def get_queryset(self):
        # guarda en area lo que traigas en el parametro "shorname" que ese "shorname" es
        # donde se guarda el dato en la url. si se va a urls veras que en el path continua con un
        # <shorname> lo que se escriba en el path se guardara ahi. ejem:listar-by-area/5
        # ese '5' se guardara en shorname
        area = self.kwargs['shorname']
        # saca y devuelveme una lista cuyo shor_name=area
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista


# listar empleados por trabajo
class ListEmploydByWork(ListView):
    template_name = 'persona/list_by_work.html'
    queryset = Empleado.objects.filter(

        job='0TRO'
    )


# listar empleados por palabra clave
class LisEmpleadosByKword(ListView):
    """lista empleados por palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print("********************")
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista


# listar habilidades de un empleado
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        nombre_clave = self.request.GET.get("kword", '')
        empleado = Empleado.objects.get(
            first_name=nombre_clave
        )
        return empleado.habilidades.all()


# Detealles de la vista de un  empleado
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        # con esto sacas toda su info, en la plantilla de html gestionas que info quieres sacar, en las url tienes que
        # que especificar un id que es pk para que sepa donde se esta clickando. se gestiona en urls
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # codigo para comprobar si es empleado del mes
        # se le pasa el 'titulo' que es "Empleado de mes" para poder utilizarlo en la plantilla html
        context['titulo'] = 'Empleado del mes'
        return context


# simplemente creo otra plantilla de html para cuando mas abajo cree un usuario valla a esta plantilla
class SuccessView(TemplateView):
    template_name = "persona/success.html"


# crear un formulario
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    # fields = ['first_name','last_name','job']
    # fields = ('__all__') aqui digo que salgan todos los campos de la bbdd de models empleado
    # saco los campos que me interesa, COMO ME VOY A TRAER UN FORM PERSONALIZADO, (EmpleadoForm), NO ME HACE FALTA LOS FIEDS
    #fields = [
    #    'first_name',
    #    'last_name',
    #    'job',
    # 'departamento',
    #  'habilidades',
    #   'avatar',
    #]

    form_class = EmpleadoForm#Me traigo el formulario personalizado EmpleadoForm, la diferencia entre poner los fields y eso es
    # que los fields los saca automatico sin poder personalizar los campos y con for_class, es su form.py puedes personalizarlos
    #como quieras

    # success_url = '/succes'  ingreso el path donde quiero ir despues de hacer el put de createview
    # con reverse_lazy voy a urls y llamo a donde tengo el array de urls "persona_app" y llamo a la
    # nombre de la url que quiero ir(se hace para casos q las url son muy largas)
    success_url = reverse_lazy('persona_app:empleado_admin')

    # valida si los datos son correctos los salva
    def form_valid(self, form):
        # logica del proceso
        empleado = form.save()  # recupera de la bbdd lo que acbamos de guardar
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()  # actualiza el campo fullname del empleado
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    # siempre tienes que ir a una pagina de confirmacion de lo que se quiere actualizar
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    # despues de ir a la pantalla de confirmaciond  de lo que se quiere actualizar se va a la pantalla 'correcto'
    success_url = reverse_lazy('persona_app:empleado_admin')

    # El poner el metodo post y el metodo form_valid juntos es solo para ver como de manera interna que se ejecuta primero
    # da igual el orden como lo pongamos, internamente siempre se ejecutara el metodo posto antes del form_valid
    # Validara que el formulario que recibe este todo ok
    def form_valid(self, form):
        # logica del proceso
        empleado = form.save()  # recupera de la bbdd lo que acbamos de guardar
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()  # actualiza el campo fullname del empleado
        return super(EmpleadoUpdateView, self).form_valid(form)

    # puedo gestionar lo que traigo en la actualizacion
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("*********Metodo Post***********")
        print("================================")
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)


# Borrar
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    # siempre tienes que ir a una pagina de confirmacion de lo que se quiere eliminar
    template_name = "persona/delete.html"
    # despues de ir a la pantalla de confirmaciond  de lo que se quiere actualizar se va a la pantalla 'correcto'
    success_url = reverse_lazy('persona_app:empleado_admin')
