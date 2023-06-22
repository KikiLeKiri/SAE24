from django.shortcuts import render
from .models import *

# Create your views here.

def capteur_list(request):
    capteurs = Capteur.objects.all()
    context = {'capteurs': capteurs}
    return render(request, 'appsae/capteur_list.html', context)

def donnee_list(request, capteur_id):
    if request.method == 'POST':
        capteur_id = request.POST.get('capteur_id')
        donnees = Donnee.objects.filter(id=capteur_id)
        context = {'donnees': donnees}
        return render(request, 'appsae/donnee_list.html', context)

