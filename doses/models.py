from django.db import models


class DosesRegion(models.Model):
    """
    Sortie du fichier output fourni par le MSS : nb de doses de chaque marque de vaccin pour la region
    """
    nb_doses = models.PositiveSmallIntegerField(default=0)


class DosesDepartement(models.Model):
    """
    Sortie du fichier output fourni par le MSS : nb de doses de chaque marque de vaccin pour le département
    """
    nb_doses = models.PositiveSmallIntegerField(default=0)
