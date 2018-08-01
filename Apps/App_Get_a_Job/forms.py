# coding=utf-8
from django import forms
from .models import *
from .models import Curriculum

class LoginForm(forms.ModelForm):
    fields = ['email', 'password']
    widgets = {
        'email': forms.EmailInput(),
        'password': forms.PasswordInput()
    }

class SolicitanteForm(forms.ModelForm):
    class Meta:
        model = Solicitante
        fields = ['Nombre', 'Apellido', 'Sexo', 'Fecha_Nacimiento', 'Cedula', 'Email', 'Clave', 'Clave2', 'Estado']
        """labels = {
                        'Cedula': 'Cédula',
                        'Nombre': 'Nombre',
                        'Apellido': 'Apellido',
                        'Sexo': 'Sexo',
                        'Fecha_Nacimiento': 'Fecha de Nacimiento',
                        'Email': 'Email',
                        'Clave': 'Contraseña',
                        'Estado': 'Estado'
                        }"""

        widgets = {
                'Nombre': forms.TextInput(attrs={
                        'id': "nombre",
                        'class': "form-control",
                        'type': "text",
                        'placeholder': "Nombre",
                        'name': "nombre",
                        'title': "Ingrese su nombre"
                    }),

                'Apellido': forms.TextInput(attrs={
                        'id': "apellido",
                        'class': "form-control",
                        'type': "text",
                        'placeholder': "Apellido",
                        'name': "apellido",
                        'title': "Ingrese su apellido.",
                    }),

                'Sexo': forms.Select(attrs={
                        'name': "genero",
                        'id': "genero",
                        'class': "form-control Genero",
                        'required': "required",
                        'title': "Seleccione el genero correspondiente"
                    }),

                'Fecha_Nacimiento': forms.DateInput(attrs={
                        'type': "date",
                        'name': "date",
                        'id': "fechaNaci",
                        'class': "form-control",
                        'required': "required",
                        'title': "Ingrese su fecha de nacimiento."
                    }),

                'Cedula': forms.NumberInput(attrs={
                        'class': "form-control",
                        'type': "text",
                        'name': "",
                        'value': "",
                        'required': "required",
                        'placeholder': "Cedula de Indentidad",
                        'id': "cedula"
                }),

                'Email': forms.EmailInput(attrs={
                        'id': "email",
                        'class': "form-control",
                        'type': "email",
                        'placeholder': "Email",
                        'name': "email",
                        'required': "required",
                        'title':  "Ingrese su email.",
                        'style': "width: 47%; float: right;"
                    }),

                'Clave': forms.PasswordInput(attrs={
                        'id': "password",
                        'class': "form-control",
                        'type': "password",
                        'placeholder': "Password",
                        'name': "password",
                        'title': "Ingrese un password.",
                        'required': "required"
                    }),

                'Clave2': forms.PasswordInput(attrs={
                    'id': "password_confirmation",
                    'class': "form-control",
                    'type': "password",
                    'placeholder': "Confirme su Password",
                    'name': "password_confirmation",
                    'title': "Confirme su password.",
                    'required': "required"
                }),

                'Estado': forms.TextInput(attrs={
                        'value': 'A',
                        'style': 'display: none',
                        'type': "text",
                        'class': "form-control",
                        'id': "Estado",
                    })
                }


