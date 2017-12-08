"""HistorialMedico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from accounts.views import UserRegisterView
from paciente import views
from paciente.views import home,nosotros,contacto,lista,PacienteDeleteView,PacienteUpdateView,PacienteCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^nosotros/$', views.nosotros, name='ns'),
    url(r'^contacto/$', views.contacto, name='co'),
    url(r'^lista/$',views.lista, name="ls"),
    url('^', include('django.contrib.auth.urls')),
    url(r'^crear/', PacienteCreateView.as_view(), name="cr"),
    url(r'^editar/(?P<pk>\d+)/', PacienteUpdateView.as_view(), name="edit"),
    url(r'^borrar/(?P<pk>\d+)/',PacienteDeleteView.as_view(),name="BorrarElemento"),
    url(r'^accounts/register/$', UserRegisterView.as_view(), name='register'),
    url(r'^pacientes/$', views.pacientes, name='paciente_view'),
]
