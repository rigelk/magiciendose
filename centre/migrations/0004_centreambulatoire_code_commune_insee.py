# Generated by Django 3.1.8 on 2021-04-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0003_auto_20210424_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='centreambulatoire',
            name='code_commune_insee',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