class EmpleadoresForm(forms.ModelForm):
    class Meta:
        model = Empleadores
        fields = [ 'Nombre', 'FechaConst', 'FormaJurd', 'RNC', 'Direccion', 'Email', 'Clave', 'Clave2', 'Estado']
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
                        'title': "Ingrese la fecha de constitucion de la empresa."
                    }),

                'FormaJurd': forms.Select(attrs={
                        'name': "tipoEmpresa",
                        'id': "inputTipoEmpresa",
                        'class': "form-control",
                        'required': "required",
                        'title': "Seleccione el tipo de empresa correspondiente."
                    }),

                'RNC': forms.NumberInput(attrs={
                        'type': "text",
                        'class': "form-control",
                        'id': "RNC",
                        'placeholder': "RNC de la empresa",
                        'title': "Ingrese RNC de la empresa.",
                    }),
                'Direccion': forms.Select(attrs={
                        'type': "text",
                        'class': "form-control",
                        'id': "direccion",
                        'placeholder': 'Direccion de la empresa',
                        'title': "Ingrese la direccion de la empresa.",
                        'style': 'width: 47%; float: left;'
                    }),

                'Email': forms.EmailInput(attrs={
                'id': "email",
                'class': "form-control",
                'type': "email",
                'placeholder': "Email",
                'name': "emailEmpresa",
                'required': "required",
                'title': "Ingrese el email de la empresa."
            }),

                'Clave': forms.PasswordInput(attrs={
                        'id': "password",
                        'class': "form-control",
                        'type': "password",
                        'placeholder': "Password",
                        'name': "password",
                        'title': "Ingrese una password.",
                        'required': "required"
                    }),

                'Clave2': forms.PasswordInput(attrs={
                    'id': "password_confirmation",
                    'class': "form-control",
                    'type': "password",
                    'placeholder': "Confirme su Password",
                    'name': "password_confirmation",
                    'title': "Confirme su password.",
                    'required': "required"
                }),

                'Estado': forms.TextInput(attrs={
                        'value': 'A',
                        'style': 'display: none',
                        'type': "text",
                        'class': "form-control",
                        'id': "Estado",
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


class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = [
            'Cod_Curriculum',
            'Telefono',
            'Celular',
            'Pais',
            'Provincia',
            'Direccion',
            'Institucion',
            'Titulo',
            'Fecha_InicioC',
            'Fecha_FinC',
            'Otro_Estd',
            'Fecha_IniEstd',
            'Fecha_FinEstd',
            'InstOtrEsd',
            'Trabajo_Rect',
            'InstTrbj',
            'PeriodoTrbj',
            'DescripTrbj',
            'OtroTrbj',
            'InstOtrTrbj',
            'PeriodoOtrTrbj',
            'DescripOtrTrbj',
            'HabLab1',
            'HabLab2',
            'ObjetivoProf',
            'Cedula_Solct'
        ]

        labels = {
            'Cod_Curriculum': 'Cod_Curriculum',
            'Telefono': 'Telefono',
            'Celular': 'Celular',
            'Pais': 'Pais',
            'Provincia': 'Provincia',
            'Direccion': 'Direccion',
            'Institucion': 'Institucion',
            'Titulo': 'Titulo',
            'Fecha_InicioC': 'Fecha_InicioC',
            'Fecha_FinC': 'Fecha_FinC',
            'Otro_Estd':'Otro_Estd',
            'Fecha_IniEstd': 'Fecha_IniEstd',
            'Fecha_FinEstd': 'Fecha_FinEstd',
            'InstOtrEsd': 'InstOtrEsd',
            'Trabajo_Rect':'Trabajo_Rect',
            'InstTrbj':'InstTrbj',
            'PeriodoTrbj':'PeriodoTrbj',
            'DescripTrbj':'DescripTrbj',
            'OtroTrbj':'OtroTrbj',
            'InstOtrTrbj':'InstOtrTrbj',
            'PeriodoOtrTrbj':'PeriodoOtrTrbj',
            'DescripOtrTrbj':'DescripOtrTrbj',
            'HabLab1':'HabLab1',
            'HabLab2':'HabLab2',
            'ObjetivoProf':'ObjetivoProf',
            'Cedula_Solct': 'Cedula_Solct'
        }

        widgets = {
            'Cod_Curriculum': forms.NumberInput(attrs={'class': 'form-control'}),
            'Telefono':  forms.NumberInput(attrs={'class': 'form-control'}),
            'Celular': forms.NumberInput(attrs={'class': 'form-control'}),
            'Pais': forms.Select(attrs={'class': 'form-control'}),
            'Provincia': forms.Select(attrs={'class': 'form-control'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'Institucion': forms.Select(attrs={'class': 'form-control'}),
            'Titulo': forms.Select(attrs={'class': 'form-control'}),
            'Fecha_InicioC': forms.DateInput(attrs={'class': 'form-control'}),
            'Fecha_FinC': forms.DateInput(attrs={'class': 'form-control'}),
            'Otro_Estd': forms.Select(attrs={'class': 'form-control'}),
            'Fecha_IniEstd': forms.DateInput(attrs={'class': 'form-control'}),
            'Fecha_FinEstd': forms.DateInput(attrs={'class': 'form-control'}),
            'InstOtrEsd': forms.Select(attrs={'class': 'form-control'}),
            'Trabajo_Rect': forms.TextInput(attrs={'class': 'form-control'}),
            'InstTrbj': forms.TextInput(attrs={'class': 'form-control'}),
            'PeriodoTrbj': forms.NumberInput(attrs={'class': 'form-control'}),
            'DescripTrbj': forms.Textarea(attrs={'class': 'form-control'}),
            'OtroTrbj': forms.TextInput(attrs={'class': 'form-control'}),
            'InstOtrTrbj': forms.TextInput(attrs={'class': 'form-control'}),
            'PeriodoOtrTrbj': forms.NumberInput(attrs={'class': 'form-control'}),
            'DescripOtrTrbj': forms.Textarea(attrs={'class': 'form-control'}),
            'HabLab1': forms.Select(attrs={'class': 'form-control'}),
            'HabLab2': forms.Select(attrs={'class': 'form-control'}),
            'ObjetivoProf': forms.Textarea(attrs={'class': 'form-control'}),
            'Cedula_Solct': forms.Select(attrs={'class': 'form-control'})
        }



"""
class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Empleadores
        fields = [ 'Cod_Curriculum', 'Telefono', 'Celular', 'Pais', 'Provincia', 'Direccion', 'Institucion', 'Titulo', 'Fecha_InicioC', 'Fecha_FinC', 'Otro_Estd', 'Fecha_IniEstd', 'Fecha_FinEstd', 'InstOtrEsd', 'Trabajo_Rect', 'InstTrbj', 'PeriodoTrbj', 'DescripTrbj', 'OtroTrbj', 'InstOtrTrbj', 'PeriodoOtrTrbj', 'DescripOtrTrbj', 'HabLab1', 'HabLab2', 'ObjetivoProf', 'Cedula_Solct']
        labels = {
                'Cod_Curriculum': 'Cod_Curriculum',
                'Telefono': 'Telefono',
                'Celular': 'Celular',
                'Pais': 'Pais',
                'Provincia': 'Provincia',
                'Direccion': 'Direccion',
                'Institucio': 'Institucio',
                'Titulo': 'Titulo',
                'Fecha_Inicio': 'Fecha_Inicio',
                'Fecha_Fin': 'Fecha_Fin',
                'Otro_Estd': 'Otro_Estd',
                'Fecha_IniEstd': 'Fecha_IniEstd',
                'Fecha_FinEstd': 'Fecha_FinEstd',
                'InstOtrEsd': 'InstOtrEsd',
                'Trabajo_Rect': 'Trabajo_Rect',
                'InstTrbj': 'InstTrbj',
                'PeriodoTrbj': 'PeriodoTrbj',
                'DescripTrbj': 'DescripTrbj',
                'OtroTrbj': 'OtroTrbj',
                'InstOtrTrbj': 'InstOtrTrbj',
                'PeriodoOtrTrbj': 'PeriodoOtrTrbj',
                'DescripOtrTrbj': 'DescripOtrTrbj',
                'HabLab1': 'HabLab1',
                'HabLab2': 'HabLab2',
                'ObjetivoProf': 'ObjetivoProf'
                }

        widgets = {
                'Cod_Curriculum': forms.NumberInput(attrs={}),
                'Telefono': forms.NumberInput(attrs={
                        'class': "form-control",
                        'id': "ex2",
                        'type': "number",
                        'placeholder': 'Ingrese sun numero de telefono',
                        'style': 'display: block, width: 100%, padding: .375rem .75rem, font-size: 1rem, line-height: 1.5, color: #495057, background-color: #fff, background-clip: padding-box, border: 1px solid #ced4da, border-radius: .25rem'

                }),

                'Celular': forms.NumberInput(attrs={

                        'class':"form-control",
                        'id':"ex2",
                        'type':"number",
                        'placeholder': 'Ingrese sun numero de celular',
                        'style': 'display: block, width: 100%, padding: .375rem .75rem, font-size: 1rem, line-height: 1.5, color: #495057, background-color: #fff, background-clip: padding-box, border: 1px solid #ced4da, border-radius: .25rem'
                    }),

                'Pais': forms.Select(attrs={
                        'name': "titulo" ,
                        'id': "inputTitulo" ,
                        'class': "form-control",
                        'required': "required" ,
                        'title': "Seleccione un pais."
                    }),

                'Provincia': forms.Select(attrs={
                        'name': "titulo",
                        'id': "inputTitulo",
                        'class': "form-control",
                        'required': "required",
                        'title' :"Seleccione el titulo adquirido."
                    }),

                'Direccion': forms.TextInput(attrs={
                         'class': "form-control",
                         'id': "ex3",
                         'type': "text",
                    }),

                'Institucion': forms.Select(attrs={
                    'name': "titulo",
                    'id': "inputTitulo",
                    'class': "form-control" ,
                    'required': "required" ,
                    'title': "Seleccione institucion donde estudio."
            }),

                'Titulo': forms.TextInput(attrs={
                        'name': "titulo",
                        'id': "inputTitulo",
                        'class': "form-control" ,
                        'required': "required" ,
                        'title': "Seleccione el titulo adquirido."
                    }),

                'Fecha_InicioC': forms.DateInput(attrs={
                       'name': "",
                       'id': "entradas",
                       'class': "form-control",
                       'required': "required",
                       'title': "Ingrese la fecha en que inicio.",
                       'placeholder': "Fecha en que obtuvo su título profesional",
                       'type': "date"
                }),

                'Fecha_FinC': forms.DateInput(attrs={
                        'name': "",
                        'id': "entradas",
                        'class': "form-control",
                        'required': "required",
                        'title': "Ingrese la fecha en que inicio.",
                        'placeholder': "Fecha en que obtuvo su título profesional",
                        'type': "date"
                }),

                'Otro_Estd': forms.Select(attrs={
                        'id':"entradas",
                        'class':"form-control",
                        'name':"otrosEstudios",
                        'required':"required",
                        'title':"Ingrese otros estudios realizados.",
                        'placeholder':"Otros estudios" ,
                        'type': "select"
                }),

                'Fecha_IniEstd': forms.DateInput(attrs={
                    'name': "",
                    'id': "entradas",
                    'class': "form-control",
                    'required': "required",
                    'title': "Ingrese la fecha en que inicio.",
                    'placeholder': "Fecha en que obtuvo su título profesional",
                    'type': "date"
                }),

                'Fecha_FinEstd': forms.DateInput(attrs={
                    'name': "tipoEmpresa",
                    'id': "inputTipoEmpresa",
                    'class': "form-control",
                    'required': "required",
                    'title': "Seleccione el tipo de empresa correspondiente."
                }),

                'InstOtrEsd': forms.Select(attrs={
                    'type': "text",
                    'class': "form-control",
                    'id': "RNC",
                    'placeholder': "RNC de la empresa",
                    'title': "Ingrese RNC de la empresa.",
                }),

                'Trabajo_Rect': forms.TextInput(attrs={
                        'id':"entradas" ,
                        'class':"form-control entradas" ,
                        'name':"trbjRenct" ,
                        'required':"required" ,
                        'title':"Ingrese su trabajo mas reciente." ,
                        'placeholder':"Trabajo mas reciente",
                        'type': "text"
                }),

                'InstTrbj': forms.TextInput(attrs={
                        'id':"entradas",
                        'class': "form-control entradas",
                        'placeholder':"Institución donde trabajó",
                        'name': "instTrbjR",
                        'title':"Ingrese el nombre de la institución donde trabajó.",
                        'style':"",
                        'type':"text"
                }),

                'PeriodoTrbj': forms.NumberInput(attrs={
                        'name': "",
                        'id': "entradas",
                        'class ': "form-control entradas",
                        'required': "required",
                        'title': "Ingrese el período durante el que trabajó.",
                        'placeholder': "Período en que trabajó",
                        'type': "number"
                }),

                'DescripTrbj': forms.Textarea(attrs={
                        'id':  "entradas",
                        'class': "form-control entradas" ,
                        'required': "required" ,
                        'title': "Ingrese el período durante el que trabajó." ,
                        'placeholder': "Descripción de la labor que desempeñaba",
                }),

                'OtroTrbj': forms.TextInput(attrs={
                        'id ':  "entradas",
                        'class ': "form-control entradas" ,
                        'name': "OtrbjRenct" ,
                        'required': "required" ,
                        'title': "Ingrese otro trabajo." ,
                        'placeholder': "Otros trabajos" ,
                        'type': "text"
                }),

                'InstOtrTrbj': forms.TextInput(attrs={
                        'id': "entradas",
                        'class': "form-control entradas",
                        'placeholder': "Institución donde trabajó",
                        'name': "instTrbjR",
                        'title': "Ingrese el nombre de la institución donde trabajó.",
                        'style': "",
                        'type': "text"
                }),

                'PeriodoOtrTrbj': forms.NumberInput(attrs={
                            'name': "",
                            'id': "entradas",
                            'class ': "form-control entradas",
                            'required': "required",
                            'title': "Ingrese el período durante el que trabajó.",
                            'placeholder': "Período en que trabajó",
                            'type': "number"
                }),

                'DescripOtrTrbj': forms.Textarea(attrs={
                        'id': "entradas",
                        'class': "form-control entradas",
                        'required': "required",
                        'title': "Ingrese el período durante el que trabajó.",
                        'placeholder': "Descripción de la labor que desempeñaba",
                }),

                'HabLab1': forms.Select(attrs={
                        'name':  "titulo",
                        'id':  "inputTitulo",
                        'class': "form-control" ,
                        'required': "required" ,
                        'title': "Seleccione la habilidad desarrollada.",
                }),
                'HabLab2': forms.Select(attrs={
                        'name': "titulo",
                        'id': "inputTitulo",
                        'class': "form-control",
                        'required': "required",
                        'title': "Seleccione la habilidad desarrollada.",
                }),

                'ObjetivoProf': forms.Textarea(attrs={
                        'id': "entradas",
                        'class': "form-control entradas",
                        'required': "required",
                        'title': "Ingrese el objetivo que lo motiva a buscar trabajo.",
                        'placeholder': "Describa su objetivo profesional",
                }),

                'Cedula_Solct': forms.Select(attrs={
                    'placeholder': 'hola'})
                }
"""






"""
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['Nombre', 'Apellido', 'Sexo', 'Fecha_Nacimiento', 'Cedula', 'Email', 'Clave', 'Clave2', 'Estado']
"""


"""
class muestraPerfil(forms.ModelForm):
    class Meta:
        model1 = Solicitante
        model2 = Curriculum
        fields1 = ['Nombre', 'Apellido']
        fields2 = ['DescripOtrTrbj']
"""