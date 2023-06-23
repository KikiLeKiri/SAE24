from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def capteur_list(request):
    capteurs = Capteur.objects.all()
    return render(request, 'appsae/capteur_list.html', {'capteurs': capteurs})

def donnee_list(request, capteur_id):
    capteur = Capteur.objects.get(id=capteur_id)
    donnees = Donnee.objects.filter(id_capteur=capteur_id)
    return render(request, 'appsae/donnee_list.html', {'capteur': capteur, 'donnees': donnees})
