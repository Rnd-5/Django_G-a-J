# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Solicitante(models.Model):
    Cedula = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=100)
    Sexo = models.CharField(max_length=1)
    Fecha_Nacimiento = models.DateField()
    Email = models.EmailField(max_length=50)
    Clave = models.CharField(max_length=75)
    Estado = models.CharField(max_length=1)

    def __str__(self):
        return self.Nombre + " " + self.Apellido


class TipoEmpresa(models.Model):
    Cod_TipoEmpr = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=5)
    Descripcion = models.CharField(max_length=60)

    def __str__(self):
        return self.Nombre

class Empleadores(models.Model):
    RNC = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    FechaConst = models.DateField()
    Direccion = models.CharField(max_length=200)
    FormaJurd = models.ForeignKey(TipoEmpresa, on_delete=models.CASCADE)
    Email = models.EmailField(max_length=50)
    Clave = models.CharField(max_length=75)
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


