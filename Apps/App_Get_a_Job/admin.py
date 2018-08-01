# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


admin.site.register(Solicitante)
admin.site.register(Empleadores)
admin.site.register(Oferta_Empl)
admin.site.register(TipoEmpresa)
admin.site.register(Genero)

admin.site.register(InstEstd)
admin.site.register(Carreras)
admin.site.register(HabilidadesCarr)
admin.site.register(OtrosEstd)
admin.site.register(HabilidadesEstd)
admin.site.register(Provincias)
admin.site.register(Curriculum)
admin.site.register(Paises)