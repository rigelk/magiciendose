# Generated by Django 3.1.8 on 2021-04-23 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20210423_1811'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('cles_region', '0002_clesregion_vaccins'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cles_region.clesregion'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]