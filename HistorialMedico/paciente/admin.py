# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import pacientes

class PacientesAdmin(admin.ModelAdmin):
    list_display = ["Paciente","Edad","Motivo_de_Consulta","Recomendaciones","Receta_Medica"]
    searchfield = ["Paciente"]
    list_filter = ["Edad"]

    class Meta:
        Model = pacientes
admin.site.register(pacientes, PacientesAdmin)