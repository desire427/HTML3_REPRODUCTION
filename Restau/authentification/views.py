from django.shortcuts import render

def connexion(request):
    return render(request, 'connexion.html')

def inscription(request):
    return render(request, 'inscription-traiteur.html')
