from django.db import models
from django.utils import timezone

class Traiteur(models.Model):
    nomcomplet = models.CharField(max_length=100)
    specialites = models.TextField()
    description = models.TextField()
    adresse = models.CharField(max_length=200)
    estactif = models.BooleanField()
    email = models.EmailField()
    datedecreation = models.DateField(default=timezone.now)
    image = models.URLField(blank=True, null=True)
    telephone = models.CharField(max_length=20)

def __str__(self):
    return self.nomcomplet

