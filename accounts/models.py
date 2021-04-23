from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    region = models.ForeignKey('cles_region.ClesRegion', on_delete=models.PROTECT, null=True)
    departement = models.ForeignKey('cles_departement.ClesDepartement', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.email
