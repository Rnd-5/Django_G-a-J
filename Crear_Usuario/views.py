# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy


class crearUsuario(CreateView):
    model = User
    form_class =
    template_name = 'Usuarios/crear_usuarios.html'
    success_url = reverse_lazy('App_Get_a_Job:home')


