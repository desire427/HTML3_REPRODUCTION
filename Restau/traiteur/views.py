from django.shortcuts import render
from .models import Traiteur, Specialite, Service , Langue
from django.http import HttpResponse


def traiteur(request):
    traiteurs = Traiteur.objects.all()
    specialites = Specialite.objects.all()
    services = Service.objects.all()
    Langues = Langue.objects.all()

    return render(request, 'traiteur.html', {
        'traiteurs': traiteurs,
        'specialites': specialites,
        'services': services,
        'langue': Langue,
    })


def liste_traiteurs(request):
    return traiteur(request)



