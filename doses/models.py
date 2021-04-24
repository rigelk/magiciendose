from django.db import models


class Doses(models.Model):
    vaccin = models.ForeignKey('vaccin.Vaccin', on_delete=models.CASCADE)

    nb_doses = models.PositiveSmallIntegerField(null=False, default=0)
    nb_doses_par_flacon = models.PositiveSmallIntegerField(null=False, default=0)

    numero_injection = models.CharField(
        max_length=1,
        choices=[
            (1, '1'),
            (2, '2')
        ],
        default=(1, '1'),
        null=True # doit être null quand renseigne une relation departement<->vaccin ou region<->vaccin ; doit avoir une valeur pour une relation centre<->vaccin
    )
    class Meta:
        abstract = True

class DosesRegion(Doses):
    """
    Sortie du fichier output fourni par le MSS : nb de doses de chaque marque de vaccin pour la region
    """
    region = models.ForeignKey('cles_region.ClesRegion', on_delete=models.CASCADE)


class DosesDepartement(Doses):
    departement = models.ForeignKey('cles_departement.ClesDepartement', on_delete=models.CASCADE)


class DosesCentre(Doses):
    centre = models.ForeignKey('centre.CentreAmbulatoire', on_delete=models.CASCADE)
