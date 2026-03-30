from django.urls import path
from . import views

urlpatterns = [
    path('traiteur/', views.traiteur, name='traiteur'),
    path('liste_traiteurs/', views.liste_traiteurs, name='liste_traiteurs'),
]