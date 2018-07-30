# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


admin.site.register(Solicitante)
admin.site.register(Empleadores)
admin.site.register(Oferta_Empl)
admin.site.register(TipoEmpresa)
