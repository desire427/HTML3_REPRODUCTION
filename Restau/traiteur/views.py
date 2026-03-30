from django.shortcuts import render
from .models import Traiteur

def traiteur(request):
    return render(request, 'traiteur.html')


def liste_traiteurs(request):
    traiteurs = Traiteur.objects.all()
    return render(request, 'liste.html', {'traiteurs': traiteurs})