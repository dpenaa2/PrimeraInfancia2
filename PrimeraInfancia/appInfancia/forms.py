from django import forms
from appInfancia.models import Regionales,Municipios


class RegionForm(forms.ModelForm):
    class Meta:
        model = Regionales
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),

            'estado': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipios
        fields = '__all__'
        widgets = {
            'codigodane': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Codigo DANE'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'Regional': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'estado': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }


