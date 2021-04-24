from django.apps import apps
from django.db.models import Sum
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
    vaccins = DosesSerializer(source="dosesregion_set", many=True, read_only=True)
    nb_doses = serializers.SerializerMethodField()

    class Meta:
        model = ClesRegion
        fields = '__all__'

    def get_nb_doses(self, obj):
        return obj.nb_doses