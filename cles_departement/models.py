from django.db import models
from mixins.models import GeoCodeMixin
from enum import Enum
import pandas
import numpy as np


def get_enum_depts() -> Enum:
    """
    Retourne une enumeration des departements francais
    :return:
    """
    df = pandas.read_csv("cles_departement/departements-francais.csv", delimiter="\t")
    df['dept'] = [str(e).zfill(2) for e in df['NUMÉRO']]
    df.drop([101, 102], axis=0, inplace=True)
    enum_dept = [(i + 1, "{} - {}".format(e.dept, e.NOM)) for i, e in df.iterrows()]

    return enum_dept


class ClesDepartement(GeoCodeMixin):
    """
    Modele de donnée pour les clefs de repartition, d'un departement à ses CVA
    """
    date_de_saisie = models.DateTimeField(null=False, auto_now_add=True)
    date_de_derniere_modification = models.DateTimeField(null=False, auto_now=True)
    date_de_validation_provisoire = models.DateTimeField(null=True)
    date_de_validation = models.DateTimeField(null=True)

    semaine_de_vaccination = models.PositiveSmallIntegerField(null=True)

    vaccins = models.ManyToManyField('vaccin.Vaccin', through='doses.DosesDepartement')

    numero_injection = models.CharField(
        max_length=1,
        choices=[
            (1, '1'),
            (2, '2')
        ],
        default=(1, '1'),
        null=False
    )
    numero_departement = models.CharField(
        max_length=3,
        choices=get_enum_depts(),
        default=get_enum_depts()[0],
        null=False
    )
    nb_doses = models.PositiveSmallIntegerField(default=0)