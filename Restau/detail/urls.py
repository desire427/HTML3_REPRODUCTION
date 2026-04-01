from django.urls import path
from . import views

urlpatterns = [
    path("detail/<int:traiteur_id>/", views.detail, name="detail"),
]