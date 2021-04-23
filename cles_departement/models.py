from django.db import models


class ClefsDepartement(models.Model):
    """
    Modele de donnée pour les clefs de repartition, d'un departement à ses CVA
    """
    date = models.DateTimeField(null=False, auto_now=True)
    semaine = models.PositiveSmallIntegerField(null=False)

    # Personne qui suggere des doses, en fait ca peut etre l'ARS ou le departement
    user = models.ForeignKey('CustomUser', on_delete=models.PROTECT)
    # Departement vise
    departement_cible = models.ForeignKey('CustomUser', on_delete=models.PROTECT)
    # Centre vise
    centre = models.ForeignKey('CentreAmbulatoire', on_delete=models.PROTECT)
    vaccin = models.ForeignKey('Vaccin', on_delete=models.PROTECT)

    FIRST = '1'
    SECOND = '2'
    INJECTIONS_CHOICES = [
        (FIRST, 1),
        (SECOND, 2)
    ]
    numero_injection = models.CharField(
        max_length=1,
        choices=INJECTIONS_CHOICES,
        default=FIRST,
        null=False
    )
    nb_doses = models.PositiveSmallIntegerField(default=0)