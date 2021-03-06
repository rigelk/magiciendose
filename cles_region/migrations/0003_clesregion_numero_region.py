# Generated by Django 3.1.8 on 2021-04-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cles_region', '0002_clesregion_vaccins'),
    ]

    operations = [
        migrations.AddField(
            model_name='clesregion',
            name='numero_region',
            field=models.CharField(choices=[(1, '01 - Guadeloupe'), (2, '02 - Martinique'), (3, '03 - Guyane'), (4, '04 - La Réunion'), (5, '06 - Mayotte'), (6, '11 - Île-de-France'), (7, '24 - Centre-Val de Loire'), (8, '27 - Bourgogne-Franche-Comté'), (9, '28 - Normandie'), (10, '32 - Hauts-de-France'), (11, '44 - Grand Est'), (12, '52 - Pays de la Loire'), (13, '53 - Bretagne'), (14, '75 - Nouvelle-Aquitaine'), (15, '76 - Occitanie'), (16, '84 - Auvergne-Rhône-Alpes'), (17, "93 - Provence-Alpes-Côte d'Azur"), (18, '94 - Corse')], default=(1, '01 - Guadeloupe'), max_length=2),
        ),
    ]
