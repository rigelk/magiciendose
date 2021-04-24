from rest_framework import serializers

from .models import ClesDepartement


class ClesDepartementSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="departement-list")

    class Meta:
        model = ClesDepartement
        exclude = ['centre']