# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render

from .forms import PacientesModelForm
from .models import pacientes 
from .mixin import FormUserNeededMixin
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

def home(request):
    contexto={
        "titulo":"Bienvenido",
        "contenido":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        "home":"active"
    }
    return render(request, 'index.html',contexto)

def nosotros(request):
    contexto={
        "titulo":"Nosotros",
        "subtitle":"Toda la informacion sobre lo que realizamos.",
        "nosotros":"active"
    }
    return render(request,'info.html',contexto)

def contacto(request):
    contexto={
        "titulo":"Contactanos",
        "subtitle":"Contactanos en cualquier momento.",
        "contactanos":"active"
    }
    return render(request,'info.html',contexto)

def lista(request):
    datos=pacientes.objects.all()
    contexto={
        "titulo":"Lista de Pacientes",
        "datos_paciente":datos,
        "subtitle":"Estos son los pacientes que han recibido una consulta",
    }
    return render(request,'listadepacientes.html',contexto)

class Lista_pacientes(ListView):
    model = pacientes

class PacienteCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
	form_class=PacientesModelForm
	template_name="pacientes/create.html"
	success_url="Crear"
	login_url="/crear"

class PacienteUpdateView(UpdateView):
	queryset= pacientes.objects.all()
	form_class=PacientesModelForm
	template_name="editarPaciente.html"
	success_url="/lista/"

class PacienteDeleteView(LoginRequiredMixin,DeleteView):
	model = pacientes
	template_name = "borrarPaciente.html"
	success_url = "/lista/"



def pacientes(request):  # En lugar de json se puede poner xml
    data = serializers.serialize('json', pacientes.objects.all())  # Se puede poner el filtro que se quiera
    return HttpResponse(data, content_type='application/json')



