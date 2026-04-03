from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction
from traiteur.models import Service, Specialite, Traiteur
from .models import TraiteurProfile


def connexion(request):
    if request.user.is_authenticated:
        return redirect('traiteur')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('traiteur')
        else:
            messages.error(request, "E-mail ou mot de passe incorrect")
    else:
        form = AuthenticationForm()

    return render(request, 'connexion.html', {'form': form})


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

        try:
            with transaction.atomic():
                username = email.split('@')[0]
                base_username = username
                counter = 1
                while User.objects.filter(username=username).exists():
                    username = f"{base_username}_{counter}"
                    counter += 1
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

                # Mise à jour des relations Many-to-Many
                if specialites_ids:
                    sps = Specialite.objects.filter(id__in=specialites_ids)
                    profile.specialites.set(sps)
                    traiteur_obj.Specialite.set(sps)

                services_ids = request.POST.getlist('services')
                if services_ids:
                    svcs = Service.objects.filter(id__in=services_ids)
                    profile.services.set(svcs)
                    traiteur_obj.Service.set(svcs)

            messages.success(request, "Inscription réussie. Veuillez vous connecter.")
            return redirect('connexion')
        except Exception as e:
            messages.error(request, f"Une erreur est survenue lors de l'inscription : {e}")

    return render(request, 'inscription-traiteur.html', {'services': services_objects, 'specialites': specialites})


def deconnexion(request):
    logout(request)
    return redirect('connexion')
