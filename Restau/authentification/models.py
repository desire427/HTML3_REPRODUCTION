from django.db import models
from django.contrib.auth.models import User


class TraiteurProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom_complet = models.CharField(max_length=150)
    categorie = models.CharField(max_length=100, blank=True)
    annee_experience = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    adresse = models.CharField(max_length=255, blank=True)
    services = models.ManyToManyField('traiteur.Service', blank=True)
    specialites = models.ManyToManyField('traiteur.Specialite', blank=True)
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.nom_complet} ({self.user.email})"
