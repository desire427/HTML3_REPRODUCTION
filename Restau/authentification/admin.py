from django.contrib import admin
from .models import TraiteurProfile


@admin.register(TraiteurProfile)
class TraiteurProfileAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'user', 'telephone', 'adresse', 'categorie', 'annee_experience', 'get_specialites')
    search_fields = ('nom_complet', 'user__email', 'telephone', 'adresse', 'categorie')

    def get_specialites(self, obj):
        return ", ".join([s.specialite for s in obj.specialites.all()])
    get_specialites.short_description = 'Specialites'
