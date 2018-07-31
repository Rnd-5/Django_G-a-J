# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import *
from .forms import *


def home(request):
    return render(request, 'index.html')


def crearSolicitante(request):
    if request.method == 'POST':
        form1 = SolicitanteForm(request.POST)
        form2 = EmpleadoresForm(request.POST)
        if form2.fields[7] == form2.fields[6]:
            if form1.is_valid():
                form1.save()
                return redirect('App_Get_a_Job:login')
            if form2.is_valid():
                form2.save()
                return redirect('App_Get_a_Job:login')
        return crearSolicitante(request)
    else:
        form1 = SolicitanteForm()
        form2 = EmpleadoresForm()

    return render(request, 'crearSolct.html', {'form_Solct': form1, 'form_Empl': form2})

def crearEmpleador(request):
    if request.method == 'POST':
        form1 = SolicitanteForm(request.POST)
        form2 = EmpleadoresForm(request.POST)
        if form2.fields[7] == form2.fields[6]:
            if form1.is_valid():
                form1.save()
                return redirect('App_Get_a_Job:login')
            if form2.is_valid():
                form2.save()
                return redirect('App_Get_a_Job:login')
        return crearEmpleador(request)
    else:
        form1 = SolicitanteForm()
        form2 = EmpleadoresForm()
    return render(request, 'crearEmpl2.html', {'form_Solct': form1, 'form_Empl': form2})


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
