from rest_framework import serializers

from .models import CentreAmbulatoire


class CentreAmbulatoireSerializer(serializers.HyperlinkedModelSerializer):
    departement = serializers.SerializerMethodField()

    class Meta:
        model = CentreAmbulatoire
        fields = ('url', 'nom', 'capacite', 'code_postal', 'departement')

    def get_departement(self, obj):
        return obj.departement