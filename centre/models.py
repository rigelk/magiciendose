from django.db import models
from pgeocode import Nominatim
nomi = Nominatim('fr')


class CentreAmbulatoire(models.Model):
    """
    Modele de donnee pour les centres de vaccination ambulatoires
    """
    id_ministere = models.IntegerField(default=0) # id utilisé par le ministère
    nom = models.CharField(max_length=1000)
    capacite = models.PositiveSmallIntegerField(null=False, default=0) # capacité en nb de vaccins
    code_postal = models.PositiveSmallIntegerField(null=True)

    @property
    def departement(self):
        return nomi.query_postal_code(self.code_postal).county_name