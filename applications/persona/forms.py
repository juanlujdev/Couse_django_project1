from django import forms

from .models import Empleado


class EmpleadoForm(forms.ModelForm):  # como dependemos de un modelo(bbdd) lo hacemos como ModelForm

    class Meta:
        model = Empleado
        fields=(
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',
        )

        widgets={
            'habilidades':forms.CheckboxSelectMultiple()#de los formiularios me traes el checkboxselec...
        }
