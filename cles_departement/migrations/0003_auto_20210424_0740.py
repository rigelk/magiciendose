# Generated by Django 3.1.8 on 2021-04-24 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cles_departement', '0002_clesdepartement_vaccins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clesdepartement',
            name='user',
        ),
        migrations.AlterField(
            model_name='clesdepartement',
            name='numero_injection',
            field=models.CharField(choices=[('1', 1), ('2', 2)], default=('1', 1), max_length=1),
        ),
    ]
