from django.contrib import admin
from .models import Traiteur


@admin.register(Traiteur)
class TraiteurAdmin(admin.ModelAdmin):
    list_display = [
        'nomcomplet', 
        'specialites', 
        'description', 
        'adresse', 
        'estactif', 
        'email', 
        'datedecreation', 
        'image', 
        'telephone']
    list_filter = ['estactif']
