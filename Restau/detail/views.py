from django.shortcuts import render, get_object_or_404
from traiteur.models import Traiteur

def detail(request, traiteur_id):
    traiteur = get_object_or_404(Traiteur, pk=traiteur_id)
    return render(request, 'detail_trai.html', {'traiteur': traiteur})
