# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class pacientes(models.Model):
    Paciente = models.CharField(max_length=100)
    Edad = models.CharField(max_length=100)
    Motivo_de_Consulta = models.CharField(max_length=100)
    Recomendaciones = models.CharField(max_length=100)
    Receta_Medica = models.CharField(max_length=100)
