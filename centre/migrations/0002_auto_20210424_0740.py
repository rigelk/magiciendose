# Generated by Django 3.1.8 on 2021-04-24 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centreambulatoire',
            name='departement',
        ),
        migrations.AddField(
            model_name='centreambulatoire',
            name='id_ministere',
            field=models.IntegerField(default=0),
        ),
    ]