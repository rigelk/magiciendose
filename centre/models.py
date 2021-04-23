from django.db import models


class CentreAmbulatoire(models.Model):
    """
    Modele de donnee pour les centres de vaccination ambulatoires
    """
    nom = models.CharField(max_length=1000)
    capacite = models.PositiveSmallIntegerField(null=False, default=0)
    code_postal = models.PositiveSmallIntegerField(null=True)
    departement = models.PositiveSmallIntegerField(null=True)
