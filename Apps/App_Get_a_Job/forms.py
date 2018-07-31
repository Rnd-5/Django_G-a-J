# coding=utf-8
from django import forms
from django.forms import TextInput

from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SolicitanteForm(forms.ModelForm):
    class Meta:
        model = Solicitante
        fields = ['Cedula', 'Nombre', 'Apellido', 'Sexo', 'Fecha_Nacimiento', 'Email', 'Clave', 'Estado']
        labels = {
                        'Cedula': 'Cédula',
                        'Nombre': 'Nombre',
                        'Apellido': 'Apellido',
                        'Sexo': 'Sexo',
                        'Fecha_Nacimiento': 'Fecha de Nacimiento',
                        'Email': 'Email',
                        'Clave': 'Contraseña',
                        'Estado': 'Estado'
                        }
        widgets = {
                    'Cedula': forms.NumberInput(),
                    'Nombre': forms.TextInput(),
                    'Apellido': forms.TextInput(),
                    'Sexo': forms.TextInput(),
                    'Fecha_Nacimiento': forms.DateInput(),
                    'Email': forms.EmailInput(),
                    'Clave': forms.PasswordInput(),
                    'Estado': forms.TextInput()
                  }


class EmpleadoresForm(forms.ModelForm):
    class Meta:
        model = Empleadores
        fields = ['RNC', 'Nombre', 'FechaConst', 'FormaJurd', 'Direccion', 'Email', 'Clave', 'Estado']
        """labels = {
                'RNC': 'RNC',
                'Nombre': 'Nombre',
                'FechaConst': 'FechaConst',
                'FormaJurd': 'FormaJurd',
                'Email': 'Email',
                'Direccion': 'Direccion',
                'Clave': 'Clave',
                'Estado': 'Estado'
                }"""
        widgets = {
                'Nombre': forms.TextInput(attrs={
                        'type': 'text',
                        'class': 'form-control',
                        'id': 'nomEmpresa',
                        'placeholder': 'Nombre de la Empresa',
                        'title': 'Ingrese el nombre de la empresa.',
                    }),

                'FechaConst': forms.DateInput(attrs={
                        'type': 'date',
                        'name': "fechaEmpresa",
                        'id': "inputFechaEmpresa",
                        'class': "form-control",
                        'value': "",
                        'required': "required",
                        'title': "Ingrese la fecha de constitución de la empresa."
                    }),

                'FormaJurd': forms.Select(attrs={
                        'name': "tipoEmpresa",
                        'id': "inputTipoEmpresa",
                        'class': "form-control",
                        'required': "required",
                        'title': "Seleccione el tipo de empresa correspondiente."
                    }),

                'Email': forms.EmailInput(attrs={
                        'id':  "email",
                        'class': "form-control",
                        'type': "email",
                        'placeholder': "Email",
                        'name': "emailEmpresa",
                        'required': "required",
                        'title': "Ingrese el email de la empresa."
                    }),

                'Direccion': forms.TextInput(attrs={

                    }),

                'Clave': forms.PasswordInput(attrs={

                    }),

                'Estado': forms.TextInput(attrs={

                    })

                }


class OfertasForm(forms.ModelForm):
    class Meta:
        model = Oferta_Empl
        fields = ['Cantidad_P', 'Puesto', 'A_Experiencia', 'Horario_Trbj', 'Salario', 'Telefono', 'Estado', 'Empleadores_RNC']
        labels = {
                        'Cantidad_P':      'Cantidad de Puestos',
                        'Puesto':          'Puesto',
                        'A_Experiencia':   'Años de Experiencia',
                        'Horario_Trbj':    'Horario de Trabajo',
                        'Salario':         'Salario',
                        'Telefono':        'Teléfono',
                        'Estado':          'Estado',
                        'Empleadores_RNC': 'Empleadores_RNC'
                        }
        widgets = {
                    'Cantidad_P': forms.NumberInput(),
                    'Puesto': forms.TextInput(),
                    'A_Experiencia': forms.NumberInput(),
                    'Horario_Trbj': forms.TextInput(),
                    'Salario': forms.NumberInput(),
                    'Telefono': forms.NumberInput(),
                    'Estado': forms.TextInput(),
                    'Empleadores_RNC': forms.Select()
                  }


