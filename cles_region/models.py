from django.db import models


class ClefsRegion(models.Model):
    """
    Modele de donnee pour les clefs de repartition, d'une region a ses departements
    D'apres la commanditaire c'est principalement fonction de la populatio cible dans les departements
    mais peut etre modifié.
    """
    date_de_saisie = models.DateTimeField(null=False, auto_now_add=True)
    date_de_derniere_modification = models.DateTimeField(null=False, auto_now=True)

    semaine_de_vaccination = models.PositiveSmallIntegerField(null=False)

    # Il faut a la fois l'id region et l'id departement, plus simple meme si on peut 
    # facilement retrouver l'un a partir de l'autre
    clef_repartition = models.PositiveSmallIntegerField(null=False, default=0)

    region = models.ForeignKey('accounts.CustomUser', on_delete=models.PROTECT)
    departement = models.ForeignKey('accounts.CustomUser', on_delete=models.PROTECT)
    vaccins = models.ManyToManyField('vaccin.Vaccin', through='doses.DosesRegion')