from django.db import models


class DosesRegion(models.Model):
    """
    Sortie du fichier output fourni par le MSS : nb de doses de chaque marque de vaccin pour la region
    """
    region = models.ForeignKey('cles_region.ClesRegion', on_delete=models.CASCADE)
    vaccin = models.ForeignKey('vaccin.Vaccin', on_delete=models.CASCADE)

    nb_doses = models.PositiveSmallIntegerField(default=0)


class DosesDepartement(models.Model):
    """
    Sortie du fichier output fourni par le MSS : nb de doses de chaque marque de vaccin pour le département
    """
    departement = models.ForeignKey('cles_departement.ClesDepartement', on_delete=models.CASCADE)
    vaccin = models.ForeignKey('vaccin.Vaccin', on_delete=models.CASCADE)

    nb_doses = models.PositiveSmallIntegerField(default=0)
