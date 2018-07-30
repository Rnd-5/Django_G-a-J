# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import *
from .forms import *


def home(request):
    return render(request, 'index.html')

def crearSolicitante(request):
    if request.method == 'POST':
        form = SolicitanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('App_Get_a_Job:home')
    else:
        form = SolicitanteForm()
    return render(request, 'crearSolct.html', {'form': form})

def crearEmpleador(request):
    if request.method == 'POST':
        form = EmpleadoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('App_Get_a_Job:home')
    else:
        form = EmpleadoresForm()
    return render(request, 'crearEmpl.html', {'form': form})


def crearOferta(request):
    if request.method == 'POST':
        form = OfertasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('App_Get_a_Job:home')
    else:
        form = OfertasForm()
    return render(request, 'crearOfrt.html', {'form': form})


def login(request):
    return render(request, 'App_Get_a_Job/Login_Registro.html')


def PagP(request):
    return render(request, 'App_G_a_J/C_Principal/PagP.html')
