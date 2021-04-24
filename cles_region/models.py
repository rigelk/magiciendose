from django.db import models
import pandas


def get_enum_regions():
    """
    Retourne une enumeration des departements francais
    :return:
    """
    df = pandas.read_csv("data/region2020.csv", delimiter=",")
    df['region'] = [str(e).zfill(2) for e in df['reg']]
    enum_region = [(i + 1, "{} - {}".format(e.region, e.libelle),) for i, e in df.iterrows()]

    return enum_region


class ClesRegion(models.Model):
    """
    Modele de donnee pour les clefs de repartition, d'une region a ses departements
    D'apres la commanditaire c'est principalement fonction de la populatio cible dans les departements
    mais peut etre modifié.
    """
    date_de_saisie = models.DateTimeField(null=False, auto_now_add=True)
    date_de_derniere_modification = models.DateTimeField(null=False, auto_now=True)

    semaine_de_vaccination = models.PositiveSmallIntegerField(null=False)
    regions = get_enum_regions()
    numero_region = models.CharField(
        max_length=2,
        choices=regions,
        default=regions[0],
        null=False
    )

    # Il faut a la fois l'id region et l'id departement, plus simple meme si on peut 
    # facilement retrouver l'un a partir de l'autre
    clef_repartition = models.PositiveSmallIntegerField(null=False, default=0)

    vaccins = models.ManyToManyField('vaccin.Vaccin', through='doses.DosesRegion')