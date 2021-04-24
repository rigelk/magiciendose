from rest_framework import serializers

from .models import ClesDepartement


class ClesDepartementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClesDepartement
        fields = '__all__'