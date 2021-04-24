from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

from .serializers import ClesRegionSerializer
from .models import ClesRegion


class RegionFilterSet(django_filters.FilterSet):
   class Meta:
       model = ClesRegion
       fields = ('date_de_saisie', 'date_de_derniere_modification', 'semaine_de_vaccination', 'clef_repartition')


class ClesRegionViewSet(viewsets.ModelViewSet):
    queryset = ClesRegion.objects.all()
    serializer_class = ClesRegionSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('semaine_de_vaccination')
    filterset_class = RegionFilterSet
