from django.db import models


class ClesDepartement(models.Model):
    """
    Modele de donnée pour les clefs de repartition, d'un departement à ses CVA
    """
    date_de_saisie = models.DateTimeField(null=False, auto_now_add=True)
    date_de_derniere_modification = models.DateTimeField(null=False, auto_now=True)
    date_de_validation_provisoire = models.DateTimeField()
    date_de_validation = models.DateTimeField()

    # Personne qui suggere des doses, en fait ca peut etre l'ARS ou le departement
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.PROTECT)

    # Centre vise
    centre = models.ForeignKey('centre.CentreAmbulatoire', on_delete=models.PROTECT)
    vaccins = models.ManyToManyField('vaccin.Vaccin', through='doses.DosesDepartement')

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