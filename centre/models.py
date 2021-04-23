from django.db import models


class CentreAmbulatoire(models.Models):
    """
    Modele de donnee pour les centres de vaccination ambulatoires
    """
    nom = models.CharField(max_length=1000)
    capacite = models.PositiveSmallIntegerField(null=False, default=0)
    code_postal = models.CharField(max_length=5)
    departement = models.CharField(max_length=2)
