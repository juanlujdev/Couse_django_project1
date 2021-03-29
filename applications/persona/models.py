from django.db import models
# PARA HACER LA FOREIGNKEY DE LA TABLA DEPARTAMENTO
from applications.departamento.models import Departamento
# importacion de app de terceros
from ckeditor.fields import RichTextField


# Create your models here.

#en la clase de abajo describo perfectamemnte que hace cada cosa
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + ' ' + self.habilidad


class Empleado(models.Model):
    """Modelo para tabla empleado"""

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', '0TRO'),
    )
    #caracteristicas de los campos
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombres completos', max_length=120, blank=True)
    job = models.CharField('Trabajos', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)#hace referencia en la foreign key
    # de la tabla departamento que es de la otra app
    avatar = models.ImageField(upload_to='media/empleado',blank=True,null=True)
    habilidades = models.ManyToManyField(Habilidades)#habilidades y empleados se relacionan muchos a muchos
    hoja_vida = RichTextField()#importacion de la libreria ckeditor

    class Meta:#como quiero que me devuelva el listado
        verbose_name = 'Persona'
        verbose_name_plural = 'Diferenctes personas'
        ordering = ['id']
        # unique_together=('name','shor_name')#no se registrara una combinacion similar

    def __str__(self):#que quiero que me devuelva el listado de Empleado
        return str(self.id) + ' ' + self.first_name + ' - ' + self.last_name
