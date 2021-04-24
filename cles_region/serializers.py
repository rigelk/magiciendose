from rest_framework import serializers

from .models import ClesRegion


class ClesRegionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="region-detail")
    class Meta:
        model = ClesRegion
        fields = '__all__'