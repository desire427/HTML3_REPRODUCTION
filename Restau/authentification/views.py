from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from traiteur.models import Service, Specialite, Traiteur
from .models import TraiteurProfile


def connexion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Utilisateur introuvable")
            return render(request, 'connexion.html')

        utilisateur = authenticate(username=user.username, password=password)
        if utilisateur is not None:
            login(request, utilisateur)
            return redirect('traiteur')
        else:
            messages.error(request, "E-mail ou mot de passe incorrect")

    return render(request, 'connexion.html')


def inscription(request):
    services_objects = Service.objects.all()
    specialites = Specialite.objects.all()

    if request.method == 'POST':
        nom_complet = request.POST.get('nom_complet')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirme_password = request.POST.get('confirme_password')
        specialites_ids = request.POST.getlist('specialites')
        annee_experience = request.POST.get('annee-expe')
        description = request.POST.get('Description')
        telephone = request.POST.get('telephone')
        adresse = request.POST.get('adresse')
        photo = request.FILES.get('photo')

        if password != confirme_password:
            messages.error(request, "Les mots de passe ne correspondent pas")
            return render(request, 'inscription-traiteur.html', {'services': services_objects, 'specialites': specialites})

        if not email:
            messages.error(request, "Email est requis")
            return render(request, 'inscription-traiteur.html', {'services': services_objects, 'specialites': specialites})

        if User.objects.filter(email=email).exists():
            messages.error(request, "Un compte existe deja avec cet email")
            return render(request, 'inscription-traiteur.html', {'services': services_objects, 'specialites': specialites})

        username = email.split('@')[0]
        if User.objects.filter(username=username).exists():
            username = f"{username}_{User.objects.count()+1}"

        user = User.objects.create_user(username=username, email=email, password=password)
        profile = TraiteurProfile.objects.create(
            user=user,
            nom_complet=nom_complet,
            categorie='',
            annee_experience=int(annee_experience or 0),
            description=description,
            telephone=telephone,
            adresse=adresse,
            photo=photo,
        )

        traiteur_obj = Traiteur.objects.create(
            nomcomplet=nom_complet,
            description=description,
            adresse=adresse,
            estactif=True,
            email=email,
            telephone=telephone,
            annee_experience=int(annee_experience or 0),
            image=photo,
        )

        if specialites_ids:
            for specialite_id in specialites_ids:
                try:
                    sp = Specialite.objects.get(id=specialite_id)
                    profile.specialites.add(sp)
                    traiteur_obj.Specialite.add(sp)
                except Specialite.DoesNotExist:
                    pass

        services_ids = request.POST.getlist('services')
        if services_ids:
            for service_id in services_ids:
                try:
                    svc = Service.objects.get(id=service_id)
                    profile.services.add(svc)
                    traiteur_obj.Service.add(svc)
                except Service.DoesNotExist:
                    pass

        traiteur_obj.save()
        messages.success(request, "Inscription réussie. Veuillez vous connecter.")
        return redirect('connexion')

    return render(request, 'inscription-traiteur.html', {'services': services_objects, 'specialites': specialites})


def deconnexion(request):
    logout(request)
    return redirect('connexion')
