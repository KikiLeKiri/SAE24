from django.shortcuts import render, redirect
from .models import *

# Create your views here.

from django.shortcuts import render
from .models import Capteur, Donnee

def capteur_list(request):
    capteurs = Capteur.objects.all()
    return render(request, 'appsae/capteur_list.html', {'capteurs': capteurs})

def donnee_list(request):
    donnees = Donnee.objects.all()
    return render(request, 'appsae/donnee_list.html', {'donnees': donnees})
