from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, 'appsae/index.html')

def maison1_list(request):
    maisons = Maison1.objects.all()
    context = {'maisons': maisons}
    return render(request, 'appsae/maison1_list.html', context)
