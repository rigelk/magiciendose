from django.db import models


class Vaccin(models.Model):
    """
    Modele de donnee pour les marques de vaccin
    """
    nom = models.CharField(max_length=20)
    # si on veut, on rajoute qqc sur l'intervalle entre les deux doses, en jours
    intervalle_injections = models.PositiveSmallIntegerField(null=False, default=28)
