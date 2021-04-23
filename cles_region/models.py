from django.db import models


class ClefsRegion(models.Model):
    """
    Modele de donnee pour les clefs de repartition, d'une region a ses departements
    D'apres la commanditaire c'est ppalement fonction de la pop cible dans les depts 
    mais peut etre modifié.
    """
    date = models.DateTimeField(null=False, auto_now=True)
    semaine = models.PositiveSmallIntegerField(null=False)
    # Il faut a la fois l'id region et l'id departement, plus simple meme si on peut facilement retrouver
    # l'un a partir de l'autre
    clef_repartition = models.PositiveSmallIntegerField(null=False, default=0)

    region = models.ForeignKey('CustomUser', on_delete=models.PROTECT)
    departement = models.ForeignKey('CustomUser', on_delete=models.PROTECT)