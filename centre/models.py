from django.db import models
from django.db.models import Sum
from mixins.models import GeoCodeMixin


class CentreAmbulatoire(GeoCodeMixin):
    """
    Modele de donnee pour les centres de vaccination ambulatoires
    """
    gid = models.IntegerField(default=0) # id utilisé par le ministère
    nom = models.CharField(max_length=1000)
    capacite = models.PositiveSmallIntegerField(null=False, default=0) # capacité en nb de vaccins

    vaccins = models.ManyToManyField('vaccin.Vaccin', through='doses.DosesCentre')

    @property
    def nb_doses(self):
        return self.dosescentre_set.aggregate(total=Sum('nb_doses'))['total']