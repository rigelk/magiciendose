# Generated by Django 3.1.8 on 2021-04-23 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cles_region', '0001_initial'),
        ('cles_departement', '0001_initial'),
        ('vaccin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DosesRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_doses', models.PositiveSmallIntegerField(default=0)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cles_region.clesregion')),
                ('vaccin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccin.vaccin')),
            ],
        ),
        migrations.CreateModel(
            name='DosesDepartement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_doses', models.PositiveSmallIntegerField(default=0)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cles_departement.clesdepartement')),
                ('vaccin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccin.vaccin')),
            ],
        ),
    ]