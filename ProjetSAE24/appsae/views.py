from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views import View
from .models import *
from .forms import *
from datetime import datetime
import plotly.graph_objects as go
from plotly.offline import plot
import csv


# Create your views here.

def capteur_list(request):
    capteurs = Capteur.objects.all()
    return render(request, 'appsae/capteur_list.html', {'capteurs': capteurs})

def donnee_list(request, capteur_id):
    capteur = Capteur.objects.get(id=capteur_id)
    donnees = Donnee.objects.filter(id_capteur=capteur)

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

def toute_donnee(request):
    datatest = []
    capteurs = Capteur.objects.all()
    donnees = Donnee.objects.all()
    for capteur in capteurs:
        data = Donnee.objects.filter(id_capteur = capteur)
        datatest.append([capteur, data] )
    context = {
        'capteurs': capteurs,
        'donnees': donnees,
        'dataset' : datatest                
    }
    return render(request, 'appsae/toute_donnee.html', context)

def affichage_graphique(request, capteur_id):
    capteur = Capteur.objects.get(id=capteur_id)

    donnees = Donnee.objects.filter(id_capteur=capteur)

    x = [donnee.heure for donnee in donnees]
    y = [donnee.temperature for donnee in donnees]

    fig = go.Figure(data=go.Scatter(x=x, y=y))
    graph = plot(fig, output_type='div')

    context = {'capteur': capteur, 'graph': graph}
    return render(request, 'appsae/graphique.html', context)

def export_csv(request, capteur_id):
    capteur = Capteur.objects.get(id=capteur_id)
    donnees = Donnee.objects.filter(id_capteur=capteur)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="donnees_capteur.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Date', 'Heure', 'Temperature', 'Nom Capteur', 'Pièce'])
    
    for donnee in donnees:
        writer.writerow([donnee.datte, donnee.heure, donnee.temperature, capteur.nom_capteur, capteur.piece])
    
    return response
