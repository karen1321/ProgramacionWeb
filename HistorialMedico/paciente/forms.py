from django import forms

from .models import pacientes

class PacientesModelForm(forms.ModelForm):
    

    class Meta:
        model = pacientes
        fields = [
            "Paciente",
            "Edad",
            "Motivo_de_Consulta",
            "Recomendaciones",
            "Receta_Medica"
        ]