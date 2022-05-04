from appInfancia.models import Regionales, Municipios, Nacionalidad, Tipodiscapacidad, Persona, CentroZonal, Lengua, GruposEtnicos
from django import forms
from datetime import datetime
from django.forms.widgets import NumberInput


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


class CentroZonalForm(forms.ModelForm):
    class Meta:
        model = CentroZonal
        fields = '__all__'
        widgets = {
            'idcentro_zonal': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'id centro zonal'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'municipio': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'estado': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class NacionalidadForm(forms.ModelForm):
    class Meta:
        model = Nacionalidad
        fields = '__all__'
        widgets = {
            'idpais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Codigo'
                }
            ),

            'Pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del Pais'
                }
            ),

            'nacionalidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nacionalidad'
                }
            )
        }


class DiscapacidadForm(forms.ModelForm):
    class Meta:
        model = Tipodiscapacidad
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


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

        widgets = {

            'idtipoidentificacio': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombres'
                }
            ),
            'no_documento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'No Documento'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellidos'
                }
            ),
            'idsexo': forms.Select(
                attrs={
                    'title': 'Sexo',
                    'class': 'form-control'
                }
            ),
            'fecha_nacimiento': forms.SelectDateWidget(
                attrs={
                    'title': 'Municipio',
                    'class': 'form-control ',
                }, years=range(1900, 2090)),

            'idcentro_zonal': forms.Select(
                attrs={
                    'title': 'Centro Zonal',
                    'class': 'form-control',
                }
            ),

            'mun_codigodane': forms.Select(
                attrs={
                    'title': 'Municipio',
                    'class': 'form-control',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Direccion'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Telefono'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo'
                }
            ),
            'idgrupoetnico': forms.Select(

                attrs={
                    'title': 'Grupo Etnico',
                    'class': 'form-control',
                }

            ),
            'nacionalidades': forms.CheckboxSelectMultiple(

            ),
            'discapacidades': forms.CheckboxSelectMultiple(

            ),
            'lenguas': forms.CheckboxSelectMultiple(

            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )

        }


class GruposEtnicosForm(forms.ModelForm):
    class Meta:
        model = GruposEtnicos
        fields = '__all__'
        widgets = {

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
        }
