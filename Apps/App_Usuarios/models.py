# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import *


class PersonalizadoBaseUserManager(BaseUserManager):
    def create_user(self, usuario, password):
        user = self.model(usuario=usuario)
        user.set_password(password)
        user.save()

class CrearUsuario(AbstractBaseUser, PermissionsMixin):
    usuario = models.CharField(max_length=50, unique=True)
    observaciones = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
"""
USERNAME_FIELD = 'usuario'

object = PersonalizadoBaseUserManager()

def get_full_name(self):
    return self.usuario

def get_short_name(self):
    return self.usuario
"""