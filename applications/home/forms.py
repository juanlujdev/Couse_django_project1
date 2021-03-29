from django import forms

from .models import Prueba


# editar formulario ModelForm estan vinculados directamente a un modelo
class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        # un widget hace que se personalice cada campo del formulario, actua como un diccionario, por eso( 'titulo':
        #forms.TextInput. aunque viene desdeel model como texto puedo modificarlo aqui
        # aparte lo podemos personalizar mas desde attrs con todos los atributos que que tiene los
        #input.
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aqui'
                }
            )
        }

    # funcion para validar que un campo cumpla ciertos parametros, siempre se llama clea_"nombre de campo a validar"
    # nunca guardara un formulario si no esta ok todos los formularios
    def clean_cantidad(self):
        # manera de recuperar los datos de campo cantidada
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            # raise gestiona el error, con forms(que esta importado de django) y es para hacer los formularios,
            # lo que hago es q si sale un error (que es menor de 10 la cantidad) nos salga una excepcion en la parte del
            # formulario donde estamos ingresando ese campo.
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad
