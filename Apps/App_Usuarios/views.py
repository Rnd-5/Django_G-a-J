# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy

"""
class CrearUsuario(CreateView):
    model = User
    form_class =
    template_name = 'App_Usuarios/crearUsuario.html'
    success_url = reverse_lazy
"""