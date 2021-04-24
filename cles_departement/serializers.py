from django.apps import apps
from django.db.models import Sum
from rest_framework import serializers

from .models import ClesDepartement


class DosesSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='vaccin.id')
    nom = serializers.ReadOnlyField(source='vaccin.nom')

    class Meta:
        model = apps.get_model('doses', 'DosesDepartement')
        fields = ('id', 'nom', 'nb_doses', 'nb_doses_par_flacon')


class ClesDepartementSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="departement-detail")
    vaccins = DosesSerializer(source="dosesdepartement_set", many=True, read_only=True)
    nb_doses = serializers.SerializerMethodField()

    class Meta:
        model = ClesDepartement
        fields = '__all__'

    def get_nb_doses(self, obj):
        return obj.nb_doses
