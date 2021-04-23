from rest_framework import serializers

from .models import Vaccin


class VaccinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaccin