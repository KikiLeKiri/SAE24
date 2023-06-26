from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from .forms import *

# Create your views here.

def capteur_list(request):
    capteurs = Capteur.objects.all()
    return render(request, 'appsae/capteur_list.html', {'capteurs': capteurs})

def donnee_list(request, capteur_id):
    capteur = Capteur.objects.get(id=capteur_id)
    donnees = Donnee.objects.filter(id_capteur=capteur)

    # Filtrer les données en fonction des paramètres de filtre
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')

    if start_date:
        donnees = donnees.filter(datte__gte=start_date)
    if end_date:
        donnees = donnees.filter(datte__lte=end_date)
    if start_time:
        donnees = donnees.filter(heure__gte=start_time)
    if end_time:
        donnees = donnees.filter(heure__lte=end_time)

    context = {
        'capteur': capteur,
        'donnees': donnees
    }
    return render(request, 'appsae/donnee_list.html', context)


def modifier_capteur(request, capteur_id):
    capteur = Capteur.objects.get(id=capteur_id)

    if request.method == 'POST':
        form = CapteurForm(request.POST, instance=capteur)
        if form.is_valid():
            form.save()
            return redirect('donnee_list', capteur_id=capteur_id)
    else:
        form = CapteurForm(instance=capteur)

    return render(request, 'appsae/modifier_capteur.html', {'form': form, 'capteur_id': capteur_id})
