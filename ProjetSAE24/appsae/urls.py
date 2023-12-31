"""ProjetSAE24 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('capteur_list/', views.capteur_list, name='capteur_list'),
    path('donnee_list/<int:capteur_id>/', views.donnee_list, name='donnee_list'),
    path('modifier_capteur/<int:capteur_id>/', views.modifier_capteur, name='modifier_capteur'),
    path('toute_donnee/', views.toute_donnee, name='toute_donnee'),
    path('graphique/<int:capteur_id>/', views.affichage_graphique, name='graphique'),
    path('export-csv/<int:capteur_id>/', views.export_csv, name='export_csv'),

]