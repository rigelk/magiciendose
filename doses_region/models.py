from django.db import models


class DosesRegion(models.Model):
    """
    Sortie du fichier output fourni par le MSS : nb de doses de chaque marque de vaccin pour la region
    """
    date = models.DateTimeField(null=False, auto_now=True)
    semaine = models.PositiveSmallIntegerField(null=False)
    nb_doses = models.PositiveSmallIntegerField(default=0)

    region = models.ForeignKey('CustomUser', on_delete=models.PROTECT)
    vaccin = models.ForeignKey('Vaccin', on_delete=models.PROTECT)