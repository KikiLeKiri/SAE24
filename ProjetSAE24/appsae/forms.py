from django import forms
from .models import Capteur, Donnee

class CapteurForm(forms.ModelForm):
    class Meta:
        model = Capteur
        fields = ['nom_capteur', 'piece']

class DonneeForm(forms.ModelForm):
    class Meta:
        model = Donnee
        fields = ['id_capteur', 'date_field', 'heure', 'temperature']
