from django.contrib import admin
from .models import Traiteur , Specialite , Service , Langue


@admin.register(Traiteur)
class TraiteurAdmin(admin.ModelAdmin):
    def specialites(self, obj):
        return ", ".join([s.specialite for s in obj.Specialite.all()])
    specialites.short_description = 'Specialite'

    def services(self, obj):
        return ", ".join([s.Service for s in obj.Service.all()])
    services.short_description = 'Service'

    def langue(self, obj):
        return ", ".join([s.langue for s in obj.langue.all()])
    langue.short_description = 'Langue'

    list_display = [
        'nomcomplet',
        'specialites',
        'description',
        'adresse',
        'estactif',
        'email',
        'datedecreation',
        'image',
        'telephone',
        'annee_experience',
        'services',
        'langue',
    ]
    search_fields = [
        'nomcomplet',
    ]
    list_filter = ['estactif']

@admin.register(Specialite)
class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ['specialite']
    search_fields = ['specialite']
    list_filter = ['specialite']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['Service']
    search_fields = ['Service']
    list_filter = ['Service']

@admin.register(Langue)
class LangueAdmin(admin.ModelAdmin):
    list_display = ['langue']
    search_fields = ['langue']
    list_filter = ['langue']