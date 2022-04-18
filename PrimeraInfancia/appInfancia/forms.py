from django import forms
from datetime import datetime
from appInfancia.models import Regionales, Municipios, Nacionalidad, Tipodiscapacidad, Persona,CentroZonal


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
                    'class': 'form-control',
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
                    'class': 'form-control',
                }
            ),
            'no_documento': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su identificación',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),

            'sexo': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d',
                                                attrs={
                                                    'value': datetime.now().strftime('%Y-%m-%d'),
                                                }
                                                ),
            'idnacionalidad': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'cz_idcentro_zonal': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'cz_mun_codigodane': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'direccion': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su direccion',
                }
            ),

            'ge_idgrupoetnico': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'discapacidad': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'Lenguas': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'telefono': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su telefono',
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su correo',
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }
