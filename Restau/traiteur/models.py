from django.db import models
from django.utils import timezone


class Specialite(models.Model):
    specialite = models.CharField(max_length=100)

    def __str__(self):
        return self.specialite
    

class Service(models.Model):
    Service = models.CharField(max_length=100)

    def __str__(self):
        return self.Service

class Langue(models.Model):
    langue = models.CharField(max_length=100)

    def __str__(self):
        return self.langue


class Traiteur(models.Model):
    nomcomplet = models.CharField(max_length=100)
    Specialite = models.ManyToManyField(Specialite)
    description = models.TextField()
    adresse = models.CharField(max_length=200)
    estactif = models.BooleanField()
    email = models.EmailField()
    datedecreation = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='traiteurs/', blank=True, null=True)
    telephone = models.CharField(max_length=20)
    annee_experience = models.IntegerField(default=0)
    Service = models.ManyToManyField(Service)
    langue = models.ManyToManyField(Langue)



    def __str__(self):
        return self.nomcomplet
