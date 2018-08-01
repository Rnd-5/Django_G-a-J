# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import *
from .forms import *
from .models import *
from django.views.generic import *
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


def home(request):
    return render(request, 'App_G_a_J/C_Principal/PagP0.html', {})

def crearSolicitante(request):
    if request.method == 'POST':
        form1 = SolicitanteForm(request.POST)
        form2 = EmpleadoresForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('App_Get_a_Job:Log')
        if form2.is_valid():
            form2.save()
            return redirect('App_Get_a_Job:Log')
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
            return redirect('App_Get_a_Job:Log')
        if form2.is_valid():
            form2.save()
            return redirect('App_Get_a_Job:Log')
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

def Log(request):
    if request.method == 'POST':
        form1 = SolicitanteForm(request.POST)
        form2 = EmpleadoresForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('App_Get_a_Job:Log')
        if form2.is_valid():
            form2.save()
            return redirect('App_Get_a_Job:Log')
    else:
        form1 = SolicitanteForm()
        form2 = EmpleadoresForm()
    return render(request, 'crearEmpl2.html', {'form_Solct': form1, 'form_Empl': form2})

def PagP(request):
    return render(request, 'App_G_a_J/C_Principal/PagP_0.html')

def PerfilSolct(request):
    return render(request, 'App_G_a_J/Prototipo_VistaPerfil.html', {})
"""
def crearCurriculum(request):
    if request.method == 'POST':
        form = CurriculumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('App_Get_a_Job:PerfilSolct')
    else:
        form = CurriculumForm()
    return render(request, 'crearEmpl2.html', {'form': form})
"""
def list_Solicitantes(request):
    solicitante = Solicitante.objects.all()
    contexto = {'solicitantes': solicitante}
    return render(request, 'Perfiles.html', contexto)


class l_Solicitante(ListView):
    model = Solicitante
    template_name = 'App_G_a_J/C_Principal/Perfiles.html'


def curriulum_view(request):
    if request.method == 'POST':
        form = CurriculumForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('App_G_a_J: home')
    else:
        form = CurriculumForm()
    return render(request, 'App_G_a_J/curriculum.html', {'form': form})





"""class Login(FormView):
    template_name = 'App_G_a_J/Login_Registro.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy("App_Get_a_Job:PagP")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)
"""