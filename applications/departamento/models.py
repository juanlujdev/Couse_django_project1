from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True)#permite ingresar campo vacio
    shor_name= models.CharField('Nombre Corto', max_length=20, unique=True)#unique para campo que no se repite
    anulate = models.BooleanField('Anulado',default=False)

    class Meta:
        verbose_name='Mi departamento'
        verbose_name_plural='Areas de la empresa'
        ordering=['-name']
        unique_together=('name','shor_name')#no se registrara una combinacion similar

    def __str__(self):
        return str(self.id) + '-'+ self.name + '-' + self.shor_name