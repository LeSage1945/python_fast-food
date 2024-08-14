# myapp/models.py

from django.db import models
from django.contrib.auth.models import User

class Auteur(models.Model):
    nom = models.CharField(max_length=50, null=True)
    nationalite = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Livre(models.Model):
    titre = models.CharField(null=True, max_length=50)
    auteur = models.ForeignKey(Auteur, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.titre} - {self.auteur}"
    