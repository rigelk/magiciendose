from django.db import models
from pgeocode import Nominatim

nomi = Nominatim('fr')


class GeoCodeMixin(models.Model):
    code_postal = models.PositiveSmallIntegerField(null=True)
    code_commune_insee = models.PositiveSmallIntegerField(null=True)

    @property
    def departement(self):
        return nomi.query_postal_code(self.code_postal).county_name

    class Meta:
       abstract = True
