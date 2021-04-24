from django.apps import apps
from rest_framework import serializers

from .models import ClesRegion


class DosesSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='vaccin.id')
    nom = serializers.ReadOnlyField(source='vaccin.nom')

    class Meta:
        model = apps.get_model('doses', 'DosesRegion')
        fields = ('id', 'nom', 'nb_doses', 'nb_doses_par_flacon')


class ClesRegionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="region-detail")
    vaccins = DosesSerializer(source="dosesregion_set", many=True)

    class Meta:
        model = ClesRegion
        fields = '__all__'
