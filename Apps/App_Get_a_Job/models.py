# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Genero(models.Model):
    Cod_Gen = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=20)
    Sigla = models.CharField(max_length=1)

    def __str__(self):
        return self.Sigla

#######################
"""
class uSolicitante(models.Model):
    Nombre = models.OneToOneField(User)
    Apellido = models.CharField(max_length=100)
    Sexo = models.ForeignKey(Genero, on_delete=models.CASCADE)
    Fecha_Nacimiento = models.DateField()
    Email = models.EmailField(max_length=50)
    Clave = models.CharField(max_length=75)
"""
#######################

class Solicitante(models.Model):
    Cedula = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=100)
    Sexo = models.ForeignKey(Genero, on_delete=models.CASCADE)
    Fecha_Nacimiento = models.DateField()
    Email = models.EmailField(max_length=50)
    Clave = models.CharField(max_length=75)
    Clave2 = models.CharField(max_length=75)
    Estado = models.CharField(max_length=1)

    def __str__(self):
        return self.Nombre + " " + self.Apellido

class TipoEmpresa(models.Model):
    Cod_TipoEmpr = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=10)
    Descripcion = models.CharField(max_length=60)

    def __str__(self):
        return self.Nombre

class Provincias(models.Model):
    Cod_Provincia = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Paises(models.Model):
    Cod_Pais = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Empleadores(models.Model):
    Nombre = models.CharField(max_length=50)
    FechaConst = models.DateField()
    FormaJurd = models.ForeignKey(TipoEmpresa, on_delete=models.CASCADE)
    RNC = models.IntegerField(primary_key=True)
    Direccion = models.ForeignKey(Provincias, on_delete=models.CASCADE)
    Email = models.EmailField(max_length=50)
    Clave = models.CharField(max_length=75)
    Clave2 = models.CharField(max_length=75)
    Estado = models.CharField(max_length=1)

    def __str__(self):
        return self.Nombre + " " + str(self.FormaJurd)

class Oferta_Empl(models.Model):
    Cod_OfertaTrbj = models.AutoField(primary_key=True)
    Cantidad_P = models.IntegerField()
    Puesto = models.CharField(max_length=50)
    A_Experiencia = models.IntegerField()
    Horario_Trbj = models.CharField(max_length=25)
    Salario = models.IntegerField()
    Telefono = models.IntegerField()
    Empleadores_RNC = models.ForeignKey(Empleadores, on_delete=models.CASCADE)
    Estado = models.CharField(max_length=1)

    def __str__(self):
        return "Puesto de: " + self.Puesto + " por: " + str(self.Empleadores_RNC)

class Universidades(models.Model):
    Cod_Univ = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre


class InstEstd(models.Model):
    Cod_InstEstd = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Carreras(models.Model):
    Cod_Carr = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=50)
    InstEstd = models.ManyToManyField(InstEstd)

    def __str__(self):
        return self.Descripcion

class HabilidadesCarr(models.Model):
    Cod_Habld = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=50)
    Cod_Carr = models.ForeignKey(Carreras, on_delete=models.CASCADE)

    def __str__(self):
        return self.Descripcion

class OtrosEstd(models.Model):
    Cod_Estd = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Cod_InstEstd = models.ForeignKey(InstEstd, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre

class HabilidadesEstd(models.Model):
    Cod_Habld = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=50)
    Cod_Estd = models.ForeignKey(OtrosEstd, on_delete=models.CASCADE)

    def __str__(self):
        return self.Descripcion



class Curriculum(models.Model):
    Cod_Curriculum = models.AutoField(primary_key=True)
    Telefono = models.IntegerField()
    Celular = models.IntegerField()
    Pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    Provincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)
    Direccion = models.CharField(max_length=70)
    Institucion = models.ForeignKey(Universidades, on_delete=models.CASCADE)
    Titulo = models.ForeignKey(Carreras, on_delete=models.CASCADE)
    Fecha_InicioC = models.DateField()
    Fecha_FinC = models.DateField()
    Otro_Estd = models.ForeignKey(OtrosEstd, on_delete=models.CASCADE)
    Fecha_IniEstd = models.DateField()
    Fecha_FinEstd = models.DateField()
    InstOtrEsd = models.ForeignKey(InstEstd, on_delete=models.CASCADE)
    Trabajo_Rect = models.CharField(max_length=50)
    InstTrbj = models.CharField(max_length=50)
    PeriodoTrbj = models.IntegerField()
    DescripTrbj = models.CharField(max_length=2500)
    OtroTrbj = models.CharField(max_length=50)
    InstOtrTrbj = models.CharField(max_length=50)
    PeriodoOtrTrbj = models.IntegerField()
    DescripOtrTrbj = models.CharField(max_length=2500)
    HabLab1 = models.ForeignKey(HabilidadesCarr, on_delete=models.CASCADE)
    HabLab2 = models.ForeignKey(HabilidadesEstd, on_delete=models.CASCADE)
    ObjetivoProf = models.TextField(max_length=400)
    Cedula_Solct = models.ForeignKey(Solicitante, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.Cod_Curriculum) + "(" +str(self.Cedula_Solct) + ")"





