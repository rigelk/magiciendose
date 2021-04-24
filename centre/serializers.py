from rest_framework.reverse import reverse
from rest_framework import serializers

from .models import CentreAmbulatoire


class CentreAmbulatoireSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="centre-detail")
    departement = serializers.SerializerMethodField()
    departement_url = serializers.SerializerMethodField()

    class Meta:
        model = CentreAmbulatoire
        fields = ('url', 'gid', 'nom', 'capacite', 'code_postal', 'departement', 'departement_url')

    def get_departement(self, obj):
        return obj.departement

    def get_departement_url(self, obj):
        request = self.context.get('request')
        return "%s?code_postal={}".format(obj.code_postal) % reverse('departement-list', request=request)