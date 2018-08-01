# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import *
from .forms import *
from .models import *


def home(request):
    return render(request, 'index.html')

def crearSolicitante(request):
    if request.method == 'POST':
        form1 = SolicitanteForm(request.POST)
        form2 = EmpleadoresForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('App_Get_a_Job:login')
        if form2.is_valid():
            form2.save()
            return redirect('App_Get_a_Job:login')
    else:
        form1 = SolicitanteForm()
        form2 = EmpleadoresForm()

    return render(request, 'crearSolct.html', {'form_Solct': form1, 'form_Empl': form2})

def crearEmpleador(request):
    if request.method == 'POST':
        form1 = SolicitanteForm(request.POST)
        form2 = EmpleadoresForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('App_Get_a_Job:login')
        if form2.is_valid():
            form2.save()
            return redirect('App_Get_a_Job:login')
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
    if request.method == 'POST':
        form1 = SolicitanteForm(request.POST)
        form2 = EmpleadoresForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('App_Get_a_Job:login')
        if form2.is_valid():
            form2.save()
            return redirect('App_Get_a_Job:login')
    else:
        form1 = SolicitanteForm()
        form2 = EmpleadoresForm()
    return render(request, 'crearEmpl2.html', {'form_Solct': form1, 'form_Empl': form2})


def PagP(request):
    return render(request, 'App_G_a_J/C_Principal/PagP.html')


def list_Solicitantes(request):
    solicitante = Solicitante.objects.all()
    contexto = {'solicitantes': solicitante}
    return render(request, 'listar_Usuarios.html', contexto)
"""
class CrearUsuario(CreateView):
    model = User
    form_class = UserForm
    template_name = 'crearUsuario.html'
    success_url = reverse_lazy('App_Get_a_Job:home')
"""
